# Generated by Django 4.2 on 2023-05-14 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0014_alter_alimony_executor_date_alter_alimony_must_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimony',
            name='must_pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.mustpay', verbose_name='Bergidaryň ady we familiýasy:'),
        ),
        migrations.AlterField(
            model_name='alimony',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.recipient', verbose_name='Algydaryn ady we familiyasy:'),
        ),
    ]
