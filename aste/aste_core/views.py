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

STATO_OGGETTO=['IN_CORSO','TEMPO_FINITO',"COMPRA_SUBITO","PAGATO","SPEDITO"]

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
	des=forms.CharField(label='Descrizione',required=True)

def index(req):
	o=Oggetto.objects.all().order_by('?')[:5]
	#o=Oggetto.objects.filter(data_termine__gt=datetime.datetime.now()).order_by('nome')[:5]
	return render(req,'aste_core/index.html',{'o':o})

@login_required
def compra_subito(req):
	o = get_object_or_404(Oggetto, pk=int(req.GET['pk']))
	try:
		o.compra_subito(req.user)
		mess=''
	except Exception as e:
			mess='/Impossibiel completare la richiesta'
	return HttpResponseRedirect('/item/'+req.GET['pk']+mess)


@login_required
def bid(req):
	o = get_object_or_404(Oggetto, pk=int(req.GET['pk']))
	mess=''
	try:
		off = Offerta.CreateOfferta(oggetto=o,utente=req.user,prezzo_massimo=float(req.GET['offerta']))
		mess=off[1]
	except Exception as e:
		if e.args[0] == 1 :
			mess='/Non puoi offrire per i tuoi oggetti'
		if e.args[0] ==  3 :
			mess='/Asta Chiusa'
		if e.args[0] ==  2 :
			mess='/Offerta troppo bassa'

	return HttpResponseRedirect('/item/'+req.GET['pk']+mess)

@login_required
def account(req):
	o=Oggetto.objects.filter(utente=req.user,data_termine__gt=datetime.datetime.now())
	oo=Oggetto.objects.filter(utente=req.user,data_termine__lt=datetime.datetime.now())
	return render(req,'aste_core/account.html',{'o':o,'oo':oo,'tipo': 1,'stato':STATO_OGGETTO})

@login_required
def offerte(req):
	off=Offerta.objects.filter(utente=req.user)
	o=[]
	oo=[]
	for i in off:
		if not i.oggetto.is_past_due :
			o.append(i.oggetto)
	for i in off:
		if i.oggetto.is_past_due :
			oo.append(i.oggetto)
	return render(req,'aste_core/account.html',{'o':o,'oo':oo,'tipo':2,'stato':STATO_OGGETTO})

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
				obj = Oggetto.objects.create(descrizione=f.cleaned_data['des'],nome=f.cleaned_data['Nome'],prezzo_partenza=f.cleaned_data['PrezzoPartenza'],prezzo_attuale=0,
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

def show_item(req,pk,mess):
	o = get_object_or_404(Oggetto, pk=int(pk))
	print(mess)
	return render(req,'aste_core/show_item.html',{'o':o,'mess':mess[1:]})

def search(req):
	try:
		s=req.GET['s']
	except Exception as e:
		s=''
	o=Oggetto.objects.none()
	for i in req.GET['s'].split(' '):
		o = o | Oggetto.objects.filter(data_termine__gt=datetime.datetime.now(),nome__contains=i)
	return render(req,'aste_core/index.html',{'o':o})

@login_required
def kk(req,str):
	print(dir(req))
	print(req.user)
	print(req.user)
	print('dsa')
	return render(req,'aste_core/kk.html',{'ll':str})

