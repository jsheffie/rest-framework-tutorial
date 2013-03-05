from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, 
                  generics.MultipleObjectAPIView):
    """ List all code snippets, or create a new snippet."""
    model = Snippet
    serializer_class = SnippetSerializer
        
class SnippetDetail(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    generics.SingleObjectAPIView):
    """ Retrieve, update or delete a code snippet."""
    model = Snippet
    serializer_class = SnippetSerializer
    
# Note: Edge cases we are not dealing with yet
#       - malformed json, 
#       - request with no view.

        
        