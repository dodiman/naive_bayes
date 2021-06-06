from django.db import models

class Datas(models.Model):
	nama_siswa = models.CharField(max_length=100, blank=True, null=True)
	jenis_kelamin = models.CharField(max_length=30, blank=True, null=True)
	tinggi_badan = models.IntegerField(null=True)
	berat_badan = models.IntegerField(null=True)
	kemampuan_fisik = models.IntegerField(null=True)
	teknik_dasar = models.IntegerField(null=True)
	hasil_bakat = models.CharField(max_length=30, blank=True, null=True)
	
	def __str__(self):
		return self.nama_siswa