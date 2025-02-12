from django.contrib import admin
from django.urls import path

from cv.views import cv_view, submit_form

app_name='cv'

urlpatterns = [
    path('mycv/', cv_view, name='cv'),  
    path('', cv_view, name='cv_root'),
    path( 'contactme/', submit_form, name='contactme')
]
