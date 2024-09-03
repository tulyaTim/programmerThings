from base.models import Notes
from rest_framework.serializers import ModelSerializer

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'