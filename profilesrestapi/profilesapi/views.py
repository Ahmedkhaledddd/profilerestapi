from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from . import serializers, permissions
# Create your views here.


class HelloAPIView(APIView):
  
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        
        an_api=['A','B','C']

        return Response({'message':'Hello','api_view':an_api})

    def post(self,request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)


    def put(self,request, pk=None):
        name = request.data
        serializer = self.serializer_class(data=name)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)


    def patch(self,request, pk=None):

       return Response({'Method':'patch'})

    def delete(self,request, pk=None):
    
       return Response({'Method':'delete'})



class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):

        a_viewset= ['aaaaa','bbbb','cccc']

        return Response({'message':a_viewset})

    def create(self, request):
        serializer= self.serializer_class(data= request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            return Response({' ':name})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve (self, request, pk= None):
        return Response({'Method': 'GET'})

    
    def update (self, request, pk= None):
        return Response({'Method': 'PUT'})
    
        
    def partial_update (self, request, pk= None):
        return Response({'Method': 'PATCH'})
    
    def destroy (self, request, pk= None):
        return Response({'Method': 'delete'})
        

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class= serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
