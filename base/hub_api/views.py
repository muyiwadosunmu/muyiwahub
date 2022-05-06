from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from base.hub_api.serializers import RoomSerializer 
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
def getRoutes(request):
    routes =[
        'GET /api',
        'GET /api/roooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
    
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) #many=True because we're serializing a queryset
    return Response(serializer.data) #we could have passed in only *serializer* as argument butwe do not need the object attributes but rather the data attributes

@api_view(['GET'])
def getRoom(request,pk): #get a single room
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) #many=True because we're serializing a queryset
    return Response(serializer.data)

