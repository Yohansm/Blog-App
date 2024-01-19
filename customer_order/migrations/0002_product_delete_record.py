# Generated by Django 4.2 on 2023-12-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('customer_email', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
