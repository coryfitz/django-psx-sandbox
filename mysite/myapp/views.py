from django.shortcuts import render

def index(request):
    return render(request, "myapp/index.html")

def about(request):
    return render(request, "myapp/about.html")

def examples(request):
    return render(request, "myapp/examples.html")

def docs(request):
    return render(request, "myapp/docs.html")