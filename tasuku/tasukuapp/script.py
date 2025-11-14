import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # Replace 'mysite' with your project name
import django
django.setup()

# Now you can safely import/use models, views, etc.
from .models import TaskStatus  