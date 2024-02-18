
from django.urls import path, include
from .views import GeminiView, GetResume
urlpatterns = [
    path('upload', GeminiView.as_view()),
    path('resume/', GetResume.as_view()),
]
