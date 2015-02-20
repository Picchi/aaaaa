from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

class SignUpForm(forms.Form):
    Username=forms.CharField(label='Username', required=True )
    Password=forms.CharField(label='Password', required=True,widget=forms.PasswordInput())
    Password2=forms.CharField(label='Reiserire Password', required=True,widget=forms.PasswordInput())
    Nome = forms.CharField(label='Nome', required=True)
    Cognome=forms.CharField(label='Cognome', required=True)
    Mail=forms.EmailField(label='Mail', required=True)
    #Img=forms.ImageField(label="im")


def logout_page(request):
    logout(request)
    print("LogOut ")
    return HttpResponseRedirect('/')

def sign_up_page(req):
	if req.user.is_authenticated():
		return HttpResponseRedirect('/')
	if req.method == 'POST' :
		f=SignUpForm(req.POST)
		if f.is_valid():
			print("Kkk")
			return HttpResponseRedirect('.')
		else:
			return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':"Dati Insereti non validi"})
	else:
		return render(req,'reg/sign_up.html',{'form':SignUpForm()})
