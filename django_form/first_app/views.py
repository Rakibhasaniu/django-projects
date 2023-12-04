from django.shortcuts import render

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