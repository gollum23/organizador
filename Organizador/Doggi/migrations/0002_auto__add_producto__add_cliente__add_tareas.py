# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Producto'
        db.create_table('Doggi_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indx', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Doggi.Cliente'])),
            ('nombre', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('clave', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Doggi', ['Producto'])

        # Adding model 'Cliente'
        db.create_table('Doggi_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('CI_RIF', self.gf('django.db.models.fields.IntegerField')()),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('Doggi', ['Cliente'])

        # Adding model 'Tareas'
        db.create_table('Doggi_tareas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indx', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Doggi.Cliente'])),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('prioridad', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('Doggi', ['Tareas'])


    def backwards(self, orm):
        # Deleting model 'Producto'
        db.delete_table('Doggi_producto')

        # Deleting model 'Cliente'
        db.delete_table('Doggi_cliente')

        # Deleting model 'Tareas'
        db.delete_table('Doggi_tareas')


    models = {
        'Doggi.cliente': {
            'CI_RIF': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Cliente'},
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombre_apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {})
        },
        'Doggi.producto': {
            'Meta': {'object_name': 'Producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'clave': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Doggi.Cliente']"}),
            'nombre': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'Doggi.tareas': {
            'Meta': {'object_name': 'Tareas'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Doggi.Cliente']"}),
            'prioridad': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['Doggi']