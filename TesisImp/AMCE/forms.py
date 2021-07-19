from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Heredo del userCreationForm que viene en django
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
		