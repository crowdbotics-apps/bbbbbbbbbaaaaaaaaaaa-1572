# Generated by Django 2.2.9 on 2020-02-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testAna001', models.BigIntegerField()),
                ('testAna002', models.BigIntegerField()),
            ],
        ),
    ]
