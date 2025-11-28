from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Category(models.Model):
    """Recipe category model."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe model."""
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text='List ingredients, one per line or separated by commas')
    instructions = models.TextField(help_text='Step-by-step cooking instructions')
    cooking_time = models.PositiveIntegerField(help_text='Cooking time in minutes', validators=[MinValueValidator(1)])
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Medium')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    favorited_by = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def average_rating(self):
        """Calculate average rating for the recipe."""
        ratings = self.ratings.all()
        if ratings.exists():
            return round(ratings.aggregate(models.Avg('score'))['score__avg'], 2)
        return 0


class Comment(models.Model):
    """Comment model for recipes."""
    content = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author.email} on {self.recipe.title}"


class Rating(models.Model):
    """Rating model for recipes."""
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rating from 1 to 5'
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'recipe']  # One rating per user per recipe
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} rated {self.recipe.title} - {self.score}/5"





