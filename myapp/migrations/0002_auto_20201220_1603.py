# Generated by Django 3.1.2 on 2020-12-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datas',
            old_name='nim',
            new_name='hasil_bakat',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='prediksi',
            new_name='jenis_kelamin',
        ),
        migrations.RenameField(
            model_name='datas',
            old_name='nama',
            new_name='nama_siswa',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='a_papua',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk1',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk2',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk3',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk4',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk5',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk6',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='ipk_prodi',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='jk',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='p_cuti',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='p_mengulang',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='sam_bekerja',
        ),
        migrations.AddField(
            model_name='datas',
            name='berat_badan',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='datas',
            name='kemampuan_fisik',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='datas',
            name='teknik_dasar',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='datas',
            name='tinggi_badan',
            field=models.IntegerField(null=True),
        ),
    ]
