from django.core.management.base import BaseCommand
from recipes.models import Category


class Command(BaseCommand):
    help = 'Creates default recipe categories'

    def handle(self, *args, **options):
        categories_data = [
            {'name': 'Breakfast', 'slug': 'breakfast', 'description': 'Morning meals and breakfast recipes'},
            {'name': 'Lunch', 'slug': 'lunch', 'description': 'Midday meals and lunch recipes'},
            {'name': 'Dinner', 'slug': 'dinner', 'description': 'Evening meals and dinner recipes'},
            {'name': 'Desserts', 'slug': 'desserts', 'description': 'Sweet treats and dessert recipes'},
            {'name': 'Snacks', 'slug': 'snacks', 'description': 'Quick bites and snack recipes'},
            {'name': 'Appetizers', 'slug': 'appetizers', 'description': 'Starters and appetizer recipes'},
            {'name': 'Salads', 'slug': 'salads', 'description': 'Fresh and healthy salad recipes'},
            {'name': 'Soups', 'slug': 'soups', 'description': 'Warm and comforting soup recipes'},
            {'name': 'Beverages', 'slug': 'beverages', 'description': 'Drinks and beverage recipes'},
            {'name': 'Vegetarian', 'slug': 'vegetarian', 'description': 'Vegetarian-friendly recipes'},
        ]
        
        created_count = 0
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new categories. Total categories: {Category.objects.count()}')
        )





