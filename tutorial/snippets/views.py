# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    list all obj or create new one
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print 'request with post %s' % request
        print 'type of request obj = %s' % type(request)
        data = JSONParser().parse(request)
        print 'jsonparser().parse(request) = %s' % data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_details(request, pk):
    """
    retrieve, update or delete obj
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        print 'put request after parsing = %s' % data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            return JSONParser(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse(status=204)