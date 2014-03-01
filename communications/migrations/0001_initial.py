# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Squirt'
        db.create_table(u'communications_squirt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinkler.Sprinkler'])),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('messageType', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'communications', ['Squirt'])

        # Adding model 'Spray'
        db.create_table(u'communications_spray', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinkler.Sprinkler'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('messageType', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'communications', ['Spray'])

        # Adding model 'Load'
        db.create_table(u'communications_load', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('sprinkler', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foreign sprinkler', to=orm['sprinkler.Sprinkler'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pipe.Pipe'])),
            ('fromPhone', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'communications', ['Load'])


    def backwards(self, orm):
        # Deleting model 'Squirt'
        db.delete_table(u'communications_squirt')

        # Deleting model 'Spray'
        db.delete_table(u'communications_spray')

        # Deleting model 'Load'
        db.delete_table(u'communications_load')


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
        u'communications.load': {
            'Meta': {'object_name': 'Load'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            'fromPhone': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'foreign sprinkler'", 'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'communications.spray': {
            'Meta': {'object_name': 'Spray'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageType': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'communications.squirt': {
            'Meta': {'object_name': 'Squirt'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageType': ('django.db.models.fields.TextField', [], {}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pipe.Pipe']"}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'billingPeriod': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'billingRate': ('django.db.models.fields.FloatField', [], {'default': '15', 'null': 'True', 'blank': 'True'}),
            'billingType': ('django.db.models.fields.TextField', [], {'default': "'daily'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattitude': ('django.db.models.fields.FloatField', [], {'default': "'14.56'", 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': "'120.99'", 'null': 'True', 'blank': 'True'}),
            'panelHealth': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'phoneNumber': ('django.db.models.fields.TextField', [], {'default': "'+8613632651167'", 'null': 'True', 'blank': 'True'}),
            'pipeLoad': ('django.db.models.fields.FloatField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'serialNumber': ('django.db.models.fields.IntegerField', [], {}),
            'sprinkler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sprinkler.Sprinkler']"}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'enabled'", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.TextField', [], {})
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

    complete_apps = ['communications']