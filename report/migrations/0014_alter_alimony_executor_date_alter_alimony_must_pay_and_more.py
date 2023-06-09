# Generated by Django 4.2 on 2023-05-14 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_alter_mustpayreceipt_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimony',
            name='executor_date',
            field=models.DateTimeField(verbose_name='Önumciligiň senesi:'),
        ),
        migrations.AlterField(
            model_name='alimony',
            name='must_pay',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.mustpay', verbose_name='Bergidaryň ady we familiýasy:'),
        ),
        migrations.AlterField(
            model_name='alimony',
            name='recipient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.recipient', verbose_name='Algydaryn ady we familiyasy:'),
        ),
        migrations.AlterField(
            model_name='alimony',
            name='ruling_scan',
            field=models.FileField(blank=True, null=True, upload_to='alimony files/', verbose_name='Kararyň nusgasy:'),
        ),
        migrations.AlterField(
            model_name='mustpay',
            name='document_scan',
            field=models.FileField(blank=True, null=True, upload_to='must pay files/', verbose_name='Passport nusgasy:'),
        ),
        migrations.AlterField(
            model_name='mustpayreceipt',
            name='document_scan',
            field=models.FileField(blank=True, null=True, upload_to='must pay receipt files/', verbose_name='Tölegi tassyklaýan resminama:'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='document_scan',
            field=models.FileField(blank=True, null=True, upload_to='recipient files/', verbose_name='Passport nusgasy:'),
        ),
        migrations.AlterField(
            model_name='recipientchild',
            name='document_scan',
            field=models.FileField(blank=True, null=True, upload_to='recipient child files/', verbose_name='Şahadatnama nusgasy'),
        ),
    ]
