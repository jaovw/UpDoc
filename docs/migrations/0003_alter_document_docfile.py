# Generated by Django 3.2.1 on 2021-05-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_alter_document_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='realizado em 2021-05-06 08:12:44.865623'),
        ),
    ]
