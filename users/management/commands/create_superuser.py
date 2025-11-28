from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser non-interactively'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Superuser email address'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Superuser password'
        )

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'User with email {email} already exists.')
            )
            return

        User.objects.create_superuser(
            email=email,
            password=password,
            first_name='Admin',
            last_name='User'
        )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created superuser: {email}')
        )
        self.stdout.write(
            self.style.WARNING(f'Password: {password} (Please change it after first login!)')
        )





