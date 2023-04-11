from django.shortcuts import render
# this displays flash messages or notifications
from django.contrib import messages
# importing validate_email and EmailNotValidError
from email_validator import validate_email, EmailNotValidError

# Create your views here.
def index(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting the email from the form input
        email = request.POST.get('email-address')
        # this is the context
        context = {
                'email': email
            }
        # the try statement for verify/validating the email
        try:
            # validating the actual email address using the validate_email function
            email_object = validate_email(email)
            # creating the message and storing it
            messages.success(request, f'{email} is a valid email address!!')
            # rendering the results to the index page
            return render(request, 'verifier/index.html', context)
        # the except statement will capture EmailNotValidError error 
        except EmailNotValidError as e:
            # creating the message and storing it
            messages.warning(request, f'{e}')
            # rendering the error to the index page
            return render(request, 'verifier/index.html', context)
    # this will render when there is no request POST or after every POST request  
    return render(request, 'verifier/index.html')

#In the code snippet, we are importing the render() function, as usual, we are also importing the built-in Django messages from django.contrib, this is for displaying flash messages or notifications, and finally, we are importing validate_email and EmailNotValidError from email_validator. According to email-validator’s documentation, it states that the library validates that a string is of the form name@example.com.

#In the index() function, we are checking if the request sent is POST. If so, then we are retrieving the email from the form data using the request.POST.get(‘email-address’), the email-address is the name given to the email input in the form.

#After putting the email in the context, we have a try/except block, in the try statement, we are validating the email address using the validate_email() function, after successful validation, we create a success message and call the render() function. In the except block, we are just catching the EmailNotValidError, we are also creating a message, but this time it is of type warning, and we are calling the render() function again.
#In the code snippet, we are importing HttpResponse() function from django.http, 
# this function is just for echoing responses in the browser to the user. 
# You will get to know more about the render() function later in the article.