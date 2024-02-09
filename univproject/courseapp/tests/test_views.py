# Test Django view associated with the Course model. This test cover various scenarios including template usage, context data, redirects, and POST requests. 

from django.test import TestCase
from courseapp.models import Department, Course

class CourseViewTest(TestCase):
    def test_use_course_template(self):
        # Create a department
        cs = Department.objects.create(name='cs')
        # Create a course for the created department
        c1 = Course.objects.create(title='c1', dept=cs) 
        # Send GET request to the URL associated with the courseapp
        response = self.client.get(f'/courseapp/{c1.id}/')
        # Assert that the response uses the 'course.html' template
        self.assertTemplateUsed(response, 'courseapp/course.html') 

    def test_context_has_the_course(self):
        cs = Department.objects.create(name='cs')
        c1 = Course.objects.create(title='c1', dept=cs)
        response = self.client.get(f'/courseapp/{c1.id}/')
        self.assertEqual(response.context['course'], c1) # Assert that the course object is present in the response context and is equal to the created course

    def test_redirect_when_course_does_not_exist(self):
        response = self.client.get('/courseapp/99/') # Send GET request to a non-existent course URL (/courseapp/99/)
        self.assertRedirects(response, '/courseapp/') # Assert that the response is a redirect to the '/courseapp/' URL

    def test_POST_save_new_course(self):
        cs = Department.objects.create(name='cs')
        c1 = Course.objects.create(title='existing course', dept=cs)
        # Send POST request to the URL associated with the existing course (/courseapp/{c1.id}/) to create a new course
        self.client.post(
            f'/courseapp/{c1.id}/',
            data={'title': 'new course', 'dept': cs.id})
        self.assertEqual(Course.objects.count(), 2) # Assert that the total count of Course objects is 2
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
##### Another Way ######
# It's a good practice to use the reverse function to generate URLs based on view names rather than hardcoding them. This helps in maintaining consistency and avoids issues if URLs change in the future.   
# Generate URLs based on the view names or URL patterns to ensure that your tests will still work even if the URLs associated with your views change in the future   
#from django.urls import reverse
#from django.test import TestCase
#from courses.models import Department, Course

#class CourseViewTest(TestCase):
#    def test_use_course_template(self):
#        cs = Department.objects.create(name='cs')
#        c1 = Course.objects.create(title='c1', dept=cs)
#        url = reverse('course', args=[c1.id])
#        response = self.client.get(url)
#        self.assertTemplateUsed(response, 'courseapp/course.html')

#    def test_context_has_the_course(self):
#        cs = Department.objects.create(name='cs')
#        c1 = Course.objects.create(title='c1', dept=cs)
#        url = reverse('course', args=[c1.id])
#        response = self.client.get(url)
#        self.assertEqual(response.context['course'], c1)

#    def test_redirect_when_course_does_not_exist(self):
#        url = reverse('course', args=[99])
#        response = self.client.get(url)
#        self.assertRedirects(response, reverse('index'))

#    def test_POST_save_new_course(self):
#        cs = Department.objects.create(name='cs')
#        c1 = Course.objects.create(title='existing course', dept=cs)
#        url = reverse('course', args=[c1.id])
#        response = self.client.post(url, data={'title': 'new course', 'dept': cs.id})
#        self.assertEqual(Course.objects.count(), 2)

      