
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('add/', views.add_category, name='add_category')
# ]


from django.urls import path , include
from . import views
urlpatterns = [
    
    path('add/',views.add_category, name='add_category')
]