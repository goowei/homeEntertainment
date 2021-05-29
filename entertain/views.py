from django.shortcuts import render
'''
from django.http import HttpResponse
# Create your views here.
def main(request):
    return HttpResponse('<h1>This is main</h1>')
'''
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer