# Generated by Django 3.1.4 on 2020-12-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20201213_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'موارد کاربرد', 'verbose_name_plural': 'موارد کاربرد'},
        ),
        migrations.AlterField(
            model_name='material',
            name='product',
            field=models.ManyToManyField(to='App.Product', verbose_name='موارد کاربرد '),
        ),
    ]
