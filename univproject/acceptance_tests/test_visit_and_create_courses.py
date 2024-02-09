# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from courseapp.models import Department, Course
# import time

# class VisitAndCreateTest(StaticLiveServerTestCase):
    
    # def test_visit_and_create(self):
        # # Create Department (cs) and a Course (se) in Django DB
        # cs = Department.objects.create(name='cs')
        # se = Course.objects.create(title='se', dept=cs)
        
        ## Initialize Firefox WebDriver
        # browser = webdriver.Firefox() 
        
        ## Browser navigates to a specific URL for the created course
        # browser.get(f'{self.live_server_url}/courseapp/{se.id}')
        
        ## Find input element with 'id_title' and assure that its initial value is 'se'.
        # inputbox = browser.find_element_by_id('id_title')
        # self.assertEqual(inputbox.get_attribute('value'), 'se')
        
        ## Simulate user inputs by deleting the existing text in the input box 'se' twice and entering 'db'.
        # inputbox.send_keys(Keys.BACKSPACE)
        # inputbox.send_keys(Keys.BACKSPACE)
        # inputbox.send_keys('db')
        
        ## After pressing the ENTER key, the test waits for 2 seconds to allow the application to process the request
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(2) # Static wait
        
        ## The test verifies that the value in the 'id_title' input box has been updated to 'db'.
        # inputbox = browser.find_element_by_id('id_title')
        # self.assertEqual(inputbox.get_attribute('value'), 'db')
                
        ## The browseris closed
        # browser.quit()
        
        
        
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from courses.models import Department, Course
import time

class VisitAndCreateTest(StaticLiveServerTestCase):
    
    # Set up the test environment before running the test by creatinga new instance of the Firefox WebDriver before each test
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    # Clean up the test environment after running the test by closing Firefox WebDriver after each test
    def tearDown(self):
        self.browser.quit()
    
    def test_visit_and_create(self):
        # Create Department (cs) and a Course (se) in Django DB
        cs = Department.objects.create(name='cs')
        se = Course.objects.create(title='se', dept=cs)   
        
        # Browser navigates to a specific URL for the created course
        self.browser.get(f'{self.live_server_url}/courseapp/{se.id}')
        
        # Find input element with 'id_title' and assure that its initial value is 'se'.
        inputbox = self.browser.find_element_by_id('id_title')
        self.assertEqual(inputbox.get_attribute('value'), 'se')
        
        # Simulate user inputs by deleting the existing text in the input box 'se' twice and entering 'db'.
        inputbox.send_keys(Keys.BACKSPACE)
        inputbox.send_keys(Keys.BACKSPACE)
        inputbox.send_keys('db')
        
        # After pressing the ENTER key, the test waits for 2 seconds to allow the application to process the request
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly.time.sleep(2) # Dynamic wait
        
        # The test verifies that the value in the 'id_title' input box has been updated to 'db'.
        inputbox = self.browser.find_element_by_id('id_title')
        self.assertEqual(inputbox.get_attribute('value'), 'db')
                
        ## The browser is closed automatically when the test method completes due to the tearDown method being called.
        
        
        