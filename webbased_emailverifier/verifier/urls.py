# from the current folder import views
from verifier.views import index
# importing path from django.urls
from django.urls import path

# this is the list of the app's views
# if the app has several views then it will have several paths
urlpatterns = [
    path('', index, name='home'),
]
#In the file, we are importing the index() view from views.py file.
# After the imports, we create a list called urlpatterns list, which will contain a URL path, and if the application has several views, then the urlpatterns will contain several URL paths.
#If you notice, the path() function takes three arguments, the actual path as an empty string, the view, and the view’s name.

