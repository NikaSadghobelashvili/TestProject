import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Recipe, Category, Comment, Rating

User = get_user_model()


@pytest.mark.django_db
def test_recipe_creation():
    """Test recipe creation."""
    user = User.objects.create_user(
        email='chef@example.com',
        password='testpass123'
    )
    category = Category.objects.create(
        name='Desserts',
        slug='desserts'
    )
    
    recipe = Recipe.objects.create(
        title='Chocolate Cake',
        description='Delicious chocolate cake',
        ingredients='Flour, Sugar, Cocoa',
        instructions='Mix and bake',
        cooking_time=60,
        difficulty_level='Medium',
        author=user,
        category=category
    )
    
    assert recipe.title == 'Chocolate Cake'
    assert recipe.author == user
    assert recipe.category == category
    assert str(recipe) == 'Chocolate Cake'





