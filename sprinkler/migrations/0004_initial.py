# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sprinkler'
        db.create_table(u'sprinkler_sprinkler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('ipAddress', self.gf('django.db.models.fields.TextField')()),
            ('localIpAddress', self.gf('django.db.models.fields.TextField')()),
            ('heartbeat', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('load', self.gf('django.db.models.fields.FloatField')()),
            ('sprinklerCountry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['country.Country'])),
        ))
        db.send_create_signal(u'sprinkler', ['Sprinkler'])


    def backwards(self, orm):
        # Deleting model 'Sprinkler'
        db.delete_table(u'sprinkler_sprinkler')


    models = {
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'countryCode': ('django.db.models.fields.TextField', [], {}),
            'currencyCode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'textRate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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