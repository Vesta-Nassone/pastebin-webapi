from django.http import Http404, JsonResponse
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        