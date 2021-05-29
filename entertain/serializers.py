from rest_framework import serializers
from .models import Room
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','name','host','description','user_pause','vote_to_skip',
                  'created_at')


