from django.shortcuts import render,redirect

from .models import Profile
from django.contrib.auth.models import User
from .forms import CreateUserForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
            
    return render(request, 'User/register.html',{
        "form":form
    })
      
# Profile Page of the People
def profile(request):
    return render(request,"User/admin_profile.html")    

# edit Profile

"""
def edit_product(request,id):
    file_record = File_Upload.objects.get(ids=id)
    form = UploadFile_Form(instance=file_record)   
    if request.method == "POST":
         form = UploadFile_Form(request.POST,instance = file_record)
         if form.is_valid():
             form.save()
             return redirect("d-products")
    return render(request,"Dashboard/edit_product.html",{
        "form":form
    })
"""

