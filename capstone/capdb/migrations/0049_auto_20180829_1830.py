# Generated by Django 2.0.8 on 2018-08-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0048_caseexport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casemetadata',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
