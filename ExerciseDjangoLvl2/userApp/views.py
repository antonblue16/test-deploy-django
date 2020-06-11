from django.shortcuts import render
from django.http import HttpResponse
from userApp.models import UserData
from userApp.forms import NewUserForm


# Create your views here.
def index(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("Error Form Invalid!")
    
    return render(request, "index.html", {'form':form})

def user(request):
    firstName = UserData.objects.order_by('firstName')
    lastName = UserData.objects.order_by('lastName')
    email = UserData.objects.order_by('email')
    address = UserData.objects.order_by('address')

    myUser = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "address": address,
        }
    return render(request, "user.html", context=myUser)

