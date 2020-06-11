from django import forms
from userApp.models import UserData

class NewUserForm(forms.ModelForm):
    
    class Meta:
        model = UserData
        fields = '__all__' #karena butuh semua inputan