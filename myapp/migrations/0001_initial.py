# Generated by Django 3.1.2 on 2020-12-20 08:40

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
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('nim', models.CharField(blank=True, max_length=30, null=True)),
                ('jk', models.CharField(max_length=50)),
                ('ipk', models.FloatField()),
                ('ipk_prodi', models.FloatField(blank=True, null=True)),
                ('p_cuti', models.CharField(max_length=30)),
                ('sam_bekerja', models.CharField(max_length=30)),
                ('a_papua', models.CharField(max_length=30)),
                ('p_mengulang', models.CharField(max_length=30)),
                ('ipk1', models.FloatField(blank=True, null=True)),
                ('ipk2', models.FloatField(blank=True, null=True)),
                ('ipk3', models.FloatField(blank=True, null=True)),
                ('ipk4', models.FloatField(blank=True, null=True)),
                ('ipk5', models.FloatField(blank=True, null=True)),
                ('ipk6', models.FloatField(blank=True, null=True)),
                ('prediksi', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
