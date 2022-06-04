from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('index', views.index, name="index"),
    path('add/', views.create, name="create"),
    path('update/<str:name>', views.update, name="update"),
    path('delete/<str:name>', views.delete, name="delete")
]
