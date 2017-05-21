# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heritages', '0003_auto_20170511_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField(default='http://www.w3.org/ns/anno.jsonld')),
                ('annotation_id', models.URLField(default='http://574heritago.com/annotations/null/', max_length=255)),
                ('type', models.CharField(default='Annotation', max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('heritage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='heritages.Heritage')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('video', 'video'), ('audio', 'audio'), ('image', 'image'), ('location', 'location'), ('text', 'text')], max_length=10)),
                ('format', models.CharField(choices=[('text/plain', 'text/plain'), ('video/mpeg', 'video/mpeg'), ('video/avi', 'video/avi'), ('image/png', 'image/png'), ('image/bmp', 'image/bmp'), ('image/gif', 'image/gif'), ('image/jpeg', 'image/jpeg'), ('audio/midi', 'audio/midi'), ('audio/mpeg', 'audio/mpeg')], max_length=15)),
                ('value', models.CharField(max_length=255)),
                ('annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body', to='heritages.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.CharField(default='http://574heritago.com/heritages/null/', max_length=255)),
                ('type', models.CharField(choices=[('video', 'video'), ('audio', 'audio'), ('image', 'image'), ('location', 'location'), ('text', 'text')], max_length=10)),
                ('format', models.CharField(choices=[('text/plain', 'text/plain'), ('video/mpeg', 'video/mpeg'), ('video/avi', 'video/avi'), ('image/png', 'image/png'), ('image/bmp', 'image/bmp'), ('image/gif', 'image/gif'), ('image/jpeg', 'image/jpeg'), ('audio/midi', 'audio/midi'), ('audio/mpeg', 'audio/mpeg')], max_length=15)),
                ('annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotationTarget', to='heritages.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='Selector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='FragmentSelector', max_length=25)),
                ('conformsTo', models.CharField(choices=[('http://tools.ietf.org/rfc/rfc5147', 'http://tools.ietf.org/rfc/rfc5147'), ('http://www.w3.org/TR/media-frags/', 'http://www.w3.org/TR/media-frags/'), ('http://www.w3.org/TR/SVG/', 'http://www.w3.org/TR/SVG/')], max_length=50)),
                ('value', models.CharField(max_length=255)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selector', to='heritages.AnnotationTarget')),
            ],
        ),
    ]
