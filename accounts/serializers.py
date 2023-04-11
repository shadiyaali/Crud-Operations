from rest_framework import serializers
from accounts.models import User,Notes

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes 
        fields = ['title','description','rating']

       