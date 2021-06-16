from django.db import models

class DataSiswa(models.Model):
	nama_siswa = models.CharField(max_length=100, blank=True, null=True)
	jenis_kelamin = models.CharField(max_length=30, blank=True, null=True)
	tinggi_badan = models.IntegerField(null=True)
	berat_badan = models.IntegerField(null=True)
	
	kemampuan_fisik_lari = models.IntegerField(null=True)
	teknik_dasar_lari = models.IntegerField(null=True)

	kemampuan_fisik_voli = models.IntegerField(null=True)
	teknik_dasar_voli = models.IntegerField(null=True)

	kemampuan_fisik_renang = models.IntegerField(null=True)
	teknik_dasar_renang = models.IntegerField(null=True)

	kemampuan_fisik_bulu_tangkis = models.IntegerField(null=True)
	teknik_dasar_bulu_tangkis = models.IntegerField(null=True)

	kemampuan_fisik_sepak_bola = models.IntegerField(null=True)
	teknik_dasar_sepak_bola = models.IntegerField(null=True)

	kemampuan_fisik_tenis_meja = models.IntegerField(null=True)
	teknik_dasar_tenis_meja = models.IntegerField(null=True)

	kemampuan_fisik_tolak_peluru = models.IntegerField(null=True)
	teknik_dasar_tolak_peluru = models.IntegerField(null=True)

	def __str__(self):
		return self.nama_siswa

class Datas(models.Model):
	nama_siswa = models.CharField(max_length=100, blank=True, null=True)
	jenis_kelamin = models.CharField(max_length=30, blank=True, null=True)
	tinggi_badan = models.IntegerField(null=True)
	berat_badan = models.IntegerField(null=True)
	
	kemampuan_fisik_lari = models.IntegerField(null=True)
	teknik_dasar_lari = models.IntegerField(null=True)
	hasil_bakat_lari = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_voli = models.IntegerField(null=True)
	teknik_dasar_voli = models.IntegerField(null=True)
	hasil_bakat_voli = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_renang = models.IntegerField(null=True)
	teknik_dasar_renang = models.IntegerField(null=True)
	hasil_bakat_renang = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_bulu_tangkis = models.IntegerField(null=True)
	teknik_dasar_bulu_tangkis = models.IntegerField(null=True)
	hasil_bakat_bulu_tangkis = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_sepak_bola = models.IntegerField(null=True)
	teknik_dasar_sepak_bola = models.IntegerField(null=True)
	hasil_bakat_sepak_bola = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_tenis_meja = models.IntegerField(null=True)
	teknik_dasar_tenis_meja = models.IntegerField(null=True)
	hasil_bakat_tenis_meja = models.CharField(max_length=30, blank=True, null=True)

	kemampuan_fisik_tolak_peluru = models.IntegerField(null=True)
	teknik_dasar_tolak_peluru = models.IntegerField(null=True)
	hasil_bakat_tolak_peluru = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return self.nama_siswa