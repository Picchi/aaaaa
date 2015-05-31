from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Indirizzo(models.Model):
#	username=models.CharField(max_length=20)
#	nome=models.CharField(max_length=50)
#	cognome=models.CharField(max_length=50)
	via=models.CharField(max_length=150)
	citta=models.CharField(max_length=150,default=None)
	provincia=models.CharField(max_length=150,default=None)
	cap=models.CharField(max_length=6,default=None)
	ref=models.ForeignKey(User,related_name="ref")




class Categoria(models.Model):
	nome=models.CharField(max_length=50)

class Feedback(models.Model):
	feed_veniditore=models.TextField()
	feed_acquirente=models.TextField()
	feed_veniditore=models.IntegerField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)),default=0)
	feed_acquirente=models.IntegerField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)),default=0)


class Oggetto(models.Model):
	nome=models.CharField(max_length=50)
	data_pubblicazione=models.DateTimeField(auto_now_add=True)
	STATO_OGGETTO=((1,'IN_CORSO'),(2,'TEMPO_FINITO'),(3,"COMPRA_SUBITO"),(4,"PAGATO"),(5,"SPEDITO")) 
	stato=models.IntegerField(choices=STATO_OGGETTO,default=1)
	descrizione=models.TextField()
	data_termine=models.DateTimeField('data di fine asta')
	prezzo_partenza=models.FloatField()
	prezzo_attuale=models.FloatField(default=0)
	prezzo_compra_subito=models.FloatField(default=0)
	categoria=models.ForeignKey(Categoria,related_name="oggetti")
	utente=models.ForeignKey(User,related_name="oggetti")
	utente_vincente=models.ForeignKey(User,related_name="vincente")
	foto=models.FileField(upload_to="foto");
	feedback=models.ForeignKey(Feedback,related_name="ogg_feed")

	def compra_subito(self,utente):
		if self.prezzo_compra_subito == 0 :
			raise Exception(1)
		if self.stato != 1 :
			raise Exception(1)
		self.stato=3
		self.utente_vincente=utente
		self.save()


	def add_offerta(self,new_off):
		if self.utente.pk==new_off.utente.pk:
			raise Exception(1)
		if self.stato != 1:
			raise Exception(3)
		if new_off.utente.id==self.utente_vincente.id:
			return (0,"Miglior offerte")
		if new_off.prezzo_massimo <= self.prezzo_attuale :
			raise Exception(2)
		if self.prezzo_attuale == 0  :
			self.prezzo_attuale=self.prezzo_partenza
			self.utente_vincente=new_off.utente
			self.save()
			return (0,"Miglior offerte")
		of=Offerta.objects.get(oggetto=self.id,utente=self.utente_vincente.id)
		#print("kk "+new_off.prezzo_massimo.__str__()+" "+self.prezzo_attuale.__str__())
		if of.prezzo_massimo >= new_off.prezzo_massimo :
			self.prezzo_attuale=of.prezzo_massimo-((of.prezzo_massimo-new_off.prezzo_massimo-0.05) if of.prezzo_massimo!=new_off.prezzo_massimo else 0 )
			self.save()
			return (1,"Offerta superata")
		self.prezzo_attuale=new_off.prezzo_massimo-(new_off.prezzo_massimo-of.prezzo_massimo-0.05)
		self.utente_vincente=new_off.utente
		self.save()
		return (0,"Miglior offerte")
	

	#offerta_migliore=models.ForeignKey(Offerta,related_name='Oggetto')



class Offerta(models.Model):
	oggetto=models.ForeignKey(Oggetto,related_name="offerte")
	utente=models.ForeignKey(User,related_name="offerta")
	data=models.DateTimeField(auto_now_add=True)
	prezzo_massimo=models.FloatField(default=0)

	@classmethod
	def CreateOfferta(cls,oggetto=None,utente=None,prezzo_massimo=0,data=None):
		try:
			o=Offerta.objects.get(oggetto=oggetto,utente=utente)
			#if o.prezzo_massimo > prezzo_massimo :
			#	return
			#o.delete()
			#raise Exception
			o.prezzo_massimo=prezzo_massimo
			o.save()
			#print("id "+o.pk.__str__())
			#print(o.save())
			#print("afet save " +oggetto.prezzo_attuale.__str__()+" "+o.oggetto.prezzo_attuale.__str__())
			#print("kkkk "+o.oggetto.nome.__str__()+" "+o.oggetto.pk.__str__()+" "+o.oggetto.prezzo_attuale.__str__())
			return o
		except Exception as e:
			return Offerta.objects.create(oggetto=oggetto,utente=utente,prezzo_massimo=prezzo_massimo,data=data)
	def save(self, *args, **kwargs):
		ret=self.oggetto.add_offerta(self)
		super(Offerta, self).save(*args, **kwargs)
		return ret

