## ----------------------[Example 1]--------------------------

# Import HttpResponse from Django's http module to generate HTTP response
#from django.http import HttpResponse

# Create your views here.

# Function returns HTTP response displaying the text between the ""
#def index(request): 
#   return HttpResponse("Courses Index Page")
   

#-------------------------------------------------------------


## ----------------------[Example 2]--------------------------


#from django.shortcuts import render # Redirect a user's browser to a different URL

#from .models import Course # Import your Course model


#def index(request):
#    courses = Course.objects.all() #Retrieves all courses from database
#    context = {'courses': courses}
#    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context

#-------------------------------------------------------------


## ----------------------[Example 3]--------------------------

#from django.shortcuts import render
#from .models import Course #Import your Course model

#def index(request):
#    courses = Course.objects.all() #Retrieves all courses from database
#    context = {'courses': courses}
#    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context

#def course(request, course_id):
#    course = Course.objects.get(id=course_id)
#    context = {'course': course}
#    return render(request, 'courseapp/course.html', context)
   
   
#-------------------------------------------------------------


## -------------------[Example 4: Object Not Found 404 Error]--------------

#from django.shortcuts import render, get_object_or_404 # Retrieve an object from the database or raising a 404 Not Found error if the object 'course' does not exist
#from .models import Course, Department # Import your Course and Department models


#def index(request):
#    courses = Course.objects.all() #Retrieves all courses from database
#    context = {'courses': courses}
#    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context


#def course(request, course_id):
#     Retrieve the Course object with the given course_id or raise a 404 error if not found
#    course = get_object_or_404(Course, pk=course_id)
#    context = {'course': course} # Place the retrieved course in the context dictionary
#    return render(request, 'courseapp/course.html', context) # Render the 'course.html' template with the context data

#------------------------------------------------------------------------


## ------------------[Example 5: Try-Except Block and Redirect]--------------------

#from django.shortcuts import render, redirect # Redirect a user browser to different URL
#from .models import Course, Department #Import your Course and Department models

# Create your views here.

#def index(request):
#    courses = Course.objects.all() #Retrieves all courses from database
#    context = {'courses': courses}
#    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context

#def course(request, course_id):
#    try:
#        course = Course.objects.get(id=course_id)
#    except Course.DoesNotExist:
#        return redirect('index')
#    context = {'course': course}
#    return render(request, 'courseapp/course.html', context)



## ------------------[Example 6: Error Message]---------------

#from django.shortcuts import render, redirect 
#from django.contrib import messages # Import messages
#from .models import Department, Course #Import your Course and Department models


#def index(request):
#    courses = Course.objects.all()
    # Prepares a context containing the retrieved courses and any messages stored in the request using messages.get_messages(request).
#    context = {'courses': courses,
#               'messages': messages.get_messages(request)} 
#    return render(request, 'courseapp/index.html', context)


#def course(request, course_id):
#    try:
#        course = Course.objects.get(id=course_id)
#    except Course.DoesNotExist:
#        messages.add_message(request, messages.INFO, 'illegal course id.')
#        return redirect('index') # Redirect to 'index' or another page 
#    context = {'course': course} # Place the retrieved course in the context dictionary
#    return render(request, 'courseapp/course.html', context) # Render the 'course.html' template with the context data    

#-------------------------------------------------------------



## ---------------[Example 7: Web Form and HTTP POST]---------

#from django.shortcuts import render, redirect 
#from .models import Department, Course #Import your Course and Department models


#def index(request):
#    courses = Course.objects.all() #Retrieves all courses from database
#    context = {'courses': courses}
#    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context


#def course(request, course_id):
#    try:
#        course = Course.objects.get(id=course_id) #Retrieve a specific course by 'id' from database
#    except Course.DoesNotExist: 
#        return redirect('index') #If course doesn't exist, redirect to 'index' view
#    if request.method == 'POST':
#        new_title=request.POST.get('title') #Retrieve data from POST request by 'title'
#        new_dept=Department.objects.get(id=request.POST.get('dept')) #Retrieve data from POST request by 'dept'
#        new_course = Course.objects.create(title=new_title, dept=new_dept) #Create a new Course object using the received 'title' and 'dept'
#        return redirect('course', new_course.id) #Redirect to 'course' view for the newly created course and display its details
#    context = {'course': course, 'depts': Department.objects.all()}
#    return render(request, 'courseapp/course.html', context) #Render 'course.html' template with course details and a list of all departments 

#-------------------------------------------------------------


## -----------[Example 8: Web Form in Django]-----------------

from django.shortcuts import render, redirect
from .models import Department, Course
from .forms import CourseForm


def index(request):
    courses = Course.objects.all() #Retrieves all courses from database
    context = {'courses': courses}
    return render(request, 'courseapp/index.html', context) #Pass the retrieved courses to 'index.html' template as context


def course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        form = CourseForm(instance=course)
    except Course.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        form = CourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save()
            return redirect('course', new_course.id)
    context = {'course': course, 'form': form}
    return render(request, 'courseapp/course.html', context)

#-------------------------------------------------------------







