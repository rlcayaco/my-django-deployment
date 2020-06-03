from django.urls import path
from basic_app import views

# TEMPLATE TAGGING, when using template tagging set a variable name called app_name equals to your app name
# Django will look for this app_name variable
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
