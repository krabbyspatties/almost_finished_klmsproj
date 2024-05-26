from django.shortcuts import render, redirect
from . models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

#Gender views
def index_gender(request):
    genders = Gender.objects.all() #select all from mysql
    context = {
        'genders': genders
    }
    return render(request, 'genders/index.html', context)
    return render(request, 'genders/index.html')

def create_gender(request):
    return render(request, 'genders/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) # add an object to a table 
    messages.success(request,'Gender successfully saved')

    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #select from mysql

    context = {
        'gender': gender,
    }

    return render(request, 'genders/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select a specfic object from mysql
    context = {
        'gender': gender,
    }

    return render(request, 'genders/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
    Gender.objects.filter(pk=gender_id).update(gender=gender) #update for mysql
    messages.success(request, 'gender successfully updated')

    return redirect('/genders')

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select for mysql
    context = {
        'gender': gender,
    }
    
    return render(request, 'genders/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() #delete from mysql
    messages.success(request, 'gender successfully Deleted')

    return redirect('/genders')

#User views

def index_user(request):
    users = User.objects.select_related('gender')

    context={
        'users': users,
    }
    return render(request, 'users/index.html', context)

def create_user(request):
    genders = Gender.objects.all()

    context = {
        'genders':genders
    }
    return render(request, 'users/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

    if password == confirmPassword:
        encryptedPassword = make_password(password)

        User.objects.create(
            first_name=firstName,
            middle_name=middleName,
            last_name=lastName,
            age=age,
            birth_date=birthDate,
            gender_id=genderId,
            username=username,
            password= encryptedPassword
            )
        messages.success(request, 'success')

        return redirect('/users')
    else:
        messages.error(request, 'error')
        return redirect('users/create.html')