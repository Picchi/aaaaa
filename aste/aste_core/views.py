from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
import datetime
import random
from django.shortcuts import get_object_or_404

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
		print(i)
		p=((i.nome,i.nome),)
		c=c+p
	cat=forms.ChoiceField(label='Categoria',required=True,choices=c)
	Durata=forms.IntegerField(label='Durata in giorni',required=True)
	img=forms.ImageField(label="Immagine articolo",required=True)

def index(req):
	o=Oggetto.objects.all().order_by('?')[:5]
	return render(req,'aste_core/index.html',{'o':o})

@login_required
def sell_object(req):
	print('ddddd')
	if req.method == 'POST' :
		print(req.FILES)
		f=AddObject(req.POST,req.FILES)
		#print(f.__str__())
		#print(req.POST['Username'])
		if f.is_valid() :
			print(f.__str__())
			try:
				try:
					p_c=float(req.POST['PrezzoCompraSubito'])
				except Exception as e:
					p_c=0
				fe=Feedback.objects.create()
				t=timezone.now()
				if p_c is not 0 and float(req.POST['PrezzoPartenza']) > p_c:
					raise Exception("Prezzo compralo subito minore prezzo partenza")
				obj = Oggetto.objects.create(nome=f.cleaned_data['Nome'],prezzo_partenza=f.cleaned_data['PrezzoPartenza'],prezzo_attuale=0,
					prezzo_compra_subito=p_c,data_termine=t+datetime.timedelta(days=f.cleaned_data['Durata'],seconds=-t.second,microseconds=-t.microsecond),
					categoria=Categoria.objects.get(nome=f.cleaned_data['cat']),utente=req.user,utente_vincente=req.user,feedback=fe,foto=f.cleaned_data['img'])
				fe.save()
				obj.save()
				print('ok')
			except  Exception as e:
				fe.delete()
				return render(req,'aste_core/sell_object.html',{'form':AddObject(),'msg':e.__str__})
			#print(f.)
			return HttpResponseRedirect(req.POST['next'])
		else:
			print('no ok')
			print(f.errors)
			#return HttpResponseRedirect(req.POST['next'])
			return render(req,'aste_core/sell_object.html',{'form':AddObject(),'msg':"Dati Insereti non validi",'next':req.POST['next']})
	else:
		try:
			return render(req,'aste_core/sell_object.html',{'form':AddObject(),'next':req.GET['next']})
		except Exception as e:
			return render(req,'aste_core/sell_object.html',{'form':AddObject(),'next':'/'})

def show_item(req,pk):
	o = get_object_or_404(Oggetto, pk=int(pk))
	return render('aste_core/show_item',{'o':0})

def search(req):
	try:
		s=req.GET['s']
	except Exception as e:
		s=''
	o=Oggetto.objects.none()
	for i in req.GET['s'].split(' '):
		o = o | Oggetto.objects.filter(nome__contains=i)
	return render(req,'aste_core/index.html',{'o':o})

@login_required
def kk(req,str):
	print(dir(req))
	print(req.user)
	print(req.user)
	print('dsa')
	return render(req,'aste_core/kk.html',{'ll':str})

