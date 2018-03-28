# Generated by Django 2.0.3 on 2018-03-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('email1', models.EmailField(max_length=254)),
                ('contact1', models.CharField(max_length=10)),
                ('member2', models.CharField(max_length=50)),
                ('email2', models.EmailField(max_length=254)),
                ('contact2', models.CharField(max_length=10)),
                ('member3', models.CharField(max_length=50)),
                ('email3', models.EmailField(max_length=254)),
                ('contact3', models.CharField(max_length=10)),
            ],
        ),
    ]