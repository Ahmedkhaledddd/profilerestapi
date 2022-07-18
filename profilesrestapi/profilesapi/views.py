from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloAPIView(APIView):
  

    def get(self, request, format=None):
        
        an_api=['A','B','C']

        return Response({'message':'Hello','api_view':an_api})