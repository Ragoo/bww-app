from django import forms

from .models import Arbeitskraft,Firma,Beacon,Projekt

class ArbeitskraftForm(forms.ModelForm):

    class Meta:
        model = Arbeitskraft
        fields = ('nachname', 'vorname','ausweisnummer','strasse','hausnummer','plz','foto','telefon','mobil', 'beacon','firma')

class FirmaForm(forms.ModelForm):

    class Meta:
        model = Firma
        fields = ('name','strasse','hausnummer','plz','telefon')

class ProjektForm(forms.ModelForm):

    class Meta:
        model = Projekt
        fields = ('name',)

class BeaconForm(forms.ModelForm):

    class Meta:
        model = Beacon
        fields = ('id',)
