from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.

from .models import Offerta,Oggetto,Categoria,Feedback

from django import forms
from aste_core.models import Indirizzo as I

class AddObject(forms.Form):
	Nome = forms.CharField(label='Nome', required=True)
	PrezzoPartenza=forms.FloatField(label='PrezzoPartenza', required=True)
	PrezzoCompraSubito=forms.FloatField(label='PrezzoCompraSubito', required=False)
	c=(("k","k"),)
	for i in Categoria.objects.all() :
		p=((i.nome,i.nome),)
		c=c+p
	cat=forms.ChoiceField(label='Cate',required=False,choices=c)
	Durata=forms.IntegerField(label='Durata',required=True)
	img=forms.ImageField(label="img",required=True)

def index(req):
	return render(req,'aste_core/index.html')

def ll(req):
	print('ddddd')
	if req.method == 'POST' :
		print(req.FILES)
		f=AddObject(req.POST,req.FILES)
		#print(f.__str__())
		#print(req.POST['Username'])
		if f.is_valid() :
			print(f.__str__())
			try:
				g=open('foto.jpg','wb')
				g.write(f.cleaned_data['img'].read())
				print('ok')
			except  Exception as e:
				return render(req,'reg/sign_up.html',{'form':AddObject(),'msg':e.__str__})
			#print(f.)
			return HttpResponseRedirect(req.POST['next'])
		else:
			print('no ok')
			print(f.errors)
			#return HttpResponseRedirect(req.POST['next'])
			return render(req,'reg/sign_up.html',{'form':AddObject(),'msg':"Dati Insereti non validi",'next':req.POST['next']})
	else:
		try:
			f=req.GET['next']
			return render(req,'reg/sign_up.html',{'form':AddObject(),'next':req.GET['next']})
		except Exception as e:
			return render(req,'reg/sign_up.html',{'form':AddObject(),'next':'/'})

@login_required
def kk(req,str):
	print(req.user)
	print('dsa')
	return render(req,'aste_core/kk.html',{'ll':str})

