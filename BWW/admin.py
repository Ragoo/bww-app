from django.contrib import admin
from .models import Arbeitskraft, Firma, Beacon, Projekt


admin.site.register(Arbeitskraft)
admin.site.register(Firma)
admin.site.register(Beacon)
admin.site.register(Projekt)