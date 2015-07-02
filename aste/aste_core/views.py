from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Offerta,Oggetto,Categoria,Feedback

from django import forms
from aste_core.models import Indirizzo as I

class AddObject(forms.Form):
	Nome = forms.CharField(label='Nome', required=True)
	PrezzoPartenza=forms.FloatField(label='PrezzoPartenza', required=True)
	PrezzoCompraSubito=forms.FloatField(label='PrezzoCompraSubito', required=False)
	c=()
	for i in Categoria.objects.all() :
		p=((i.nome,i.nome),)
		c=c+p
	cat=forms.ChoiceField(label='Cate',required=True,choices=c)
	Durata=forms.IntegerField(label='Durata',required=True)
	Img=forms.ImageField(label="im",required=True)

def index(req):
	return render(req,'aste_core/index.html')

def ll(req):
	print('ddddd')
	if req.method == 'POST' :
		f=AddObject(req.POST)
		print(req.POST['Username'])
		if False or f.is_valid() :
			#print(f.Username)
			try:
				print('ok')
			except  Exception as e:
				return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':e.__str__})
			#print(f.)
			return HttpResponseRedirect(req.POST['next'])
		else:
			return HttpResponseRedirect(req.POST['next'])
			return render(req,'reg/sign_up.html',{'form':SignUpForm(),'msg':"Dati Insereti non validi"})
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

