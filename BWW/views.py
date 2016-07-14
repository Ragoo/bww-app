from django.shortcuts import render, get_object_or_404, redirect
from .models import Arbeitskraft, Firma,Beacon,Projekt
from .forms import ArbeitskraftForm, FirmaForm

"""REST TEST IMPORTS"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import UserSerializer, GroupSerializer, ArbeitskraftSerializer

# Create your views here.

def home(request):
    return render(request, 'BWW/home.html')

"""
Arbeitskraft
"""
def arbeitskraft_list(request):
    arbeitskraft = Arbeitskraft.objects.order_by('vorname')
    return render(request, 'BWW/arbeitskraft_list.html', {'arbeitskraft': arbeitskraft})


def arbeitskraft_detail(request, pk):
    arbeitskraft = get_object_or_404(Arbeitskraft, pk = pk)
    return render(request, 'BWW/arbeitskraft_detail.html', {'arbeitskraft': arbeitskraft})


def arbeitskraft_neu(request):
    if request.method == "POST":
        form = ArbeitskraftForm(request.POST)
        if form.is_valid():
            arbeitskraft = form.save(commit=False)
            arbeitskraft.save()
            return redirect('arbeitskraft_detail', pk=arbeitskraft.pk)
    else:
        form = ArbeitskraftForm()
    return render(request, 'BWW/arbeitskraft_edit.html', {'form': form})


def arbeitskraft_edit(request, pk):
    arbeitskraft = get_object_or_404(Arbeitskraft, pk = pk)
    if request.method == "POST":
        form = ArbeitskraftForm(request.POST, instance=arbeitskraft)
        if form.is_valid():
            arbeitskraft = form.save(commit=False)
            arbeitskraft.save()
            return redirect('arbeitskraft_detail', pk=arbeitskraft.pk)
    else:
        form = ArbeitskraftForm(instance=arbeitskraft)
    return render(request, 'BWW/arbeitskraft_edit.html', {'form': form})


"""
Firma
"""
def firma_list(request):
    firma = Firma.objects.order_by('name')
    return render(request, 'BWW/firma_list.html', {'firma': firma})

def firma_detail(request,pk):
    firma = get_object_or_404(Firma, pk = pk)
    return render(request, 'BWW/firma_detail.html', {'firma':firma})


def firma_neu(request):
    if request.method == "POST":
        form = FirmaForm(request.POST)
        if form.is_valid():
            firma = form.save(commit=False)
            firma.save()
            return redirect('firma_detail', pk=firma.pk)
    else:
        form = FirmaForm()
    return render(request, 'BWW/firma_edit.html', {'form': form})


def firma_edit(request, pk):
    firma = get_object_or_404(Firma, pk = pk)
    if request.method == "POST":
        form = FirmaForm(request.POST, instance=firma)
        if form.is_valid():
            firma = form.save(commit=False)
            firma.save()
            return redirect('firma_detail', pk=firma.pk)
    else:
        form = FirmaForm(instance=firma)
    return render(request, 'BWW/firma_edit.html', {'form': form})


"""
REST VIEWS
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ArbeitskraftViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Arbeitskraft to be viewed or edited."""
    queryset = Arbeitskraft.objects.all().order_by('nachname')
    serializer_class = ArbeitskraftSerializer

class ArbeitskraftList(generics.ListAPIView):
    serializer_class = ArbeitskraftSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        nachname = self.kwargs['nachname']
        return Arbeitskraft.objects.filter(nachname=nachname)

