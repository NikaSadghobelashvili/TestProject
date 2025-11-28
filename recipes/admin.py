from django.contrib import admin
from .models import Category, Recipe, Comment, Rating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'difficulty_level', 'cooking_time', 'created_at')
    list_filter = ('category', 'difficulty_level', 'created_at')
    search_fields = ('title', 'description', 'ingredients')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('favorited_by',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'recipe__title', 'author__email')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('recipe__title', 'user__email')





