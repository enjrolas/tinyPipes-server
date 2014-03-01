# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pipe.billingPeriod'
        db.delete_column(u'pipe_pipe', 'billingPeriod')


        # Changing field 'Pipe.serialNumber'
        db.alter_column(u'pipe_pipe', 'serialNumber', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Pipe.billingPeriod'
        db.add_column(u'pipe_pipe', 'billingPeriod',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Pipe.serialNumber'
        db.alter_column(u'pipe_pipe', 'serialNumber', self.gf('django.db.models.fields.IntegerField')())

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
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'enabled'", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.TextField', [], {'default': "'v2.3'"})
        },
        u'sprinkler.sprinkler': {
            'Meta': {'object_name': 'Sprinkler'},
            'heartbeat': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipAddress': ('django.db.models.fields.TextField', [], {}),
            'load': ('django.db.models.fields.FloatField', [], {}),
            'localIpAddress': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'sprinklerCountry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"})
        }
    }

    complete_apps = ['pipe']