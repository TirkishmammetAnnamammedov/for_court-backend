# Generated by Django 4.2 on 2023-05-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_alter_mustpay_name_and_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mustpay',
            name='document_scan',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Passport nusgasy'),
        ),
    ]