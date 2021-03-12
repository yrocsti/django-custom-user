# django-custom-user
_**Django custom user with email and username authentication**_

Feel free to change, break and learn to create your own custom user .

All the contained code can be found in the django code base.
[GitHub](http://github.com/django/django)

![Image of code download](https://github.com/yrocsti/django-custom-user/blob/main/images/github_code_img.png)

Once downloaded into your django directory where your manage.py file is located. Be sure to save each file after making changes.
Make sure to add accounts to your installed apps in your project settings folder.

With a custom user remember to use:
```
from django.contrib.auth import get_user_model

User = get_user_model()
```
Or
```
from django.conf import settings

whatever_variable = settings.AUTH_USER_MODEL
```

*<your_project>/settings.py*
```
INSTALLED_APPS = [
    # Our apps
    'accounts.apps.AccountsConfig',

    # built in django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Then change your TEMPLATES list as follows:
*<your_project>/settings.py*
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
The last thing to add to the bottom of your project settings:
*<your_project>/settings.py*
```
# Declare our own user model
AUTH_USER_MODEL = 'accounts.User'

# First django will try to authenticate against built in ModelBackend, if that fails it will try EmailAuthBackend to authenticate.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
]

# have email sent to the console for testing purposes only. Change this to your mail server for production.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Upon successful sign in, logout or clicking login link constant variables below will handle redirect to named urls
LOGIN_REDIRECT_URL = 'accounts:dashboard'  # Redirected to after successful login
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
```
_Now onto the project urls_
*<your_project>/urls.py*
```
from django.contrib import admin
from django.urls import path, include  # Make sure to import include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
```

*<your_main_project_directory>/templates*
This is where you can define a base html page and navbar to build your templates.


### Accounts directory
First lets create our own custom user model.
If you look through the code for django you will notice this model is based on the exact same code django’s default user uses.

*accounts/models.py*
Change this file to fit your specific needs for your user.
_Change this file before making migrations_
[GitHub](http://https://github.com/django/django/blob/master/django/contrib/auth/models.py)

*accounts/managers.py*
Manager is also based on djangos implementation of a manager.
[GitHub](http://https://github.com/django/django/blob/master/django/contrib/auth/models.py)

*accounts/views.py*
Register view is a basic sign up view. The dashboard view is just a simple logged in home page to redirect to after a successful login. Feel free to change these files to fit your specific needs. The rest of the views are built in to django.
[GitHub](https://github.com/django/django/blob/master/django/contrib/auth/views.py)

These views are found through djangos url path search => <your_project>.urls.py => accounts.urls.py
```
from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
```
*accounts/authentication.py*
If you want to authenticate using both username and email make sure to keep this file and the AUTHENTICATION_BACKENDS list as is. If you prefer just username you can delete the AUTHENTICATION_BACKENDS from <your_project>.settings.py file.

*accounts/forms.py*
The CustomUserCreationForm and CustomUserChangeForm are for use in the admin and the UserRegistrationForm is for users to sign up to your site.

*accounts/admin.py*
Here we tell admin what forms to use and how we want to view the models.

*accounts/templates*
	*accounts*
		This is where we keep our apps namespaced templates.
	*registration*
		This needs to be called registration so the built in django views know where to find the 			templates.

Email verification is here!!!
