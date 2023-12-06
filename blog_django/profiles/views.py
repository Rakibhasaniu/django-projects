from django.shortcuts import render, redirect

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = forms.AuthorForm()
    return render(request,'add_profile.html')