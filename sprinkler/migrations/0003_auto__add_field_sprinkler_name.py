# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sprinkler.name'
        db.add_column(u'sprinkler_sprinkler', 'name',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sprinkler.name'
        db.delete_column(u'sprinkler_sprinkler', 'name')


    models = {
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'countryCode': ('django.db.models.fields.TextField', [], {}),
            'currencyCode': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'textRate': ('django.db.models.fields.FloatField', [], {})
        },
        u'sprinkler.sprinkler': {
            'Meta': {'object_name': 'Sprinkler'},
            'heartbeat': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipAddress': ('django.db.models.fields.TextField', [], {}),
            'load': ('django.db.models.fields.FloatField', [], {}),
            'localIpAddress': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sprinklerCountry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"})
        }
    }

    complete_apps = ['sprinkler']