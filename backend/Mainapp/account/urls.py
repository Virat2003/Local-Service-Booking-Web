from django.urls import path
from .views import RegisterView
from .views import ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path("profile/", ProfileView.as_view(), name="profile"),
]
