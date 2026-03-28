from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book, name="book"),
    path("book/thanks/", views.book_thanks, name="book_thanks"),
]