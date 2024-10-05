from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("examples", views.examples, name="examples"),
    path("docs", views.docs, name="docs"),
]
