from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Permission
from django.shortcuts import render
from django import forms
from aste_core.models import Indirizzo as I

class SignUpForm(forms.Form):
    Username=forms.CharField(label='Username', required=True )
    Password=forms.CharField(label='Password', required=True,widget=forms.PasswordInput())
    Password2=forms.CharField(label='Reiserire Password', required=True,widget=forms.PasswordInput())
    Nome = forms.CharField(label='Nome', required=True)
    Cognome=forms.CharField(label='Cognome', required=True)
    Mail=forms.EmailField(label='Mail', required=True)
    Via=forms.CharField(label='Via', required=True)
    Citta=forms.CharField(label='Citta', required=True)
    Provincia=forms.CharField(label='Provincia', required=True)
    Cap=forms.CharField(label='Cap', required=True)

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
		#print(req.POST['Username'])
		if False or f.is_valid() or req.POST['Password']!=req.POST['Password2']:
			#print(f.Username)
			try:
				user = User.objects.create_user(req.POST['Username'],req.POST['Mail'], req.POST['Password'])
				user.first_name=req.POST['Nome']
				user.last_name=req.POST['Cognome']
				user.user_permissions.add(Permission.objects.get(name='Can add indirizzo'))
				user.user_permissions.add(Permission.objects.get(name='Can change indirizzo'))
				user.user_permissions.add(Permission.objects.get(name='Can delete indirizzo'))
				user.user_permissions.add(Permission.objects.get(name='Can add oggetto'))
				user.user_permissions.add(Permission.objects.get(name='Can change oggetto'))
				user.user_permissions.add(Permission.objects.get(name='Can add offerta'))
				user.user_permissions.add(Permission.objects.get(name='Can change offerta'))
				user.save()
				II=I.objects.create(via=req.POST['Via'])
			except  Exception as e:
				return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':e.__str__})
			#print(f.)
			return HttpResponseRedirect(req.POST['next'])
		else:
			return HttpResponseRedirect(req.POST['next'])
			return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':"Dati Insereti non validi"})
	else:
		return render(req,'reg/sign_up.html',{'form':SignUpForm(),'next':req.GET['next']})
