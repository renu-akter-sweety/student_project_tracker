from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from project_app.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def signuppage(req):
    if req.method=='POST':
        student_name= req.POST.get("student_name")
        student_id= req.POST.get("student_id")
        username= req.POST.get("username")
        email= req.POST.get("email")
        password= req.POST.get("password")
        confirm_password= req.POST.get("confirm_password")
        username_exists=UserModel.objects.filter(username=username).exists()
       
        if username_exists:
            print("username already exists.")
            return redirect("sign_upurl")
        else:
            if password==confirm_password:   
                print('same hoise ') 
                UserModel.objects.create_user(

                    username=username,
                    student_name=student_name,
                    student_id=student_id,
                    email=email,
                    password=confirm_password,
                 
                    )
                return redirect("log_inurl")

            else:
                print("both password are not matched")

    return render(req,"signup_page.html")

def loginpage(req):
    if req.method=='POST':
        password=req.POST.get("password")
        username= req.POST.get("username")
        user = authenticate(
            username=username,
            password=password
        )
        if user:

         login(req,user)
        return redirect("baseurl")
    return render(req,"log_in.html")

def log_outpage(req):
    return render(req)



@login_required
def basepage(req):
    return render(req,"base.html")




@login_required

def addproject(req):
    projects = ProjectModel.objects.all()
    users = UserModel.objects.all()

    if req.method == "POST":
        project_name = req.POST.get("project_name")
        project_description = req.POST.get("project_description")
        project_status = req.POST.get("project_status")
        deadline = req.POST.get("deadline")
        thumbnail = req.FILES.get("thumbnail")

        # Directly get the selected user
        created_by_id = req.POST.get("created_by")
        created_by = UserModel.objects.get(id=created_by_id)  # assumes valid ID

        # Save project
        ProjectModel.objects.create(
            project_name=project_name,
            project_description=project_description,
            project_status=project_status,
            deadline=deadline,
            thumbnail=thumbnail,
            created_by=created_by,
        )
        return redirect("addprojecturl")

    context = {
        "projects": projects,
        "users": users,
    }
    return render(req, "addproject.html", context)

@login_required
def editproject(req, id):
    project = get_object_or_404(ProjectModel, id=id)
    users = UserModel.objects.all()

    if req.method == "POST":
        project.project_name = req.POST.get("project_name")
        project.project_description = req.POST.get("project_description")
        project.project_status = req.POST.get("project_status")
        project.deadline = req.POST.get("deadline")
        created_by_id = req.POST.get("created_by")
        project.created_by = UserModel.objects.get(id=created_by_id)
        
        thumbnail = req.FILES.get('thumbnail')  # <-- Fixed here
        print(True) if thumbnail else print(False)
        if thumbnail:
            project.thumbnail = thumbnail
        project.save()
        return redirect("addprojecturl")

    return render(req, "editproject.html", {"project": project, "users": users})


@login_required

def deleteproject(req, id):
    project = get_object_or_404(ProjectModel, id=id)
    project.delete()
    return redirect("addprojecturl")


def log_outpage(req):
    logout(req)
    return redirect("log_inurl")
 
