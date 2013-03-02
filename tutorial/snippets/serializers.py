from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer( serializers.Serializer ):
    pk       = serializers.Field() # Note: 'Field' is an untyped read-only field.
    title    = serializers.CharField(required=False, 
                                     max_length=100)
    code     = serializers.CharField(widget=widgets.Textarea, 
                                     max_length=100000)
    linenos  = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, 
                                       default='python')
    style    = serializers.ChoiceField(choices=STYLE_CHOICES, 
                                       default='friendly')
    
    def restore_object(self, attrs, instance=None):
        """ Create or update a snippit instance
        Note: we can actually save time by using the ModelSerializer class. """
        if instance:
            # update an existing instance
            instance.title    = attrs.get('title',    instance.title)
            instance.code     = attrs.get('code',     instance.code)
            instance.linenos  = attrs.get('linenos',  instance.linenos) 
            instance.language = attrs.get('language', instance.language)
            instance.style    = attrs.get('style',    instance.style)
            return instance
        
        # create new instance
        return Snippet(**attrs) 