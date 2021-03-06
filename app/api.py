from django.shortcuts import render, redirect
# from django.contrib import messages
from django.conf import settings
# from django.core.files.storage import FileSystemStorage

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

import os

@api_view(['GET'])
def routes(request):
    context = {
        'teste': 'teste'
    }

    return Response(context)

@api_view(['GET'])
def get_lojas(request):
    lojas = Loja.objects.all()
    serializer = LojaSerializer(instance=lojas, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(instance=items, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_items_loja(request, pk):
    loja = Loja.objects.get(id=pk)
    loja_serializer = LojaSerializer(instance=loja, many=False)
    
    items_loja = Loja_Item.objects.filter(loja=loja)
    items_loja_serializer = Loja_ItemSerializer(instance=items_loja, many=True)

    list_items_loja = []
    for item in items_loja_serializer.data:
        temp_item = Item.objects.get(id=item['item'])
        temp_item_serializer = ItemSerializer(instance=temp_item, many=False)
        dict = {
            'nome' : temp_item_serializer.data['nome'],
            'image' : temp_item_serializer.data['image'],
            'preco': item['preco']
        }
        list_items_loja.append(dict)

    context = {
        'loja' : loja_serializer.data,
        'items' : list_items_loja
    }
    return Response(context)