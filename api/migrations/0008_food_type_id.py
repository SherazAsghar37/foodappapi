# Generated by Django 4.1.6 on 2023-02-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_type_id_products_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
