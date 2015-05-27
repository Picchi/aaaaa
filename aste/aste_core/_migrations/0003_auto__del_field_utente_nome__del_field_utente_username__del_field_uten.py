# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Utente.nome'
        db.delete_column('aste_core_utente', 'nome')

        # Deleting field 'Utente.username'
        db.delete_column('aste_core_utente', 'username')

        # Deleting field 'Utente.cognome'
        db.delete_column('aste_core_utente', 'cognome')

        # Adding field 'Utente.citta'
        db.add_column('aste_core_utente', 'citta',
                      self.gf('django.db.models.fields.CharField')(max_length=150, default=None),
                      keep_default=False)

        # Adding field 'Utente.provincia'
        db.add_column('aste_core_utente', 'provincia',
                      self.gf('django.db.models.fields.CharField')(max_length=150, default=None),
                      keep_default=False)

        # Adding field 'Utente.cap'
        db.add_column('aste_core_utente', 'cap',
                      self.gf('django.db.models.fields.CharField')(max_length=6, default=None),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Utente.nome'
        raise RuntimeError("Cannot reverse this migration. 'Utente.nome' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Utente.nome'
        db.add_column('aste_core_utente', 'nome',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Utente.username'
        raise RuntimeError("Cannot reverse this migration. 'Utente.username' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Utente.username'
        db.add_column('aste_core_utente', 'username',
                      self.gf('django.db.models.fields.CharField')(max_length=20),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Utente.cognome'
        raise RuntimeError("Cannot reverse this migration. 'Utente.cognome' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Utente.cognome'
        db.add_column('aste_core_utente', 'cognome',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'Utente.citta'
        db.delete_column('aste_core_utente', 'citta')

        # Deleting field 'Utente.provincia'
        db.delete_column('aste_core_utente', 'provincia')

        # Deleting field 'Utente.cap'
        db.delete_column('aste_core_utente', 'cap')


    models = {
        'aste_core.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aste_core.offerta': {
            'Meta': {'object_name': 'Offerta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ogetto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attuale_vincitore'", 'to': "orm['aste_core.Oggetto']"}),
            'prezzo_massimo': ('django.db.models.fields.FloatField', [], {}),
            'utente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offerte'", 'to': "orm['auth.User']"})
        },
        'aste_core.oggetto': {
            'Meta': {'object_name': 'Oggetto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oggetti'", 'to': "orm['aste_core.Categoria']"}),
            'data_pubblicazione': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'data_termine': ('django.db.models.fields.DateTimeField', [], {}),
            'descrizione': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prezzo_attuale': ('django.db.models.fields.FloatField', [], {}),
            'prezzo_compra_subito': ('django.db.models.fields.FloatField', [], {}),
            'prezzo_partenza': ('django.db.models.fields.FloatField', [], {}),
            'utente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oggetti'", 'to': "orm['aste_core.Utente']"}),
            'utente_vincente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vincente'", 'to': "orm['aste_core.Utente']"})
        },
        'aste_core.utente': {
            'Meta': {'object_name': 'Utente'},
            'cap': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': 'None'}),
            'citta': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': 'None'}),
            'ref': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ref'", 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['aste_core']