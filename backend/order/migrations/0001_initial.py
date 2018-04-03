# Generated by Django 2.0.3 on 2018-04-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('verbose_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('legal_address', models.TextField()),
                ('shipment_address', models.TextField(blank=True, null=True)),
                ('bank', models.CharField(max_length=100)),
                ('swift', models.CharField(max_length=50)),
                ('account_iban', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
