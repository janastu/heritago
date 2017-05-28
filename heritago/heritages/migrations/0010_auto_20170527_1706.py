# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heritages', '0009_merge_20170522_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='annotation_id',
        ),
        migrations.AddField(
            model_name='annotation',
            name='motivation',
            field=models.CharField(choices=[('assessing', 'assessing'),
                                            ('bookmarking', 'bookmarking'),
                                            ('classifying', 'classifying'),
                                            ('commenting', 'commenting'),
                                            ('describing', 'describing'),
                                            ('editing', 'editing'),
                                            ('highlighting', 'highlighting'),
                                            ('identifying', 'highlighting'),
                                            ('linking', 'linking'),
                                            ('moderating', 'moderating'),
                                            ('questioning', 'questioning'),
                                            ('replying', 'replying'),
                                            ('tagging', 'tagging')],
                                   max_length=20,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='heritage',
            field=models.ForeignKey(blank=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='annotation',
                                    to='heritages.Heritage'),
        ),
        migrations.AlterField(
            model_name='annotationtarget',
            name='annotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='target',
                                    to='heritages.Annotation'),
        ),
        migrations.AlterField(
            model_name='heritage',
            name='tags',
            field=models.ManyToManyField(related_name='tags',
                                         to='heritages.Tag'),
        ),
    ]