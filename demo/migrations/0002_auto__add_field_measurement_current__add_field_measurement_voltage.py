# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Measurement.current'
        db.add_column(u'demo_measurement', 'current',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Measurement.voltage'
        db.add_column(u'demo_measurement', 'voltage',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Measurement.current'
        db.delete_column(u'demo_measurement', 'current')

        # Deleting field 'Measurement.voltage'
        db.delete_column(u'demo_measurement', 'voltage')


    models = {
        u'demo.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'current': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['demo']