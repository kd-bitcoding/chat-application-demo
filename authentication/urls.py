# imports
from django.urls import path
from authentication.views import user_login_view, user_registration_view

# urls
urlpatterns = [
    path('login/', user_login_view),
    path('register/', user_registration_view),
]