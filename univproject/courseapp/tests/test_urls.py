from django.test import TestCase
from django.urls import resolve
from courseapp.views import index

# This test ensures that when the URL "/courseapp/" is accessed, it correctly resolves to the index view function. If the actual view function doesn't match the expected one, the test will report a failure.

class CourseUrlTest(TestCase):
    def test_courses_url_resolve_to_course_index_page(self):
        view = resolve('/courseapp/') # Find the view function associated with a given URL
        
        self.assertEqual(view.func, index) # Assert that the resolved view function for the URL /courseapp/ is equal to the index view function.