# Generated by Django 3.1.2 on 2020-10-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jk', models.CharField(max_length=50)),
                ('p_mengulang', models.CharField(max_length=30)),
                ('ipk', models.FloatField()),
                ('p_cuti', models.CharField(max_length=30)),
                ('sam_bekerja', models.CharField(max_length=30)),
                ('a_papua', models.CharField(max_length=30)),
                ('ipk_sm1', models.FloatField()),
            ],
        ),
    ]