from django.urls import path
from .views import *

urlpatterns = [
    path("",userapi.as_view()),
    path("bookapi/",bookapi.as_view()),
    path("issuebook/",issuebook.as_view()),
]
