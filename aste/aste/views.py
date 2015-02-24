from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Permissions
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
    Provincia=forms.CharField(label='Via', required=True)
    Cap=forms.CharField(label='Via', required=True)

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
		if f.is_valid() or req.POST['Password']!=req.POST['Password2']:
			print(f.Username)
			try:
				user = User.objects.create_user(req.POST['Username'],req.POST['Mail'], req.POST['Password'])
				user.first_name=req.POST['Nome']
				user.last_name=req.POST['Cognome']
				user.user_permissions.add(Permissions.objects.get(name='Can add Indirizzo'))
				user.user_permissions.add(Permissions.objects.get(name='Can change Indirizzo')
				user.user_permissions.add(Permissions.objects.get(name='Can delete Indirizzo'))
				user.user_permissions.add(Permissions.objects.get(name='Can add Oggetto'))
				user.user_permissions.add(Permissions.objects.get(name='Can change Oggetto'))
				user.user_permissions.add(Permissions.objects.get(name='Can add Offerta'))
				user.user_permissions.add(Permissions.objects.get(name='Can change Offerta'))

				user.save()
				II=I.objects.create(via=req.POST['Via'])
			except  e:
				return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':e.__str__})
			#print(f.)
			return HttpResponseRedirect('.')
		else:
			return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':"Dati Insereti non validi"})
	else:
		return render(req,'reg/sign_up.html',{'form':SignUpForm()})
