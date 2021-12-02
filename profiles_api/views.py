from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# vagrant up
# vagrant ssh
# cd ./vagrant
# source ~/env/bin/activate
# python manage.py runserver 0.0.0.0:8000

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'baga',
            'pijas',
            'fei'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        #pk is primary key to find the object to update
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'Method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Pijas',
            'AutoPijas',
            'PEEEEJAS'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset}) #GET MULTIPLE OBJECTS FROM DB

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Hello {name}!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #CREATE SINGLE OBJECT IN DB

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'}) #GET SINGLE OBJECT FROM DB

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'}) #COMPLETELY UPDATE OBJECT IN DB

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'}) #PARTIALLY UPDATE OBJECT IN DB

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'}) #DELETE OBJECT IN DB

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer #Just by adding the UserProfileSerializer (which has UserProfile as the set model), ModelViewSet knows what objects to deal with (in this case Users objects)
    queryset = models.UserProfile.objects.all() #APPLYING ON ALL USERS IN DATABASE
    authentication_classes = (TokenAuthentication,) #PUT THE COMMA SO IT CREATES A TUPPLE
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
