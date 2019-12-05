from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def home(request):
    permission_classes = (IsAuthenticated, )
    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("serializer.data", status=201,safe=False)
        return JsonResponse(serializer.errors, status=400,safe=False)
