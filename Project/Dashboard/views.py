from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import UploadFile_Form
from .models import File_Upload, Updates

from django.contrib.auth.models import User
from User.models import Profile
# Create your views here. 
@login_required(login_url="u-login")
def index(request):
    files_all = File_Upload.objects.all()
    files_c = files_all.count()
    users = Profile.objects.all().count()
    
    updates = Updates.objects.all()
    all_updates = updates.count()
    if request.method == "POST":
        form = UploadFile_Form(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user_specific = request.user
            inst.save()
            
            upload_update = Updates.objects.create(name= request.user, upload= "Has uploaded a File")
            upload_update.save()
            return redirect("d-index")
    form = UploadFile_Form()       
    return render(request,"Dashboard/index.html",{
        "count_p":files_c,
        "count_s":users,
        "form":form,
        "files_all":files_all,
        "count_up":all_updates
    })


@login_required(login_url="u-login")
def staff(request):
    files_all = File_Upload.objects.all().count()    
    users = Profile.objects.all()   
    users_all = users.count() 
    updates = Updates.objects.all()
    all_updates = updates.count()
    return render(request,"Dashboard/staff.html",{
        "count_p":files_all,
        "User":users,
        "count_s":users_all,
        "count_up":all_updates
    }) 
 
 
"""
All about the Products(File) Page
---> Delete
---> Edit
"""

"""
if request.method == "POST":
        form = UploadFile_Form(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user_specific = request.user
            inst.save()
            return redirect("d-index")""" 
@login_required(login_url="u-login")
def products(request):    
    files_all = File_Upload.objects.all()
    user_specific_files = File_Upload.objects.filter(user_specific = request.user)  
    count_file = user_specific_files.count()
    users = Profile.objects.all().count()   
    updates = Updates.objects.all()
    all_updates = updates.count()    
    
    if request.method == "POST":
        form = UploadFile_Form(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user_specific = request.user
            inst.save() 
            messages.success(request,"File has been uploaded!")
            upload_update = Updates.objects.create(name= request.user, upload = "Has uploaded a File")
            upload_update.save()            
            return redirect("d-products")
    else: 
        form = UploadFile_Form()            
    return render(request,"Dashboard/products.html",{
        "form":form,
        "files":files_all,
        "count_p":count_file,
        "count_s":users,
        "count_up":all_updates
    })

# Delete Product and Also Delete Staff Product
def delete_product(request,id):
    if request.method == "POST":
        data = File_Upload.objects.get(ids=id)
        data.delete()
        delete_update = Updates.objects.create(name= request.user, upload="Has deleted a File")
        delete_update.save()
        return redirect("d-products") 
    return render(request,"Dashboard/delete_product.html")

def staff_delete(request,id):
    if request.method == "POST":
        data = File_Upload.objects.get(ids=id)
        data.delete()
        delete_update = Updates.objects.create(name= request.user, upload="Has deleted a File")
        delete_update.save()
        return redirect("d-index")
    return render(request,"Dashboard/staff_delete.html")

# Edit Product and Staff Edit 
def edit_product(request,id):
    file_record = File_Upload.objects.get(ids=id)
    form = UploadFile_Form(instance=file_record)   
    if request.method == "POST":
         form = UploadFile_Form(request.POST,instance = file_record)
         if form.is_valid():
             form.save() 
             edit_update = Updates.objects.create(name=request.user, upload= "Has edited the File")
             edit_update.save()
             
             return redirect("d-products")
    return render(request,"Dashboard/edit_product.html",{
        "form":form
    })

def staff_edit(request,id):
    file_record = File_Upload.objects.get(ids=id)
    form = UploadFile_Form(instance = file_record)
    if request.method == "POST":
        form = UploadFile_Form(request.POST, instance = file_record)
        if form.is_valid():
            form.save()
            edit_update = Updates.objects.create(name=request.user, upload = "Has edited the File")
            edit_update.save()            
            return redirect("d-index")
    return render(request,"Dashboard/staff_edit.html",{
        "form":form
    })
  
@login_required(login_url="u-login")
def orders(request):
    files_all = File_Upload.objects.all()
    count_files = files_all.count()
    updates = Updates.objects.all()
    all_updates = updates.count()
    users = Profile.objects.all().count()        
         
    return render(request,"Dashboard/orders.html",{
        "count_p":count_files,
        "count_s":users,
        "updates":updates,
        "count_up":all_updates
    }) 