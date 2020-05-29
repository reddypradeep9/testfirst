from django.shortcuts import render
from . import forms

def studentview(request):
    form=forms.studentform()
    if request.method=="POST":
        form=forms.studentform(request.POST)
        if form.is_valid():
            form.save(commit="True")
    return render(request,"firstapp/one.html",{"form":form})

def thankview(request):
    return render(request,"firstapp/two.html")
