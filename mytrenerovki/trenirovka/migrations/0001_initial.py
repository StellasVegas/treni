# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podhod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200)),
                ('povtoreniya', models.IntegerField(default=0)),
                ('ves', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'date created')),
                ('status', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PP_Podhod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pp', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PP_Yprazneniya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pp', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vid_Podhod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vid_Treni',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='podhod',
            name='pp_podhoda',
            field=models.ForeignKey(to='trenirovka.PP_Podhod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='podhod',
            name='pp_yprazneniya',
            field=models.ForeignKey(to='trenirovka.PP_Yprazneniya'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='podhod',
            name='vid_podhoda',
            field=models.ForeignKey(to='trenirovka.Vid_Podhod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='podhod',
            name='vid_treni',
            field=models.ForeignKey(to='trenirovka.Vid_Treni'),
            preserve_default=True,
        ),
    ]
