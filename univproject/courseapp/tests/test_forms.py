from django.test import TestCase
from courseapp.models import Department
from courseapp.forms import CourseForm

class CourseFormTest(TestCase):
    def test_course_form(self):
        cs = Department.objects.create(name='CS') 

        # Create CourseForm instance with data
        course_form = CourseForm(data={'title': 'DB', 'dept': cs.id}) 
        
        #self.fail(course_form.as_p()) # Output the HTML representation of the form as a failure message. Here, the test will intentionally fail, and the failure message will be the HTML representation of the form (course_form.as_p()).
      
        
        ## Alternatively: you can use assertion methods like assertEqual, assertTrue, or assertFalse to check specific conditions about the form fields
        
        ## Check that there are no errors in the form
        self.assertEqual(course_form.errors, {})
        
        ## Check if the form is valid based on the provided data
        self.assertTrue(course_form.is_valid())     
        
        ## Check whether the validated data for the 'title' field in the form is equal to the string 'DB'
        self.assertEqual(course_form.cleaned_data['title'], 'DB')
        
        ## Check whether the validated data for the 'dept' field in the form is equal to the string department object 'cs'
        self.assertEqual(course_form.cleaned_data['dept'], cs)
        