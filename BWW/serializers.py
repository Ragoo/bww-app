from django.contrib.auth.models import User, Group
from .models import Arbeitskraft, Firma, Beacon, Projekt
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
        fields = ('id','nachname', 'vorname','firma','foto','beacon','ausweisnummer','strasse','hausnummer','plz','telefon','mobil')

class FirmaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Firma
        fields = ('id','name', 'strasse','hausnummer','plz','telefon')

class BeaconSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beacon
        fields = ('id','zuletzt_gesehen', 'letzter_boot')

class ProjektSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Projekt
        fields = ('name',)