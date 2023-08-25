from django.contrib import admin
from django.urls import path
from home.views import helloview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',helloview),
]















