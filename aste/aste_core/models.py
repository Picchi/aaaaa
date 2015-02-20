from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Utente(models.Model):
#	username=models.CharField(max_length=20)
#	nome=models.CharField(max_length=50)
#	cognome=models.CharField(max_length=50)
	indirizzo=models.CharField(max_length=150)
	ref=models.ForeignKey(User,related_name="ref")




class Categoria(models.Model):
	nome=models.CharField(max_length=50)

		

class Oggetto(models.Model):
	nome=models.CharField(max_length=50)
	data_pubblicazione=models.DateTimeField(auto_now_add=True)
	descrizione=models.TextField()
	data_termine=models.DateTimeField('data di fine asta')
	prezzo_partenza=models.FloatField()
	prezzo_attuale=models.FloatField()
	prezzo_compra_subito=models.FloatField()
	categoria=models.ForeignKey(Categoria,related_name="oggetti")
	utente=models.ForeignKey(Utente,related_name="oggetti")
	utente_vincente=models.ForeignKey(Utente,related_name="vincente")



class Offerta(models.Model):
	ogetto=models.ForeignKey(Oggetto,related_name="attuale_vincitore")
	utente=models.ForeignKey(User,related_name="offerte")
	prezzo_massimo=models.FloatField()
