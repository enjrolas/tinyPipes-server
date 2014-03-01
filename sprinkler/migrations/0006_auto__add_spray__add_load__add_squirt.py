# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Spray'
        db.create_table(u'sprinkler_spray', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinkler.Sprinkler'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('messageType', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sprinkler', ['Spray'])

        # Adding model 'Load'
        db.create_table(u'sprinkler_load', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('loadPIN', self.gf('django.db.models.fields.TextField')()),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foreign sprinkler', to=orm['sprinkler.Sprinkler'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=100)),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sprinkler', ['Load'])

        # Adding model 'Squirt'
        db.create_table(u'sprinkler_squirt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinkler.Sprinkler'])),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('messageType', self.gf('django.db.models.fields.TextField')()),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sprinkler', ['Squirt'])


    def backwards(self, orm):
        # Deleting model 'Spray'
        db.delete_table(u'sprinkler_spray')

        # Deleting model 'Load'
        db.delete_table(u'sprinkler_load')

        # Deleting model 'Squirt'
        db.delete_table(u'sprinkler_squirt')


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
            'heartbeat': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipAddress': ('django.db.models.fields.TextField', [], {}),
            'load': ('django.db.models.fields.FloatField', [], {}),
            'localIpAddress': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {}),
            'sprinklerCountry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"})
        },
        u'sprinkler.squirt': {
            'Meta': {'object_name': 'Squirt'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageType': ('django.db.models.fields.TextField', [], {}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sprinkler']