from django.urls import path
from pages.views import *

urlpatterns = [
        path('', auto_auth_page), 
        path('home/', home_page),
        path('signup/', signup_page),
        path('login/', login_page),
]
