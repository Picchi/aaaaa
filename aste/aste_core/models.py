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

		


class Oggetto(models.Model):
	nome=models.CharField(max_length=50)
	data_pubblicazione=models.DateTimeField(auto_now_add=True)
	STATO_OGGETTO=((1,'IN CORSO'),(2,'SCADUTA')) 
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

	def add_offerta(self,new_off):
		if new_off.utente.id==self.utente_vincente.id:
			return (0,"Miglior offerte")
		if new_off.prezzo_massimo <= self.prezzo_attuale :
			#raise OffertaExcpetion("Offerta Troppo bassa")
			return (-1,"Offerta troppo bassa")
		if self.prezzo_attuale == 0  :
			self.prezzo_attuale=self.prezzo_partenza
			self.utente_vincente=new_off.utente
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
	prezzo_massimo=models.FloatField()

	@classmethod
	def CreateOfferta(cls,oggetto=None,utente=None,prezzo_massimo=None,data=None):
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
		super(Offerta, self).save(*args, **kwargs)
		ret=self.oggetto.add_offerta(self)
		return ret

