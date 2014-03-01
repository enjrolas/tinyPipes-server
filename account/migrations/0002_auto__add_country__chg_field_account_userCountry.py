# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'account_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('textRate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('countryCode', self.gf('django.db.models.fields.TextField')()),
            ('currencyCode', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'account', ['Country'])


        # Changing field 'Account.userCountry'
        db.alter_column(u'account_account', 'userCountry_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Country']))

    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'account_country')


        # Changing field 'Account.userCountry'
        db.alter_column(u'account_account', 'userCountry_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['country.Country']))

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'province': ('django.db.models.fields.TextField', [], {}),
            'userCountry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Country']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'account.country': {
            'Meta': {'object_name': 'Country'},
            'countryCode': ('django.db.models.fields.TextField', [], {}),
            'currencyCode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'textRate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['account']