from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import OhmySerializer
from .models import Ohmy
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def register_user(request):
    serializer=OhmySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" :"user added successfully" , "user":serializer.data} ,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request,id):
    if str(request.user.id) != str(id):
        return Response({"error" :"You are not the main user"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        user=Ohmy.objects.get(id=id)
        serializer=OhmySerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Ohmy.DoesNotExist :
        return Response({"error":"user not found man"},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request,id):
    if str(request.user.id) != str(id):
        return Response({"error" :"You are not the main user"},status=status.HTTP_403_FORBIDDEN)
    try:
        user=Ohmy.objects.get(id=id)
        if user.is_superuser :
            return Response({"error":"Cannot delete a super user"},status=status.HTTP_403_FORBIDDEN)
        user.delete()
        return Response({"DoneMessage" : "Done successfully"},status=status.HTTP_200_OK)

    except Ohmy.DoesNotExist :
        return Response({"error":"user not found man"},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request,id):
    if str(request.user.id) != str(id):
        return Response({"error" :"You are not the main user"},status=status.HTTP_403_FORBIDDEN)
    try:
        user=Ohmy.objects.get(id=id)
        if user.is_superuser == True:
            return Response({"error":"Cannot update a super user"},status=status.HTTP_403_FORBIDDEN)
        serializer=OhmySerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Ohmy.DoesNotExist :
        return Response({"error":"user not found man"},status=status.HTTP_404_NOT_FOUND)
