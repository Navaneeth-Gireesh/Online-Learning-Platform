# Import compatibility features for Python 2
from __future__ import absolute_import, unicode_literals

# Import the os module for interacting with the operating system
import os

# Import the Celery class from the Celery library
from celery import Celery

# Set the default Django settings module in the environment
# This tells Django which settings to use for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_learning_platform.settings')

# Create an instance of the Celery class named 'app'
app = Celery('online_learning_platform')

# Configure the Celery application using Django project settings
# The namespace argument specifies the namespace for Celery-related settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover and register task modules from all installed apps
app.autodiscover_tasks()

# Define a Celery task decorated with @app.task
# The bind=True argument allows the task to access information about itself
@app.task(bind=True)
def debug_task(self):
    # Print information about the task request
    print('Request: {0!r}'.format(self.request))