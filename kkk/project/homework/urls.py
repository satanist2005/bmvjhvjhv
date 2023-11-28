from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('error', error, name='error'),
    # re_path(r'^user/<str:name>/<int:age>', user, name='user')
]