# Generated by Django 3.1.6 on 2021-04-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0015_remove_produto_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(to='component.Produto'),
        ),
    ]
