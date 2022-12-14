# Generated by Django 2.1.1 on 2022-10-28 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item_url', models.URLField(blank=True, null=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('buy_date', models.DateField(blank=True, null=True)),
                ('buy', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shop_site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shoppinglist.Shop', verbose_name='shop'),
        ),
    ]
