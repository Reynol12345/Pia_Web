from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente con credenciales predefinidas'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'admin@example.com'
        password = 'Admin123!'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'El superusuario "{username}" ya existe.'))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario creado exitosamente!'))
            self.stdout.write(f'  Username: {username}')
            self.stdout.write(f'  Email: {email}')
            self.stdout.write(f'  Password: {password}')
