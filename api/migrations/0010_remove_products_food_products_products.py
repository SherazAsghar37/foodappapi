# Generated by Django 4.1.6 on 2023-02-15 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_products_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='food',
        ),
        migrations.AddField(
            model_name='products',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.food'),
            preserve_default=False,
        ),
    ]
