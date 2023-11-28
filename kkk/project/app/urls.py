from django.urls import path, re_path
from .views import index, user

urlpatterns = [

    path('', index, name='home'),
    re_path(r'^user/<str:name>/<int:age>', user, name='user')
]
