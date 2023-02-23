# Generated by Django 4.1.6 on 2023-02-12 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_products_related_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='type_id',
        ),
        migrations.AddField(
            model_name='products',
            name='type_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='productData', to='api.food'),
            preserve_default=False,
        ),
    ]
