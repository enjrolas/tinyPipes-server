# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Measurement'
        db.create_table(u'demo_measurement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'demo', ['Measurement'])


    def backwards(self, orm):
        # Deleting model 'Measurement'
        db.delete_table(u'demo_measurement')


    models = {
        u'demo.measurement': {
            'Meta': {'object_name': 'Measurement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']