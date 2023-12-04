from django.shortcuts import render
from .form import contact_form

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'about.html',{'name': name,'email': email,'select': select})
    else:
      return render(request,'about.html')

def submit_form(request):
    # if request.method == 'POST':
    #     name=request.POST.get('username')
    #     email=request.POST.get('email')
    #     return render(request,'form.html',{'name': name,'email': email})
    # else:
    #     return render(request,'form.html')
    return render(request,'form.html')

def django_form(request):
    if request.method == 'POST':
     form=contact_form(request.POST,request.FILES)
     if form.is_valid():
        file= form.cleaned_data['file']
        # print(form.cleaned_data)
        with open('./first_app/upload/'+ file.name, 'wb+') as destination:
           for chunk in file.chunks():
              destination.write(chunk)
        return render(request,'django_form.html',{'form': form})
    else:
       form=contact_form()
    return render(request,'django_form.html',{'form': form})
