from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getItem(request, id):
    item = get_object_or_404(Item, pk = id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request, id):
    item = get_object_or_404(Item, pk = id)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
# @api_view(['PUT'])
# def updateItem(request, id):
#     item = get_object_or_404(Item, pk=id)
#     serializer = ItemSerializer(item, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
def deleteItem(request, id):
    item = get_object_or_404(Item, pk = id)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)