# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Measurement.enabled'
        db.add_column(u'demo_measurement', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Measurement.enabled'
        db.delete_column(u'demo_measurement', 'enabled')


    models = {
        u'demo.demopanel': {
            'Meta': {'object_name': 'DemoPanel'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'demo.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'current': ('django.db.models.fields.FloatField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['demo']