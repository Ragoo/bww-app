from django.contrib.auth.models import User, Group
from .models import Arbeitskraft
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ArbeitskraftSerializer(serializers.HyperlinkedModelSerializer):
    firma = serializers.CharField(source='firma.name')
    beacon = serializers.CharField(source='beacon.id')

    class Meta:
        model = Arbeitskraft
        fields = ('id','nachname', 'vorname','firma','foto','beacon')