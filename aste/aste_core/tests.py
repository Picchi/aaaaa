"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Offerta,Oggetto

class TestOgg(TestCase):
	def test_correct_update(self):
		of=sorted(sorted(Offerta.objects.filter(oggetto=og.id),key=lambda obj:obj.data,reverse=true),key=lambda obj=obj.prezzo_massimo)[-2:]
		if of.__len__()==1:
			self.prezzo_attuale=self.prezzo_partenza
			self.utente_vincente=of.utente
			return 
		self.prezzo_attuale=of[1].prezzo_massimo-((of[1].prezzo_massimo-of[0].prezzo_massimo-RILANCIO_MINIMO) if of[1].prezzo_massimo!=of[0].prezzo_massimo else 0 )
		self.utente_vincente=of.utente
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
