"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Offerta,Oggetto,Categoria
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class TestOgg(TestCase):
	def setUp(self):
		g=Categoria.objects.create(nome="cat prova",id=1)
		v=User.objects.create(username="V")
		Oggetto.objects.create(nome="prova",prezzo_partenza=50,prezzo_attuale=0,data_termine=timezone.now() + datetime.timedelta(days=30),
			categoria=g,utente=v,utente_vincente=v)
		User.objects.create(username="1")
		User.objects.create(username="2")
		User.objects.create(username="3")

	def test_correct_update(self):
		ogg=Oggetto.objects.get(id=1)
		u1=User.objects.get(username="1")
		u2=User.objects.get(username="2")
		u3=User.objects.get(username="3")
		#of1=Offerta.objects.create(oggetto=ogg,utente=u1,prezzo_massimo=75)
		of1=Offerta.CreateOfferta(oggetto=ogg,utente=u1,prezzo_massimo=75)
		#print(ogg.add_offerta(of1))
		self.assertEqual(ogg.utente_vincente,u1)
		self.assertEqual(ogg.prezzo_attuale,50)
		#of2=Offerta.objects.create(oggetto=ogg,utente=u2,prezzo_massimo=75)
		of2=Offerta.CreateOfferta(oggetto=ogg,utente=u2,prezzo_massimo=74)
		ogg=Oggetto.objects.get(id=1)
		self.assertEqual(ogg.utente_vincente,u1)
		self.assertEqual(ogg.prezzo_attuale,74.05)
		#of3=Offerta.objects.create(oggetto=ogg,utente=u2,prezzo_massimo=80)


		of3=Offerta.CreateOfferta(oggetto=ogg,utente=u2,prezzo_massimo=80)
		ogg=Oggetto.objects.get(id=1)

		self.assertEqual(ogg.prezzo_attuale,75.05)
		self.assertEqual(ogg.utente_vincente,u2)
		of4=Offerta.CreateOfferta(oggetto=ogg,utente=u2,prezzo_massimo=90)
		ogg=Oggetto.objects.get(id=1)

		self.assertEqual(ogg.prezzo_attuale,75.05)
		self.assertEqual(Offerta.objects.get(oggetto=ogg.id,utente=ogg.utente_vincente.id).pk,of4.pk)
		self.assertEqual(Offerta.objects.get(oggetto=ogg.id,utente=ogg.utente_vincente.id).prezzo_massimo,90)
		self.assertEqual(ogg.utente_vincente,u2)



		#of=sorted(sorted(Offerta.objects.filter(oggetto=og.id),key=lambda obj:obj.data,reverse=true),key=lambda obj=obj.prezzo_massimo)[-2:]
		#if of.__len__()==1:
		#	self.prezzo_attuale=self.prezzo_partenza
		#	self.utente_vincente=of.utente
		#	return 
		#self.prezzo_attuale=of[1].prezzo_massimo-((of[1].prezzo_massimo-of[0].prezzo_massimo-RILANCIO_MINIMO) if of[1].prezzo_massimo!=of[0].prezzo_massimo else 0 )
		#self.utente_vincente=of.utente
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
