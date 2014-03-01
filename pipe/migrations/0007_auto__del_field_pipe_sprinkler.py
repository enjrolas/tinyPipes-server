# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pipe.sprinkler'
        db.delete_column(u'pipe_pipe', 'sprinkler_id')


    def backwards(self, orm):
        # Adding field 'Pipe.sprinkler'
        db.add_column(u'pipe_pipe', 'sprinkler',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sprinkler.Sprinkler']),
                      keep_default=False)


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'province': ('django.db.models.fields.TextField', [], {}),
            'userCountry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'countryCode': ('django.db.models.fields.TextField', [], {}),
            'currencyCode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'textRate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pipe.pipe': {
            'Meta': {'object_name': 'Pipe'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'batteryCapacity': ('django.db.models.fields.IntegerField', [], {'default': '720', 'null': 'True', 'blank': 'True'}),
            'batteryHealth': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'billingRate': ('django.db.models.fields.FloatField', [], {'default': '15', 'null': 'True', 'blank': 'True'}),
            'billingType': ('django.db.models.fields.TextField', [], {'default': "'daily'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattitude': ('django.db.models.fields.FloatField', [], {'default': "'14.56'", 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': "'120.99'", 'null': 'True', 'blank': 'True'}),
            'panelHealth': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'pipeLoad': ('django.db.models.fields.FloatField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'serialNumber': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'enabled'", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.TextField', [], {'default': "'v2.3'", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pipe']