from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer


def snippet_list(request):
    