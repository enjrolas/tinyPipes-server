# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sprinkler.temp'
        db.add_column(u'sprinkler_sprinkler', 'temp',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sprinkler.temp'
        db.delete_column(u'sprinkler_sprinkler', 'temp')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'province': ('django.db.models.fields.TextField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'account.country': {
            'Meta': {'object_name': 'Country'},
            'abbreviation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattitude': ('django.db.models.fields.FloatField', [], {'default': "'14.56'", 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': "'120.99'", 'null': 'True', 'blank': 'True'}),
            'panelHealth': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'pipeLoad': ('django.db.models.fields.FloatField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'serialNumber': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'enabled'", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.TextField', [], {'default': "'v2.3'", 'null': 'True', 'blank': 'True'})
        },
        u'sprinkler.load': {
            'Meta': {'object_name': 'Load'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loadPIN': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'foreign sprinkler'", 'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sprinkler.spray': {
            'Meta': {'object_name': 'Spray'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageType': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sprinkler.sprinkler': {
            'Meta': {'object_name': 'Sprinkler'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['account.Country']"}),
            'heartbeat': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'temp': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'sprinkler.squirt': {
            'Meta': {'object_name': 'Squirt'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sprinkler']