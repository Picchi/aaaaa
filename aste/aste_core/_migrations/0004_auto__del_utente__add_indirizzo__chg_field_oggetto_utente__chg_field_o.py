# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Utente'
        db.delete_table('aste_core_utente')

        # Adding model 'Indirizzo'
        db.create_table('aste_core_indirizzo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('via', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('citta', self.gf('django.db.models.fields.CharField')(max_length=150, default=None)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=150, default=None)),
            ('cap', self.gf('django.db.models.fields.CharField')(max_length=6, default=None)),
            ('ref', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='ref')),
        ))
        db.send_create_signal('aste_core', ['Indirizzo'])


        # Changing field 'Oggetto.utente'
        db.alter_column('aste_core_oggetto', 'utente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Oggetto.utente_vincente'
        db.alter_column('aste_core_oggetto', 'utente_vincente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Adding model 'Utente'
        db.create_table('aste_core_utente', (
            ('citta', self.gf('django.db.models.fields.CharField')(max_length=150, default=None)),
            ('cap', self.gf('django.db.models.fields.CharField')(max_length=6, default=None)),
            ('indirizzo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=150, default=None)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ref', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='ref')),
        ))
        db.send_create_signal('aste_core', ['Utente'])

        # Deleting model 'Indirizzo'
        db.delete_table('aste_core_indirizzo')


        # Changing field 'Oggetto.utente'
        db.alter_column('aste_core_oggetto', 'utente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aste_core.Utente']))

        # Changing field 'Oggetto.utente_vincente'
        db.alter_column('aste_core_oggetto', 'utente_vincente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aste_core.Utente']))

    models = {
        'aste_core.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aste_core.indirizzo': {
            'Meta': {'object_name': 'Indirizzo'},
            'cap': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': 'None'}),
            'citta': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': 'None'}),
            'ref': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'ref'"}),
            'via': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'aste_core.offerta': {
            'Meta': {'object_name': 'Offerta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ogetto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aste_core.Oggetto']", 'related_name': "'attuale_vincitore'"}),
            'prezzo_massimo': ('django.db.models.fields.FloatField', [], {}),
            'utente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'offerte'"})
        },
        'aste_core.oggetto': {
            'Meta': {'object_name': 'Oggetto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aste_core.Categoria']", 'related_name': "'oggetti'"}),
            'data_pubblicazione': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'data_termine': ('django.db.models.fields.DateTimeField', [], {}),
            'descrizione': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prezzo_attuale': ('django.db.models.fields.FloatField', [], {}),
            'prezzo_compra_subito': ('django.db.models.fields.FloatField', [], {}),
            'prezzo_partenza': ('django.db.models.fields.FloatField', [], {}),
            'utente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'oggetti'"}),
            'utente_vincente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'vincente'"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['aste_core']