from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import Note

# Create your views here.


@api_view([''])
def getRoutes(request):
    routes= [

    ]

    return Response('API response')

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = serializer
    return Response('NOTES')
