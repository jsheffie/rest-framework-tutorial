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
    
    def get(self, request, *args, **kwargs ):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):    
        return self.create(request, *args, **kwargs )
        
class SnippetDetail(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    generics.SingleObjectAPIView):
    """ Retrieve, update or delete a code snippet."""
    model = Snippet
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs ):
        return self.destroy(request, *args, **kwargs)
    
# Note: Edge cases we are not dealing with yet
#       - malformed json, 
#       - request with no view.

        
        