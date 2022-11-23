from django.urls import path

from . import views

app_name = 'Core_app'

urlpatterns = [
    path('',views.HomeTemplateView.as_view(), name='Home')
]