
from django.shortcuts import render, redirect, get_object_or_404

from mistri_info.models import Mistri

# Create your views here.

def home(request):
    return render(request, "index.html")

def add_mistri(request):

    if request.method == 'POST':
        Mistri.objects.create(
            image= request.FILES.get('image'),
            name= request.POST.get('name'),
            skill= request.POST.get('skill'),
            location= request.POST.get('location'),
            contact= request.POST.get('contact')
        )
        return redirect(all_mistri)

    return render(request, "mistri/add_mistri.html")


def all_mistri(request):

    data = Mistri.objects.all()

    context = {
        "mistris" : data
    }

    return render(request, "mistri/all_mistri.html", context)
