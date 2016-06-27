from django import forms

from .models import Arbeitskraft,Firma

class ArbeitskraftForm(forms.ModelForm):

    class Meta:
        model = Arbeitskraft
        fields = ('nachname', 'vorname','ausweisnummer','strasse','hausnummer','plz','foto','telefon','mobil', 'beacon','firma')