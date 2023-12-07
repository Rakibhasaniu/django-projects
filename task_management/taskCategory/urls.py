
from django.urls import path
from . import views
urlpatterns = [
    path('taskcategory/', views.add_category, name='add_category')
]
