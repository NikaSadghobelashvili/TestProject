from django import forms
from .models import Recipe, Comment, Rating, Category


class RecipeForm(forms.ModelForm):
    """Form for creating and updating recipes."""
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 
                  'cooking_time', 'difficulty_level', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'List ingredients...'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Step-by-step instructions...'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes'}),
            'difficulty_level': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add empty option and populate categories
        self.fields['category'].required = False
        self.fields['category'].empty_label = 'Select a category (optional)'
        self.fields['category'].queryset = Category.objects.all().order_by('name')


class CommentForm(forms.ModelForm):
    """Form for adding comments to recipes."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment...'
            })
        }


class RatingForm(forms.ModelForm):
    """Form for rating recipes."""
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rating (1-5)'
            })
        }

