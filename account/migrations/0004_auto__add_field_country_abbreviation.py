# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.abbreviation'
        db.add_column(u'account_country', 'abbreviation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.abbreviation'
        db.delete_column(u'account_country', 'abbreviation')


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
        }
    }

    complete_apps = ['account']