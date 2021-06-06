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

class Fomrdata(forms.Form):
	

    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YEAR_IN_SCHOOL_CHOICES,
    #     default=FRESHMAN,
    # )

	nama = forms.CharField(label='Nama')
	nim = forms.CharField(label='NIM')

	jk = forms.ChoiceField(
		label='Jenis Kelamin',
		# max_length=3,
		choices=PIL,
		# default=1,
	)
	ipk = forms.FloatField(label='IPK')
	ipk_prodi = forms.FloatField(label='IPK Prodi')
	p_cuti = forms.ChoiceField(choices=PILIHAN, label='Pernah Cuti')
	sam_bekerja = forms.ChoiceField(choices=PILIHAN, label='Sambil Bekerja')
	a_papua	= forms.ChoiceField(choices=PILIHAN, label='Asli Papua')
	p_mengulang = forms.ChoiceField(choices=PILIHAN, label='Pernah Mengulang')
	ipk1 = forms.FloatField(label='IPK Semester 1')
	ipk2 = forms.FloatField(label='IPK Semester 2')
	ipk3 = forms.FloatField(label='IPK Semester 3')
	ipk4 = forms.FloatField(label='IPK Semester 4')
	ipk5 = forms.FloatField(label='IPK Semester 5')
	ipk6 = forms.FloatField(label='IPK Semester 6')

	class Meta:
		model = Datas

		# widgets = {
		# 	'p_mengulang' : forms.ChoiceField(attrs={'class': 'mantap'})
		# }