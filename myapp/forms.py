from django import forms
from .models import Datas

# pilihan
PIL = [
    (0, 'Perempuan'),
    (1, 'Laki - Laki'),
]

PILIHAN = [
    (1, 'Ya'),
    (0, 'Tidak'),
]

PILIHAN_ANGKA = [
    (60, '60'),
    (65, '65'),
    (70, '70'),
    (75, '75'),
    (80, '80'),
    (85, '85'),
    (90, '90'),
    (95, '95'),
]


class Fomrdata(forms.Form):
	

    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YEAR_IN_SCHOOL_CHOICES,
    #     default=FRESHMAN,
    # )

	nama_siswa = forms.CharField(label='Nama Siswa')
	# nim = forms.CharField(label='NIM')

	jenis_kelamin = forms.ChoiceField(
		label='Jenis Kelamin',
		# max_length=3,
		choices=PIL,
		# default=1,
	)



	nama_siswa = forms.CharField(max_length=100)
	tinggi_badan = forms.IntegerField()
	berat_badan = forms.IntegerField()
	
	kemampuan_fisik_lari = forms.ChoiceField(label='Kemampuan Fisik Lari ', choices=PILIHAN_ANGKA)
	# kemampuan_fisik_lari = forms.IntegerField()
	teknik_dasar_lari = forms.ChoiceField(label='Teknik Dasar Lari ', choices=PILIHAN_ANGKA)

	# kemampuan_fisik_voli = forms.ChoiceField(label='Kemampuan Fisik Lari ', choices=PILIHAN_ANGKA)
	kemampuan_fisik_voli = forms.ChoiceField(label='Kemampuan Fisik Voli ', choices=PILIHAN_ANGKA)
	teknik_dasar_voli = forms.ChoiceField(label='Teknik Dasar Voli ', choices=PILIHAN_ANGKA)

	kemampuan_fisik_renang = forms.ChoiceField(label='Kemampuan Fisik Renang ', choices=PILIHAN_ANGKA)
	teknik_dasar_renang = forms.ChoiceField(label='Teknik Dasar Renang ', choices=PILIHAN_ANGKA)

	kemampuan_fisik_bulu_tangkis = forms.ChoiceField(label='Kemampuan Fisik Bulu Tangkis ', choices=PILIHAN_ANGKA)
	teknik_dasar_bulu_tangkis = forms.ChoiceField(label='Teknik Dasar Bulu Tangkis ', choices=PILIHAN_ANGKA)

	kemampuan_fisik_sepak_bola = forms.ChoiceField(label='Kemampuan Fisik Sepak Bola ', choices=PILIHAN_ANGKA)
	teknik_dasar_sepak_bola = forms.ChoiceField(label='Teknik Dasar Sepak Bola ', choices=PILIHAN_ANGKA)

	kemampuan_fisik_tenis_meja = forms.ChoiceField(label='Kemampuan Fisik Tenis Meja ', choices=PILIHAN_ANGKA)
	teknik_dasar_tenis_meja = forms.ChoiceField(label='Teknik Dasar Tenis Meja ', choices=PILIHAN_ANGKA)

	kemampuan_fisik_tolak_peluru = forms.ChoiceField(label='Kemampuan Fisik Tolak Peluru ', choices=PILIHAN_ANGKA)
	teknik_dasar_tolak_peluru = forms.ChoiceField(label='Teknik Dasar Tolak Peluru ', choices=PILIHAN_ANGKA)

	class Meta:
		model = Datas

		# widgets = {
		# 	'p_mengulang' : forms.ChoiceField(attrs={'class': 'mantap'})
		# }