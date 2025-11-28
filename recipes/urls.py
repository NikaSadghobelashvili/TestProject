from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:pk>/', views.recipe_detail, name='detail'),
    path('recipes/create/', views.recipe_create, name='create'),
    path('recipes/<int:pk>/update/', views.recipe_update, name='update'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='delete'),
    path('recipes/<int:pk>/favorite/', views.recipe_favorite, name='favorite'),
    path('recipes/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('recipes/<int:pk>/rate/', views.add_rating, name='add_rating'),
    path('categories/', views.category_list, name='categories'),
]





