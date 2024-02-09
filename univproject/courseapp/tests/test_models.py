## This test check whether the model Course raises Validation Error when an attempt is made to create a duplicate title within the same department

# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from courseapp.models import Department, Course

# class CourseModelTest(TestCase):
    # def test_duplicate_titles_invalid(self):
        # cs = Department.objects.create() # Create a new Department instance
        
        # Course.objects.create(dept=cs, title='twice') # Create a Course instance with the title 'twice' in the 'cs' department created
        
        # same_course = Course(dept=cs, title='twice') # Create another Course instance with the same title 'twice' in the same department
        
        ## A code to raise validation error indicating uniqueness constraint violation
        # with self.assertRaises(ValidationError):
            # same_course.validate_unique() # Call the Django built-in 'validate_unique' method on the same_course instance to check uniqueness constraints or you can you same_course.full_clean() to call all validation on the model including validate unique.
           
##-------------------------------------------------------------------          
## This test check whether the model Course raises Integrity Error when an attempt to save a Course with duplicate title in the same department 

from django.test import TestCase
from django.db.utils import IntegrityError
from courseapp.models import Department, Course

class CourseModelTest(TestCase):
       def test_duplicate_titles_invalid(self):
        ## Create a new Department instance
           cs = Department.objects.create() 
        
        ## Create a Course instance with the title 'twice' in the 'cs' department created
           Course.objects.create(dept=cs, title='twice') 
        
        ## Create another Course instance with the same title 'twice' in the same department
           same_course = Course(dept=cs, title='twice')
        
        ## A code to raise integrity error indicating saving a Course instance with a duplicate title in the same department
           with self.assertRaises(IntegrityError):  
                same_course.save() # Attempts to save the same_course instance to the database. If there's a uniqueness constraint violation, Django will raise an integrity error
            