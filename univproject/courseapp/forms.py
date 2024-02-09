
## ------------[Example 8: Web Form in Django]-----------------

from django.forms import ModelForm
from .models import Department, Course

class CourseForm(ModelForm):
    class Meta: # Provide metadata about the form
        model = Course # Associate the form with a model 'Course'
        fields = ['title', 'dept'] # Define the fields from model 'Course' that you want to include in your form
        
## -----------------------------------------------------------
