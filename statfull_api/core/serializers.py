from rest_framework import serializers
from .models import Task


class NewTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title','description']

class NewTaskEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id','title','description']


class LinkTaskSerializer(serializers.Serializer):
    first_id = serializers.IntegerField()
    sec_id = serializers.IntegerField()



class ChangeTaskStateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    state = serializers.CharField()

class ShowTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id' ,'title','description' , 'state', 'linked_id']
        read_only_fields = ['id']