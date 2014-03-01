# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Measurement.energy'
        db.add_column(u'demo_measurement', 'energy',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Measurement.energy'
        db.delete_column(u'demo_measurement', 'energy')


    models = {
        u'demo.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'current': ('django.db.models.fields.FloatField', [], {}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['demo']