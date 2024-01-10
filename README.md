# Email-Verifier-
This is a web-based email verifier to check if an email is valid. 

Start by creating a virtual environment for the project; use this command: python -m venv project.
To activate the virtual environment, use; .\project\Scripts\activate(windows) 
                                          source project/bin/activate(Kali Linux)
Install the project dependencies by running the following coman:pip install Django email-validator_
Create the Django main project by running the following command; django-admin startproject webbased_emailverifier

Run the following commands on the terminal or cmd;
                                              cd webbased_emailverifier
                                              python manage.py startapp verifier
                                              python manage.py runserver
