
from django.urls import include, path

from . import views

app_name='job'

urlpatterns = [
    path('signup',views.signup , name='signup'),

]