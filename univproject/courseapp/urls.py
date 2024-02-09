## --------------------- [Example 3]--------------------------

# Import path function which is used to define URL patterns in Django
from django.urls import path

# Import views module (containing your view functions) from the current directory or package
from . import views

# Define list of URL patterns

urlpatterns = [ 
    path('', views.index, name='index'), # Map the root URL ('') to the index view function, naming it 'index'
    path('<int:course_id>/', views.course, name='course'), # Capture integer parameter from the URL and pass it to course function
]

#---------------------------------------------------------



