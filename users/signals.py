from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile automatically when a new user is created."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """Send welcome email when a new user registers."""
    if created:
        subject = 'Welcome to Recipe Sharing Platform!'
        message = f"""
        Hello {instance.first_name or instance.email},
        
        Welcome to our Recipe Sharing Platform! We're excited to have you join our community.
        
        Start sharing your favorite recipes and discover amazing dishes from other chefs!
        
        Happy cooking!
        The Recipe Sharing Team
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@recipes.com',
            [instance.email],
            fail_silently=False,
        )





