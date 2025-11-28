import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Profile

User = get_user_model()


@pytest.mark.django_db
def test_user_registration():
    """Test user registration with email."""
    user = User.objects.create_user(
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )
    assert user.email == 'test@example.com'
    assert user.check_password('testpass123')
    assert user.first_name == 'Test'


@pytest.mark.django_db
def test_user_login(client):
    """Test user login functionality."""
    user = User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )
    
    login_url = reverse('users:login')
    response = client.post(login_url, {
        'username': 'test@example.com',
        'password': 'testpass123'
    })
    
    assert response.status_code == 302  # Redirect after successful login


@pytest.mark.django_db
def test_profile_auto_creation():
    """Test that profile is automatically created when user is created."""
    user = User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )
    
    # Profile should be automatically created via signal
    assert hasattr(user, 'profile')
    assert Profile.objects.filter(user=user).exists()





