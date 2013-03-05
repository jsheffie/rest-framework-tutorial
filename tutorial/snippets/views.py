from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
    """ List all code snippets, or create a new snippet."""
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a code snippet."""
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
    
class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    
# Note: Edge cases we are not dealing with yet
#       - malformed json, 
#       - request with no view.

        
        