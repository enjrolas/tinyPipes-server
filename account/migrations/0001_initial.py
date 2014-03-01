# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'account_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userCountry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['country.Country'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('province', self.gf('django.db.models.fields.TextField')()),
            ('phoneNumber', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'account', ['Account'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'account_account')


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
        }
    }

    complete_apps = ['account']