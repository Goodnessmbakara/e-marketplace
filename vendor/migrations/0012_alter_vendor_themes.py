# Generated by Django 4.2.3 on 2023-09-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_alter_vendor_themes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='themes',
            field=models.ManyToManyField(blank=True, to='vendor.theme'),
        ),
    ]
