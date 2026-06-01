from rest_framework import serializers
from trade_notes.models import trade_notes

class trade_notes_serializer(serializers.ModelSerializer):
    class Meta:
        model = trade_notes
        fields = '__all__'
        read_only_fields = ['created_on', 'note_id', 'author']
        
