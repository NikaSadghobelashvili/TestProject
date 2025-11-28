from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Recipe, Category, Comment, Rating
from .forms import RecipeForm, CommentForm, RatingForm


def home(request):
    """Home page with list of all recipes."""
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ingredients__icontains=search_query)
        )
    
    # Filter by category
    category_slug = request.GET.get('category', '')
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
    }
    return render(request, 'recipes/list.html', context)


def recipe_detail(request, pk):
    """Recipe detail page."""
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.all()
    is_favorited = False
    
    if request.user.is_authenticated:
        is_favorited = recipe.favorited_by.filter(id=request.user.id).exists()
    
    # Forms for authenticated users
    comment_form = CommentForm() if request.user.is_authenticated else None
    rating_form = RatingForm() if request.user.is_authenticated else None
    
    # Check if user has already rated
    user_rating = None
    if request.user.is_authenticated:
        try:
            user_rating = Rating.objects.get(user=request.user, recipe=recipe)
        except Rating.DoesNotExist:
            pass
    
    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'user_rating': user_rating,
        'is_favorited': is_favorited,
        'average_rating': recipe.average_rating(),
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_create(request):
    """Create a new recipe."""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe created successfully!')
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/form.html', {'form': form, 'title': 'Create Recipe'})


@login_required
def recipe_update(request, pk):
    """Update an existing recipe (only by author)."""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Check if user is the author
    if recipe.author != request.user:
        messages.error(request, 'You can only edit your own recipes.')
        return redirect('recipes:detail', pk=pk)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/form.html', {'form': form, 'recipe': recipe, 'title': 'Update Recipe'})


@login_required
def recipe_delete(request, pk):
    """Delete a recipe (only by author)."""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Check if user is the author
    if recipe.author != request.user:
        messages.error(request, 'You can only delete your own recipes.')
        return redirect('recipes:detail', pk=pk)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('recipes:home')
    
    return render(request, 'recipes/delete_confirm.html', {'recipe': recipe})


@login_required
def recipe_favorite(request, pk):
    """Add or remove recipe from favorites."""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if recipe.favorited_by.filter(id=request.user.id).exists():
        recipe.favorited_by.remove(request.user)
        messages.info(request, 'Recipe removed from favorites.')
    else:
        recipe.favorited_by.add(request.user)
        messages.success(request, 'Recipe added to favorites!')
    
    return redirect('recipes:detail', pk=pk)


@login_required
def add_comment(request, pk):
    """Add a comment to a recipe."""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added!')
    
    return redirect('recipes:detail', pk=pk)


@login_required
def add_rating(request, pk):
    """Add or update a rating for a recipe."""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        # Check if user already rated
        rating, created = Rating.objects.get_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'score': request.POST.get('score')}
        )
        
        if not created:
            # Update existing rating
            rating.score = request.POST.get('score')
            rating.save()
            messages.info(request, 'Rating updated!')
        else:
            messages.success(request, 'Rating added!')
    
    return redirect('recipes:detail', pk=pk)


def category_list(request):
    """List all categories."""
    categories = Category.objects.all()
    return render(request, 'recipes/categories.html', {'categories': categories})





