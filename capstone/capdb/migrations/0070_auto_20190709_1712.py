# Generated by Django 2.2.2 on 2019-07-09 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0069_volumemetadata_last_es_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngramobservation',
            name='jurisdiction',
        ),
        migrations.RemoveField(
            model_name='ngramobservation',
            name='ngram',
        ),
        migrations.DeleteModel(
            name='Ngram',
        ),
        migrations.DeleteModel(
            name='NgramObservation',
        ),
        migrations.DeleteModel(
            name='NgramWord',
        ),
    ]
