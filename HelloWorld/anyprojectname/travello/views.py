from django.shortcuts import render
from .models import destination

# Create your views here.
def travello(request):
    dests = destination.objects.all()
    return render( request, 'index.html', { 'destinations' : dests } )

