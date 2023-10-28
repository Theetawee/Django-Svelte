from django.shortcuts import render
from .serializers import TestSerializer
from rest_framework import generics
from .models import TestModel
# Create your views here.


class ListAccountsApi(generics.ListAPIView):
    queryset=TestModel.objects.all()
    serializer_class=TestSerializer


