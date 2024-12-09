# from django.contrib import admin
# from django.urls import path
# from .views import index

# urlpatterns=[
# 	path('', index)
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
