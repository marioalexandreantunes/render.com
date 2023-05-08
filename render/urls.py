from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', admin.site.urls), # ADD --MA-- gosto de mudar url da parte de administração
    path('', include('werbapp.urls')) # ADD --MA-- iremos trabalhar noutro ficheiro todas as nossas urls
]