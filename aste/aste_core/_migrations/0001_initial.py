# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utente'
        db.create_table('aste_core_utente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indirizzo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('ref', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ref', to=orm['auth.User'])),
        ))
        db.send_create_signal('aste_core', ['Utente'])

        # Adding model 'Categoria'
        db.create_table('aste_core_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aste_core', ['Categoria'])

        # Adding model 'Oggetto'
        db.create_table('aste_core_oggetto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data_pubblicazione', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')()),
            ('data_termine', self.gf('django.db.models.fields.DateTimeField')()),
            ('prezzo_partenza', self.gf('django.db.models.fields.FloatField')()),
            ('prezzo_attuale', self.gf('django.db.models.fields.FloatField')()),
            ('prezzo_compra_subito', self.gf('django.db.models.fields.FloatField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oggetti', to=orm['aste_core.Categoria'])),
            ('utente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oggetti', to=orm['aste_core.Utente'])),
            ('utente_vincente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vincente', to=orm['aste_core.Utente'])),
        ))
        db.send_create_signal('aste_core', ['Oggetto'])

        # Adding model 'Offerta'
        db.create_table('aste_core_offerta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ogetto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attuale_vincitore', to=orm['aste_core.Oggetto'])),
            ('utente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offerte', to=orm['auth.User'])),
            ('prezzo_massimo', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('aste_core', ['Offerta'])


    def backwards(self, orm):
        # Deleting model 'Utente'
        db.delete_table('aste_core_utente')

        # Deleting model 'Categoria'
        db.delete_table('aste_core_categoria')

        # Deleting model 'Oggetto'
        db.delete_table('aste_core_oggetto')

        # Deleting model 'Offerta'
        db.delete_table('aste_core_offerta')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ref': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ref'", 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['aste_core']