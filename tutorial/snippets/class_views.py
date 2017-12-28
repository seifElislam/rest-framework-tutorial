"""

"""
from .models import Snippet
from .serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    list all obj or create new
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetails(APIView):
    """
    retrieve, update or delete obj
    """
    def get_obj(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_obj(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_obj(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_obj(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)