from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from .models import Recipe

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Recipe)
def log_recipe_creation(sender, instance, created, **kwargs):
    """Log when a new recipe is created."""
    if created:
        logger.info(f"New recipe created: {instance.title} by {instance.author.email}")





