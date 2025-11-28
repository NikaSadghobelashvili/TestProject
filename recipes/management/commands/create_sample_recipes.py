from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from recipes.models import Recipe, Category
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates 10 sample recipes in the database'

    def handle(self, *args, **options):
        # Get or create categories
        categories_data = [
            {'name': 'Breakfast', 'slug': 'breakfast', 'description': 'Morning meals'},
            {'name': 'Lunch', 'slug': 'lunch', 'description': 'Midday meals'},
            {'name': 'Dinner', 'slug': 'dinner', 'description': 'Evening meals'},
            {'name': 'Desserts', 'slug': 'desserts', 'description': 'Sweet treats'},
            {'name': 'Snacks', 'slug': 'snacks', 'description': 'Quick bites'},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name'], 'description': cat_data['description']}
            )
            categories.append(category)
        
        # Get or create a sample user
        user, created = User.objects.get_or_create(
            email='sample@example.com',
            defaults={'first_name': 'Sample', 'last_name': 'Chef'}
        )
        if created:
            user.set_password('samplepass123')
            user.save()
        
        # Sample recipes data
        recipes_data = [
            {
                'title': 'Classic Pancakes',
                'description': 'Fluffy and delicious pancakes perfect for breakfast',
                'ingredients': '2 cups flour, 2 eggs, 1 cup milk, 2 tbsp sugar, 1 tsp baking powder',
                'instructions': 'Mix dry ingredients. Add wet ingredients. Cook on griddle until golden.',
                'cooking_time': 20,
                'difficulty_level': 'Easy',
            },
            {
                'title': 'Spaghetti Carbonara',
                'description': 'Creamy Italian pasta dish',
                'ingredients': 'Spaghetti, eggs, bacon, parmesan cheese, black pepper',
                'instructions': 'Cook pasta. Fry bacon. Mix eggs and cheese. Combine all ingredients.',
                'cooking_time': 30,
                'difficulty_level': 'Medium',
            },
            {
                'title': 'Grilled Salmon',
                'description': 'Healthy and flavorful grilled salmon',
                'ingredients': 'Salmon fillets, lemon, olive oil, herbs, salt, pepper',
                'instructions': 'Marinate salmon. Grill for 6-8 minutes per side. Serve with lemon.',
                'cooking_time': 25,
                'difficulty_level': 'Medium',
            },
            {
                'title': 'Chocolate Chip Cookies',
                'description': 'Classic homemade cookies',
                'ingredients': 'Flour, butter, sugar, eggs, chocolate chips, vanilla',
                'instructions': 'Cream butter and sugar. Add eggs and vanilla. Mix in flour and chips. Bake.',
                'cooking_time': 15,
                'difficulty_level': 'Easy',
            },
            {
                'title': 'Beef Stir Fry',
                'description': 'Quick and tasty stir fry',
                'ingredients': 'Beef strips, vegetables, soy sauce, garlic, ginger',
                'instructions': 'Marinate beef. Stir fry vegetables. Add beef and sauce. Cook until done.',
                'cooking_time': 20,
                'difficulty_level': 'Medium',
            },
            {
                'title': 'Caesar Salad',
                'description': 'Fresh and crisp salad',
                'ingredients': 'Romaine lettuce, croutons, parmesan, caesar dressing',
                'instructions': 'Wash and chop lettuce. Add croutons and cheese. Toss with dressing.',
                'cooking_time': 10,
                'difficulty_level': 'Easy',
            },
            {
                'title': 'Beef Wellington',
                'description': 'Elegant and sophisticated dish',
                'ingredients': 'Beef tenderloin, puff pastry, mushrooms, pate',
                'instructions': 'Sear beef. Prepare mushroom duxelles. Wrap in pastry. Bake until golden.',
                'cooking_time': 90,
                'difficulty_level': 'Hard',
            },
            {
                'title': 'Vegetable Curry',
                'description': 'Spicy and aromatic curry',
                'ingredients': 'Mixed vegetables, curry spices, coconut milk, onions',
                'instructions': 'Sauté onions. Add spices. Add vegetables and coconut milk. Simmer.',
                'cooking_time': 40,
                'difficulty_level': 'Medium',
            },
            {
                'title': 'French Toast',
                'description': 'Sweet breakfast favorite',
                'ingredients': 'Bread, eggs, milk, cinnamon, vanilla, butter',
                'instructions': 'Mix eggs, milk, and spices. Dip bread. Cook in butter until golden.',
                'cooking_time': 15,
                'difficulty_level': 'Easy',
            },
            {
                'title': 'Tiramisu',
                'description': 'Classic Italian dessert',
                'ingredients': 'Ladyfingers, mascarpone, coffee, cocoa, eggs, sugar',
                'instructions': 'Make coffee. Mix mascarpone with eggs and sugar. Layer with ladyfingers. Chill.',
                'cooking_time': 60,
                'difficulty_level': 'Hard',
            },
        ]
        
        # Create recipes
        created_count = 0
        for recipe_data in recipes_data:
            recipe, created = Recipe.objects.get_or_create(
                title=recipe_data['title'],
                defaults={
                    **recipe_data,
                    'author': user,
                    'category': random.choice(categories),
                }
            )
            if created:
                created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample recipes')
        )





