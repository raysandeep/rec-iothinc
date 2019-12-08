from django.shortcuts import render
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
from django.contrib.auth.models import User,auth
from rest_framework import filters
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Snippet



# Create your views here.
@csrf_exempt
def home(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.xdata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



class FilterList(generics.ListAPIView):
    serializer_class = SnippetSerializer

    def get_queryset(self):
        queryset = Snippet.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

