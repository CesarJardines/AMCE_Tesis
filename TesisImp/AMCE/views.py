from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext

# Create your views here.

def index(request):
	return render(request, "AMCE/index.html")

@login_required
def MG1(request):
	return render(request,"AMCE/MG1.html")

def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}
	if request.method == "POST":
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request,user)
			messages.success(request, "Tu registro ha sido exitoso")
			return redirect(to="AMCE:MG1")
		data["form"] = formulario
	return render(request,'registration/registro.html',data)





