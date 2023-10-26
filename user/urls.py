# imports
from django.urls import path
from user.views import user_profile_view

# urls
urlpatterns = [
    path('profile/', user_profile_view),
]