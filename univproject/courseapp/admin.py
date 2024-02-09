from django.contrib import admin
from .models import Department, Course # Import the models

## Register your models here.
## Make these models accessible and manageable through the Django admin interface.
admin.site.register(Department)
admin.site.register(Course)


