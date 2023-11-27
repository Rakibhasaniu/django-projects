from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author': 'rakib', 'age': 24}
    return render(request,'home.html',d)
