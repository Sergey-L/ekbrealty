# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('website_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('common.fields.MultiEmailField')(max_length=255)),
        ))
        db.send_create_signal('website', ['Settings'])

        # Adding model 'Region'
        db.create_table('website_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('website', ['Region'])

        # Adding model 'Area'
        db.create_table('website_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Region'])),
        ))
        db.send_create_signal('website', ['Area'])

        # Adding model 'DealType'
        db.create_table('website_dealtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('website', ['DealType'])

        # Adding model 'RealtyType'
        db.create_table('website_realtytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('website', ['RealtyType'])

        # Adding model 'Realty'
        db.create_table('website_realty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Region'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Area'])),
            ('realty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.RealtyType'])),
            ('deal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.DealType'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sq', self.gf('django.db.models.fields.FloatField')()),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Realty'])

        # Adding model 'Profile'
        db.create_table('website_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('scype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('website', ['Profile'])

        # Adding model 'Slot'
        db.create_table('website_slot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('cab_show', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('website', ['Slot'])

        # Adding model 'Banner'
        db.create_table('website_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal('website', ['Banner'])

        # Adding M2M table for field slots on 'Banner'
        db.create_table('website_banner_slots', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('banner', models.ForeignKey(orm['website.banner'], null=False)),
            ('slot', models.ForeignKey(orm['website.slot'], null=False))
        ))
        db.create_unique('website_banner_slots', ['banner_id', 'slot_id'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('website_settings')

        # Deleting model 'Region'
        db.delete_table('website_region')

        # Deleting model 'Area'
        db.delete_table('website_area')

        # Deleting model 'DealType'
        db.delete_table('website_dealtype')

        # Deleting model 'RealtyType'
        db.delete_table('website_realtytype')

        # Deleting model 'Realty'
        db.delete_table('website_realty')

        # Deleting model 'Profile'
        db.delete_table('website_profile')

        # Deleting model 'Slot'
        db.delete_table('website_slot')

        # Deleting model 'Banner'
        db.delete_table('website_banner')

        # Removing M2M table for field slots on 'Banner'
        db.delete_table('website_banner_slots')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.gallery': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Gallery'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'website.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Region']"})
        },
        'website.banner': {
            'Meta': {'object_name': 'Banner'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slots': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Slot']", 'symmetrical': 'False'})
        },
        'website.dealtype': {
            'Meta': {'object_name': 'DealType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.profile': {
            'Meta': {'object_name': 'Profile'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'website.realty': {
            'Meta': {'object_name': 'Realty'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Area']"}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.DealType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'realty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.RealtyType']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Region']"}),
            'sp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sq': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'website.realtytype': {
            'Meta': {'object_name': 'RealtyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.settings': {
            'Meta': {'object_name': 'Settings'},
            'email': ('common.fields.MultiEmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.slot': {
            'Meta': {'object_name': 'Slot'},
            'cab_show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['website']
