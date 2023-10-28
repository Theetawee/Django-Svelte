from django.urls import path
from .views import ListAccountsApi


urlpatterns=[
    path('',ListAccountsApi.as_view())
]