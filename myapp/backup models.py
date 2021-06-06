from django.db import models

class Datas(models.Model):
	nama = models.CharField(max_length=100, blank=True, null=True)
	nim = models.CharField(max_length=30, blank=True, null=True)
	jk = models.CharField(max_length=50)
	ipk = models.FloatField()
	ipk_prodi = models.FloatField(blank=True, null=True)
	p_cuti = models.CharField(max_length=30)
	sam_bekerja = models.CharField(max_length=30)
	a_papua	= models.CharField(max_length=30)
	p_mengulang = models.CharField(max_length=30)
	ipk1 = models.FloatField(blank=True, null=True)
	ipk2 = models.FloatField(blank=True, null=True)
	ipk3 = models.FloatField(blank=True, null=True)
	ipk4 = models.FloatField(blank=True, null=True)
	ipk5 = models.FloatField(blank=True, null=True)
	ipk6 = models.FloatField(blank=True, null=True)
	prediksi = models.CharField(max_length=30, blank=True, null=True)


	def __str__(self):
		return self.nama