from django.shortcuts import render, redirect
from .forms import Fomrdata

from myapp.models import Datas

import numpy as np
import pandas as pd

from pydataset import data

# # sklearn package / module
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from mixed_naive_bayes import MixedNB

# untuk import export
from import_export import resources
from .resources import DatasResources
from tablib import Dataset

from django.contrib.auth.decorators import login_required

@login_required
def datas(request):
	pesan = ''
	db = Datas.objects.all()
	if request.method == 'POST':
		file_format = request.POST['file-format']
		employee_resource = DatasResources()
		dataset = Dataset()
		new_employees = request.FILES['importData']

		# print(len(new_employees.read()))
		imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
		result = employee_resource.import_data(dataset, dry_run=True)   # datanya di test

		# if file_format == 'CSV':
		if not result.has_errors():
			employee_resource.import_data(dataset, dry_run=False)

			pesan = 'sukses'


	context = {
		'db': db,
		'pesan' : pesan,
		# 'data_resource'	: data_resource,
	}
	return render(request, 'myapp/datas.html', context)

def dashboard(request):
	db = Datas.objects.all()
	if not db:
		return redirect('datas')
	csv = pd.DataFrame(db.values())
	df = pd.DataFrame(db.values())
	csv = df.copy()

	labeling = csv.copy()
	
	
	def konvers(csv):
		csv[['jenis_kelamin']] = np.where(csv[['jenis_kelamin']] == 'perempuan', 0, 1)

		kondisi = [
		        (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] < 148),
		        (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] > 158),
		        (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] < 145), 
		        (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] > 155)
		    ]

		kondisi_berat_badan = [
		        (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] < 37),
		        (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] > 45),
		        (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] < 35), 
		        (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] > 40)
		    ]

		pilihan = [0, 0, 0, 0]
		csv['tinggi_badan'] = np.select(kondisi, pilihan, default=1)
		csv['berat_badan'] = np.select(kondisi_berat_badan, pilihan, default=1)
		return csv

	def konvers_test_post(csv):
		csv[['jenis_kelamin']] = np.where(csv[['jenis_kelamin']] == 'perempuan', 0, 1)

		kondisi = [
		        (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] < 148),
		        (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] > 158),
		        (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] < 145), 
		        (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] > 155)
		    ]

		kondisi_berat_badan = [
		        (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] < 37),
		        (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] > 45),
		        (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] < 35), 
		        (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] > 40)
		    ]

		pilihan = [0, 0, 0, 0]
		csv['tinggi_badan'] = np.select(kondisi, pilihan, default=1)
		csv['berat_badan'] = np.select(kondisi_berat_badan, pilihan, default=1)
		return csv

	def konvers_train(csv):
	    csv.iloc[:, 0] = np.where(csv.iloc[:, 0] == 'perempuan', 0, 1)
	    csv.iloc[:, 3:5] = np.where(csv.iloc[:, 3:5] < 80.0, 0, 1)

	    kondisi = [
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,1] < 148),
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,1] > 158),
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,1] < 145), 
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,1] > 155)
	        ]

	    kondisi_berat_badan = [
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,2]< 37),
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,2]> 45),
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,2]< 35), 
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,2]> 40)
	        ]

	    pilihan = [0, 0, 0, 0]
	    csv.iloc[:,1] = np.select(kondisi, pilihan, default=1)
	    csv.iloc[:,2] = np.select(kondisi_berat_badan, pilihan, default=1)
	    return csv

	def konvers_target(csv):
	    csv = np.where(csv == 'berbakat', 1, 0)
	    return csv

	def konvers_ideal(xy_train_):
		xy_train_.iloc[:,0] = xy_train_.iloc[:,0].apply(lambda x: 'Perempuan' if x == 0 else 'Laki - Laki')
		xy_train_.iloc[:, 1:-1] = xy_train_.iloc[:, 1:-1].applymap(lambda x: 'ideal' if x == 1 else 'tidak ideal')
		return xy_train_
	
	def konvers_ideal_post(xy_train_):
		xy_train_.iloc[:,0] = xy_train_.iloc[:,0].apply(lambda x: 'Perempuan' if x == 0 else 'Laki - Laki')
		xy_train_.iloc[:, 1:] = xy_train_.iloc[:, 1:].applymap(lambda x: 'ideal' if x == 1 else 'tidak ideal')
		return xy_train_

	# gabung data
	def gabung(x_train, y_train):
	    xy_train = x_train.copy()
	    xy_train['hasil_bakat'] = y_train
	    return xy_train

	# konversi inputan (berat badan dan tinggi badan) menjadi 0 atau 1
	def konversi_berat_badan_tinggi_badan_inputan(csv):
		kondisi = [
		        (csv.iloc[:,0] == 1) & (csv.iloc[:,1] < 148),
		        (csv.iloc[:,0] == 1) & (csv.iloc[:,1] > 158),
		        (csv.iloc[:,0] == 0) & (csv.iloc[:,1] < 145), 
		        (csv.iloc[:,0] == 0) & (csv.iloc[:,1] > 155)
		    ]

		kondisi_berat_badan = [
		        (csv.iloc[:,0] == 1) & (csv.iloc[:,2]< 37),
		        (csv.iloc[:,0] == 1) & (csv.iloc[:,2]> 45),
		        (csv.iloc[:,0] == 0) & (csv.iloc[:,2]< 35), 
		        (csv.iloc[:,0] == 0) & (csv.iloc[:,2]> 40)
		    ]

		pilihan = [0, 0, 0, 0]
		csv[['tinggi_badan']] = np.select(kondisi, pilihan, default=1)
		csv[['berat_badan']] = np.select(kondisi_berat_badan, pilihan, default=1)
		# csv.iloc[:,1] = np.select(kondisi, pilihan, default=1)
		# csv.iloc[:,2] = np.select(kondisi_berat_badan, pilihan, default=1)
		return csv
	
	'''  ========================================= pembagian data====================================== '''
	labeling = konvers(csv)
	data_training_lari = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_lari', 'teknik_dasar_lari', 'hasil_bakat_lari']]
	data_training_voli = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_voli', 'teknik_dasar_voli', 'hasil_bakat_voli']]
	

	data_testing_voli = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_voli', 'teknik_dasar_voli', 'hasil_bakat_voli']]
	

	data_training_renang = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_renang', 'teknik_dasar_renang', 'hasil_bakat_renang']]
	data_training_bulu_tangkis = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_bulu_tangkis', 'teknik_dasar_bulu_tangkis', 'hasil_bakat_bulu_tangkis']]
	data_training_sepak_bola = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_sepak_bola', 'teknik_dasar_sepak_bola', 'hasil_bakat_sepak_bola']]
	data_training_tenis_meja = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tenis_meja', 'teknik_dasar_tenis_meja', 'hasil_bakat_tenis_meja']]
	data_training_tolak_peluru = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tolak_peluru', 'teknik_dasar_tolak_peluru', 'hasil_bakat_tolak_peluru']]


	# data testing
	# data_training_voli = labeling[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_voli', 'teknik_dasar_voli', 'hasil_bakat_voli']]

	'''  =========================================end pembagian data====================================== '''

	'''  =========================================pembagian data training olahraga====================================== '''
	y_lari = csv['hasil_bakat_lari']
	x_lari = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_lari','teknik_dasar_lari']]
	x_train_lari, x_test_lari, y_train_lari, y_test_lari = train_test_split(x_lari,y_lari, test_size=0.2, random_state=0)

	y_voli = csv['hasil_bakat_voli']
	x_voli = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_voli','teknik_dasar_voli']]
	x_train_voli, x_test_voli, y_train_voli, y_test_voli = train_test_split(x_voli,y_voli, test_size=0.2, random_state=0)

	y_renang = csv['hasil_bakat_renang']
	x_renang = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_renang','teknik_dasar_renang']]
	x_train_renang, x_test_renang, y_train_renang, y_test_renang = train_test_split(x_renang,y_renang, test_size=0.2, random_state=0)

	y_bulu_tangkis = csv['hasil_bakat_bulu_tangkis']
	x_bulu_tangkis = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_bulu_tangkis','teknik_dasar_bulu_tangkis']]
	x_train_bulu_tangkis, x_test_bulu_tangkis, y_train_bulu_tangkis, y_test_bulu_tangkis = train_test_split(x_bulu_tangkis,y_bulu_tangkis, test_size=0.2, random_state=0)

	y_sepak_bola = csv['hasil_bakat_sepak_bola']
	x_sepak_bola = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_sepak_bola','teknik_dasar_sepak_bola']]
	x_train_sepak_bola, x_test_sepak_bola, y_train_sepak_bola, y_test_sepak_bola = train_test_split(x_sepak_bola,y_sepak_bola, test_size=0.2, random_state=0)

	y_tenis_meja = csv['hasil_bakat_tenis_meja']
	x_tenis_meja = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tenis_meja','teknik_dasar_tenis_meja']]
	x_train_tenis_meja, x_test_tenis_meja, y_train_tenis_meja, y_test_tenis_meja = train_test_split(x_tenis_meja,y_tenis_meja, test_size=0.2, random_state=0)

	y_tolak_peluru = csv['hasil_bakat_tolak_peluru']
	x_tolak_peluru = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tolak_peluru','teknik_dasar_tolak_peluru']]
	x_train_tolak_peluru, x_test_tolak_peluru, y_train_tolak_peluru, y_test_tolak_peluru = train_test_split(x_tolak_peluru,y_tolak_peluru, test_size=0.2, random_state=0)

	'''  =========================================pembagian data training olahraga====================================== '''
	
	'''  =========================================algoritma naivebayes====================================== '''
	model_lari = GaussianNB()
	model_lari.fit(x_train_lari, y_train_lari)

	model_voli = GaussianNB()
	model_voli.fit(x_train_voli, y_train_voli)

	model_renang = GaussianNB()
	model_renang.fit(x_train_renang, y_train_renang)

	model_bulu_tangkis = GaussianNB()
	model_bulu_tangkis.fit(x_train_bulu_tangkis, y_train_bulu_tangkis)

	model_sepak_bola = GaussianNB()
	model_sepak_bola.fit(x_train_sepak_bola, y_train_sepak_bola)

	model_tenis_meja = GaussianNB()
	model_tenis_meja.fit(x_train_tenis_meja, y_train_tenis_meja)

	model_tolak_peluru = GaussianNB()
	model_tolak_peluru.fit(x_train_tolak_peluru, y_train_tolak_peluru)

	'''  =========================================end algoritma naivebayes====================================== '''
	

	prediksi_lari = [0]
	prediksi_voli = [0]
	prediksi_renang = [0]
	prediksi_bulu_tangkis = [0]
	prediksi_sepak_bola = [0]
	prediksi_tenis_meja = [0]
	prediksi_tolak_peluru = [0]

	'''  =========================================method post====================================== '''
	prediksi_post = ''
	nama_siswa = ''
	jenis_kelamin = ''
	test = []
	test_ = []
	form = Fomrdata()
	if request.method == 'POST':
		form = Fomrdata(request.POST)
		if form.is_valid():
			dt = form .cleaned_data

			lihat = {
				'jenis_kelamin': [dt['jenis_kelamin']],
				'tinggi_badan': [dt['tinggi_badan']],
				'berat_badan': [dt['berat_badan']],

				'kemampuan_fisik_lari': [dt['kemampuan_fisik_lari']],
				'teknik_dasar_lari': [dt['teknik_dasar_lari']],

				'kemampuan_fisik_voli': [dt['kemampuan_fisik_voli']],
				'teknik_dasar_voli': [dt['teknik_dasar_voli']],

				'kemampuan_fisik_renang': [dt['kemampuan_fisik_renang']],
				'teknik_dasar_renang': [dt['teknik_dasar_renang']],

				'kemampuan_fisik_bulu_tangkis': [dt['kemampuan_fisik_bulu_tangkis']],
				'teknik_dasar_bulu_tangkis': [dt['teknik_dasar_bulu_tangkis']],

				'kemampuan_fisik_sepak_bola': [dt['kemampuan_fisik_sepak_bola']],
				'teknik_dasar_sepak_bola': [dt['teknik_dasar_sepak_bola']],

				'kemampuan_fisik_tenis_meja': [dt['kemampuan_fisik_tenis_meja']],
				'teknik_dasar_tenis_meja': [dt['teknik_dasar_tenis_meja']],

				'kemampuan_fisik_tolak_peluru': [dt['kemampuan_fisik_tolak_peluru']],
				'teknik_dasar_tolak_peluru': [dt['teknik_dasar_tolak_peluru']],
			}


			test = pd.DataFrame(lihat)
			# test = konvers_train(test)

			konversiberatbadantinggibadan = test.copy()
			konversiberatbadantinggibadan = konversi_berat_badan_tinggi_badan_inputan(konversiberatbadantinggibadan)

			test_ = test.copy()
			test_ = konvers_ideal_post(test_)

			nama_siswa = request.POST['nama_siswa']
			jenis_kelamin = request.POST['jenis_kelamin']

			
			prediksi_lari= model_lari.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_lari', 'teknik_dasar_lari']])
			prediksi_voli= model_voli.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_voli', 'teknik_dasar_voli']])
			prediksi_renang= model_renang.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_renang', 'teknik_dasar_renang']])
			prediksi_bulu_tangkis= model_bulu_tangkis.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_bulu_tangkis', 'teknik_dasar_bulu_tangkis']])
			prediksi_sepak_bola= model_sepak_bola.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_sepak_bola', 'teknik_dasar_sepak_bola']])
			prediksi_tenis_meja= model_tenis_meja.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tenis_meja', 'teknik_dasar_tenis_meja']])
			prediksi_tolak_peluru= model_tolak_peluru.predict(konversiberatbadantinggibadan[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik_tolak_peluru', 'teknik_dasar_tolak_peluru']])
			# prediksi_post = model.predict(test)
	'''  =========================================end method post====================================== '''

	'''  =========================================prediksi olahraga====================================== '''


	'''  ========================================= end prediksi olahraga====================================== '''
	
	if jenis_kelamin == '0':
		jenis_kelamin = "Perempuan"
	else:
		jenis_kelamin = "Laki - Laki"

	'''  =========================================kirim nilai====================================== '''
	# data_training_lari = x_train_lari.copy()
	# data_training_lari.reset_index(inplace=True)

	# file ini akan dikirim ke html (file ini digunakan sebagai data training ke 7 olahraga)
	def kirimdatatraining(data_training, x_train):
		datanya = x_train.copy()
		datanya.reset_index(inplace=True)
		return datanya

	data_training_lari = kirimdatatraining(data_training_lari, x_train_lari)
	data_training_renang = kirimdatatraining(data_training_renang, x_train_renang)
	data_training_sepak_bola = kirimdatatraining(data_training_sepak_bola, x_train_sepak_bola)
	data_training_tolak_peluru = kirimdatatraining(data_training_tolak_peluru, x_train_tolak_peluru)
	data_training_bulu_tangkis = kirimdatatraining(data_training_bulu_tangkis, x_train_bulu_tangkis)
	data_training_tenis_meja = kirimdatatraining(data_training_tenis_meja, x_train_tenis_meja)
	data_training_voli = kirimdatatraining(data_training_voli, x_train_voli)
	
	

	# data testing
	data_testing_voli = kirimdatatraining(data_testing_voli, x_test_voli)
	data_testing_lari = kirimdatatraining(data_training_lari, x_test_lari)
	data_testing_renang = kirimdatatraining(data_training_renang, x_test_renang)
	data_testing_sepak_bola = kirimdatatraining(data_training_sepak_bola, x_test_sepak_bola)
	data_testing_tenis_meja = kirimdatatraining(data_training_tenis_meja, x_test_tenis_meja)
	data_testing_bulu_tangkis = kirimdatatraining(data_training_bulu_tangkis, x_test_bulu_tangkis)
	data_testing_tolak_peluru = kirimdatatraining(data_training_tolak_peluru, x_test_tolak_peluru)

	

	# data_training_renang.to_csv('data_training_renang.csv')
	# data_training_tenis_meja.to_csv('data_training_tenis_meja.csv')
	# data_training_tenis_meja.to_csv('data_training_tenis_meja.csv')
	# data_training_bulu_tangkis.to_csv('data_training_bulu_tangkis.csv')
	# data_training_tolak_peluru.to_csv('data_training_tolak_peluru.csv')
	# data_training_sepak_bola.to_csv('data_training_sepak_bola.csv')

	# pengujian

	def lakukan_uji(data_aktual, modelnya):
		dataku = data_aktual.values
		data_mau_prediksi = dataku.reshape(-1,1)
		data_aktual = data_aktual                                         # data yang sebenarnya
		data_hasil_prediksi = modelnya.predict(data_mau_prediksi)		# data yang di prediksi dari data yang sebenarnya


		precision = metrics.precision_score(data_aktual, data_hasil_prediksi, average='weighted')    # prcesion : (y_true, y_pred)
		recall = metrics.recall_score(data_aktual, data_hasil_prediksi, average='weighted')
		akurasi = metrics.accuracy_score(data_aktual, data_hasil_prediksi)
		hasilnya = {
			'precision': int(precision * 100),
			'recall': int(recall * 100),
			'akurasi': int(akurasi * 100)
		}
		# df = pd.DataFrame(hasilnya)

		return hasilnya

	hasil_uji_lari = lakukan_uji(y_test_lari, model_lari)
	hasil_uji_renang = lakukan_uji(y_test_renang, model_renang)
	hasil_uji_sepak_bola = lakukan_uji(y_test_sepak_bola, model_sepak_bola)
	hasil_uji_tolak_peluru = lakukan_uji(y_test_tolak_peluru, model_tolak_peluru)
	hasil_uji_tenis_meja = lakukan_uji(y_test_tenis_meja, model_tenis_meja)
	hasil_uji_bulu_tangkis = lakukan_uji(y_test_bulu_tangkis, model_bulu_tangkis)
	hasil_uji_voli = lakukan_uji(y_test_voli, model_voli)

	# print(hasil_uji_voli['precision'])

	# dataku = y_test_voli.values
	# data_mau_prediksi = dataku.reshape(-1,1)
	# # print(dataku.reshape(-1,1).ndim)

	# data_aktual_voli = y_test_voli                                         # data yang sebenarnya
	# data_hasil_prediksi_voli = model_voli.predict(data_mau_prediksi)		# data yang di prediksi dari data yang sebenarnya


	# precision_voli = metrics.precision_score(data_aktual_voli, data_hasil_prediksi_voli, average='weighted')    # prcesion : (y_true, y_pred)
	# recall_voli = metrics.recall_score(data_aktual_voli, data_hasil_prediksi_voli, average='weighted')
	# akurasi_voli = metrics.accuracy_score(data_aktual_voli, data_hasil_prediksi_voli)




	context = {
		'form' : form,
		'test': test,
		'nama_siswa': nama_siswa,
		'jenis_kelamin': jenis_kelamin,

		'prediksi_lari': prediksi_lari[0],
		'prediksi_voli': prediksi_voli[0],
		'prediksi_renang': prediksi_renang[0],
		'prediksi_bulu_tangkis': prediksi_bulu_tangkis[0],
		'prediksi_sepak_bola': prediksi_sepak_bola[0],
		'prediksi_tenis_meja': prediksi_tenis_meja[0],
		'prediksi_tolak_peluru': prediksi_tolak_peluru[0],
		'data_training_lari': data_training_lari,
		'data_training_voli': data_training_voli,
		

		'data_testing_voli': data_testing_voli,
		'data_testing_tolak_peluru': data_testing_tolak_peluru,
		'data_testing_lari': data_testing_lari,
		'data_testing_renang': data_testing_renang,
		'data_testing_sepak_bola': data_testing_sepak_bola,
		'data_testing_tenis_meja': data_testing_tenis_meja,
		'data_testing_bulu_tangkis': data_testing_bulu_tangkis,

		# 'precision_voli': int(precision_voli * 100),
		# 'recall_voli': int(recall_voli * 100),
		# 'akurasi_voli': int(akurasi_voli * 100),


		'hasil_uji_voli': hasil_uji_voli,
		'hasil_uji_tenis_meja': hasil_uji_tenis_meja,
		'hasil_uji_lari': hasil_uji_lari,
		'hasil_uji_tolak_peluru': hasil_uji_tolak_peluru,
		'hasil_uji_renang': hasil_uji_renang,
		'hasil_uji_bulu_tangkis': hasil_uji_bulu_tangkis,
		'hasil_uji_sepak_bola': hasil_uji_sepak_bola,




		'data_training_renang': data_training_renang,
		'data_training_sepak_bola': data_training_sepak_bola,
		'data_training_tenis_meja': data_training_tenis_meja,
		'data_training_tolak_peluru': data_training_tolak_peluru,
		'data_training_bulu_tangkis': data_training_bulu_tangkis,

		# 'xy_train' : xy_train,
		# 'xy_train_' : xy_train_,
		# 'idealnya' : idealnya,
		# 'test_' : test_,
		# 'prediksi_post' : prediksi_post,
	}
	'''  =========================================end kirim nilai====================================== '''

	return render(request, 'myapp/dashboard1.html', context)


def dashboard3(request):
	db = Datas.objects.all()
	if not db:
		return redirect('datas')
	csv = pd.DataFrame(db.values())

	label_encoder = preprocessing.LabelEncoder()
	
	# csv[['jenis_kelamin', 'p_mengulang', 'p_cuti', 'sam_bekerja','a_papua']] = csv[['jk', 'p_mengulang', 'p_cuti', 'sam_bekerja','a_papua']].apply(label_encoder.fit_transform)
	# csv[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] = np.where(csv[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] < 3.0, 0, 1)
	
	csv[['kemampuan_fisik', 'teknik_dasar']] = np.where(csv[['kemampuan_fisik', 'teknik_dasar']] < 80.0, 0, 1)
	csv[['jenis_kelamin']] = np.where(csv[['jenis_kelamin']] == 'perempuan', 0, 1)
	csv[['hasil_bakat']] = np.where(csv[['hasil_bakat']] == 'berbakat', 1, 0)
	csv[['kemampuan_fisik', 'teknik_dasar']] = np.where(csv[['kemampuan_fisik', 'teknik_dasar']] < 80.0, 0, 1)


	kondisi = [
		(csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] < 148),
		(csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] > 158),
		(csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] < 145), 
		(csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] > 155)
	]

	kondisi_berat_badan = [
		(csv['jenis_kelamin'] == 1) & (csv['berat_badan'] < 37),
		(csv['jenis_kelamin'] == 1) & (csv['berat_badan'] > 45),
		(csv['jenis_kelamin'] == 0) & (csv['berat_badan'] < 35), 
		(csv['jenis_kelamin'] == 0) & (csv['berat_badan'] > 40)
	]

	pilihan = [0, 0, 0, 0]

	csv['tinggi_badan'] = np.select(kondisi, pilihan, default=1)
	csv['berat_badan'] = np.select(kondisi_berat_badan, pilihan, default=1)

	y = csv['hasil_bakat']	 																	 # y_train
	x = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik','teknik_dasar']]  # x_train

	x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
	nv = GaussianNB()
	ajar = nv.fit(x_train, y_train)
	y_pred = nv.predict(x_test)

	# mixed
	# data_y = pd.DataFrame(y)
	# data_y = data_y.apply(label_encoder.fit_transform)
	# yyy = data_y['hasil_bakat']
	# clf = MixedNB(categorical_features=[0,1])       #discrete and continues data
	# # clf = MixedNB(categorical_features='all')		# discrete data only
	# # clf = MixedNB()									# continuous data only
	# clf.fit(x,yyy)
	# prediksi_mixed = clf.predict(x_test)
	# encoder_y_test = label_encoder.transform(y_test)
	
	# akurasi_mixed = accuracy_score(encoder_y_test, prediksi_mixed)

	# end mixed

	gabung = x_train.copy()
	gabung.insert(5,'hasil_bakat',y_train,True)
	x_train_y_train = gabung.copy()

	# gabung.loc[(gabung.jk == 0), 'jk'] = 'perempuan'			# ini kalau satu kondisi
	# gabung.loc[(gabung.jk == 1), 'jk'] = 'laki-laki'			# hanya satu kondisi

	# gabung['jenis_kelamin'] = np.where(gabung['jenis_kelamin'] == 0, 'perempuan', 'laki-laki')
	# gabung[['kemampuan_fisik', 'teknik_dasar','berat_badan', 'tinggi_badan']] = np.where(gabung[['kemampuan_fisik', 'teknik_dasar','berat_badan', 'tinggi_badan']] == 1 , 'ideal', 'tidak ideal')
	# gabung['hasil_bakat'] = np.where(gabung['hasil_bakat'] == 2 , 'berbakat', 'tidak berbakat')


	kamusdata = {
		'jenis_kelamin'	: np.array([0]),
		'tinggi_badan'	: np.array([0]),
		'berat_badan'	: np.array([0]),
		'kemampuan_fisik' : np.array([0]),
		'teknik_dasar'	: np.array([0]),
		'hasil_bakat'	: np.array([0]),
	}

	test = pd.DataFrame(kamusdata)
	# prediksi_test = nv.predict(test)

	form = Fomrdata()

	
	prediksi_post = ''

	# test['jenis_kelamin'] = np.where(test['jenis_kelamin'] == 0, ' ', ' ')
	# test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6','sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6','sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, ' ', ' ')	# 2 kondisi ya/tidak

	data_input = request.POST
	print(data_input)

	context = {
		'gabung': gabung,
		'form' : form,
	}
	return render(request, 'myapp/dashboard1.html', context)

@login_required
def dashboard2(request):
	# data
	db = Datas.objects.all()
	if not db:
		return redirect('datas')
	csv = pd.DataFrame(db.values())
	# csv = pd.read_csv('D:/aplikasi/tesis/aplikasinaivebayes/static/data.csv')
	label_encoder = preprocessing.LabelEncoder()
	
	csv[['jk', 'p_mengulang', 'p_cuti', 'sam_bekerja','a_papua']] = csv[['jk', 'p_mengulang', 'p_cuti', 'sam_bekerja','a_papua']].apply(label_encoder.fit_transform)
	csv[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] = np.where(csv[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] < 3.0, 0, 1)
	csv[['kemampuan_fisik', 'teknik_dasar']] = np.where(csv[['kemampuan_fisik', 'teknik_dasar']] < 80.0, 0, 1)

	csv[['jenis_kelamin']] = np.where(csv[['jenis_kelamin']] == 'perempuan', 0, 1)
	csv[['hasil_bakat']] = np.where(csv[['hasil_bakat']] == 'berbakat', 1, 0)
	csv[['kemampuan_fisik', 'teknik_dasar']] = np.where(csv[['kemampuan_fisik', 'teknik_dasar']] < 80.0, 0, 1)


	kondisi = [
		(csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] < 148),
		(csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] > 158),
		(csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] < 145), 
		(csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] > 155)
	]

	kondisi_berat_badan = [
		(csv['jenis_kelamin'] == 1) & (csv['berat_badan'] < 37),
		(csv['jenis_kelamin'] == 1) & (csv['berat_badan'] > 45),
		(csv['jenis_kelamin'] == 0) & (csv['berat_badan'] < 35), 
		(csv['jenis_kelamin'] == 0) & (csv['berat_badan'] > 40)
	]

	pilihan = [0, 0, 0, 0]

	csv['tinggi_badan'] = np.select(kondisi, pilihan, default=1)
	csv['berat_badan'] = np.select(kondisi_berat_badan, pilihan, default=1)

	y = csv['hasil_bakat']	 																	 # y_train
	x = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik','teknik_dasar']]  # x_train

	x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
	nv = GaussianNB()
	ajar = nv.fit(x_train, y_train)
	y_pred = nv.predict(x_test)

	# mixed
	data_y = pd.DataFrame(y)
	data_y = data_y.apply(label_encoder.fit_transform)
	yyy = data_y['hasil_bakat']
	clf = MixedNB(categorical_features=[0,1])       #discrete and continues data
	# clf = MixedNB(categorical_features='all')		# discrete data only
	# clf = MixedNB()									# continuous data only
	clf.fit(x,yyy)
	prediksi_mixed = clf.predict(x_test)
	encoder_y_test = label_encoder.transform(y_test)
	
	akurasi_mixed = accuracy_score(encoder_y_test, prediksi_mixed)

	# end mixed

	gabung = x_train.copy()
	gabung.insert(5,'hasil_bakat',y_train,True)
	x_train_y_train = gabung.copy()

	# gabung.loc[(gabung.jk == 0), 'jk'] = 'perempuan'			# ini kalau satu kondisi
	# gabung.loc[(gabung.jk == 1), 'jk'] = 'laki-laki'			# hanya satu kondisi

	gabung['jenis_kelamin'] = np.where(gabung['jenis_kelamin'] == 0, 'perempuan', 'laki-laki')
	gabung[['kemampuan_fisik', 'teknik_dasar','berat_badan', 'tinggi_badan']] = np.where(gabung[['kemampuan_fisik', 'teknik_dasar','berat_badan', 'tinggi_badan']] == 1 , 'ideal', 'tidak ideal')
	gabung['hasil_bakat'] = np.where(gabung['hasil_bakat'] == 2 , 'berbakat', 'tidak berbakat')

	# gabung[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(gabung[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, 'tidak', 'ya')	# 2 kondisi ya/tidak
	# gabung['prediksi'] = np.where(gabung['prediksi'] == 'tw', 'Tepat Waktu', 'Terlambat')
	# gabung[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] = np.where(gabung[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] == 0, 'lebih kecil dari 3', 'lebih besar atau sama dengan 3')	# 2 kondisi ya/tidak

	# gabung = x_train
	# pd.options.mode.chained_assigment = None
	# gabung.loc[:, 'jk'] = gabung.loc[:, 'jk'].apply(lambda x: 'perempuan' if x == 0 else 'laki - laki')
	# gabung.loc[:, 'jk'] = gabung.loc[:, 'jk'].apply(lambda x: 'perempuan' if x == 0 else 'laki - laki')
	# gabung.insert(7,'prediksi',y_train,True)


	# imputan data
	kamusdata = {
		'jenis_kelamin'	: np.array([0]),
		'tinggi_badan'	: np.array([0]),
		'berat_badan'	: np.array([0]),
		'kemampuan_fisik'	: np.array([0]),
		'teknik_dasar'	: np.array([0]),
		'hasil_bakat'	: np.array([0]),
	}

	test = pd.DataFrame(kamusdata)
	prediksi_test = nv.predict(test)

	form = Fomrdata()

	prediksi_post = ''

	test['jenis_kelamin'] = np.where(test['jenis_kelamin'] == 0, ' ', ' ')
	# test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6','sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6','sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, ' ', ' ')	# 2 kondisi ya/tidak

	if request.method == 'POST':
		pass
		# form = Fomrdata(request.POST)
		# if form.is_valid():
		# 	dt = form .cleaned_data
		# 	print(dt)
		# 	lihat = {'jk': [dt['jk']], 'p_mengulang': [dt['p_mengulang']], 'ipk': [dt['ipk']], 'p_cuti': [dt['p_cuti']], 'sam_bekerja': [dt['sam_bekerja']], 'a_papua': [dt['a_papua']], 'ipk1': [dt['ipk1']],
		# 		'ipk_prodi': [dt['ipk_prodi']],
		# 		'ipk2': [dt['ipk2']],
		# 		'ipk3': [dt['ipk3']],
		# 		'ipk4': [dt['ipk4']],
		# 		'ipk5': [dt['ipk5']],
		# 		'ipk6': [dt['ipk6']],
		# 	}

		# 	test = pd.DataFrame(lihat)
		# 	test = test.astype('int')
		# 	test[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] = np.where(test[['ipk','ipk_prodi','ipk1', 'ipk2', 'ipk3', 'ipk4','ipk5', 'ipk6']] < 3.0, 0, 1)



		# 	prediksi_post = nv.predict(test)

		# 	print('ini hasil')
		# 	print(test)
		# 	print(prediksi_post)

		# 	# print(test)
		# 	test['jk'] = np.where(test['jk'] == 0, 'perempuan', 'laki-laki')
		# 	test[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(test[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, 'tidak', 'ya')	# 2 kondisi ya/tidak
		# 	test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] = np.where(test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] == 0, 'lebih kecil dari 3', 'lebih besar atau sama dengan 3')	# 2 kondisi ya/tidak
			# print(test)
			
	# akurasi = accuracy_score(y_test, y_pred)

	print(gabung)
	context = {
		'gabung': gabung,
	}

	# context = {
	# 	# 'df'	: df,
	# 	'gabung': gabung,
	# 	'x_train'	: x_train,
	# 	'y_train'	: y_train,
	# 	'x_test'	: x_test,
	# 	'y_test'	: y_test,
	# 	'csv'		: csv,
		# 'x_train_y_train'	: x_train_y_train,
		# 'test'	: test,
		# 'form'	: form,
		# 'prediksi_post'	: prediksi_post,
		# 'akurasi'	: akurasi,
		# 'prediksi_mixed'	: prediksi_mixed,
		# 'akurasi_mixed'	: akurasi_mixed,
	# }

	return render(request, 'myapp/dashboard.html', context)

@login_required
def pengujian(request):
	# data
	db = Datas.objects.all()
	if not db:
		return redirect('datas')
	csv = pd.DataFrame(db.values())
	# label_encoder = preprocessing.LabelEncoder()


	def konvers(csv):
	    csv[['jenis_kelamin']] = np.where(csv[['jenis_kelamin']] == 'perempuan', 0, 1)
	    csv[['hasil_bakat']] = np.where(csv[['hasil_bakat']] == 'berbakat', 1, 0)
	    csv[['kemampuan_fisik', 'teknik_dasar']] = np.where(csv[['kemampuan_fisik', 'teknik_dasar']] < 80.0, 0, 1)

	    kondisi = [
	            (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] < 148),
	            (csv['jenis_kelamin'] == 1) & (csv['tinggi_badan'] > 158),
	            (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] < 145), 
	            (csv['jenis_kelamin'] == 0) & (csv['tinggi_badan'] > 155)
	        ]

	    kondisi_berat_badan = [
	            (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] < 37),
	            (csv['jenis_kelamin'] == 1) & (csv['berat_badan'] > 45),
	            (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] < 35), 
	            (csv['jenis_kelamin'] == 0) & (csv['berat_badan'] > 40)
	        ]

	    pilihan = [0, 0, 0, 0]
	    csv['tinggi_badan'] = np.select(kondisi, pilihan, default=1)
	    csv['berat_badan'] = np.select(kondisi_berat_badan, pilihan, default=1)
	    return csv

	def konvers_train(csv):
	    csv.iloc[:, 0] = np.where(csv.iloc[:, 0] == 'perempuan', 0, 1)
	    csv.iloc[:, 3:5] = np.where(csv.iloc[:, 3:5] < 80.0, 0, 1)

	    kondisi = [
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,1] < 148),
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,1] > 158),
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,1] < 145), 
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,1] > 155)
	        ]

	    kondisi_berat_badan = [
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,2]< 37),
	            (csv.iloc[:,0] == 1) & (csv.iloc[:,2]> 45),
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,2]< 35), 
	            (csv.iloc[:,0] == 0) & (csv.iloc[:,2]> 40)
	        ]

	    pilihan = [0, 0, 0, 0]
	    csv.iloc[:,1] = np.select(kondisi, pilihan, default=1)
	    csv.iloc[:,2] = np.select(kondisi_berat_badan, pilihan, default=1)
	    return csv

	def konvers_target(csv):
	    csv = np.where(csv == 'berbakat', 1, 0)
	    return csv

	def konvers_ideal(xy_train_):
		xy_train_.iloc[:,0] = xy_train_.iloc[:,0].apply(lambda x: 'Perempuan' if x == 0 else 'Laki - Laki')
		xy_train_.iloc[:, 1:-1] = xy_train_.iloc[:, 1:-1].applymap(lambda x: 'ideal' if x == 1 else 'tidak ideal')
		return xy_train_
	
	def konvers_ideal_post(xy_train_):
		xy_train_.iloc[:,0] = xy_train_.iloc[:,0].apply(lambda x: 'Perempuan' if x == 0 else 'Laki - Laki')
		xy_train_.iloc[:, 1:] = xy_train_.iloc[:, 1:].applymap(lambda x: 'ideal' if x == 1 else 'tidak ideal')
		return xy_train_

	# gabung data
	def gabung(x_train, y_train):
	    xy_train = x_train.copy()
	    xy_train['hasil_bakat'] = y_train
	    return xy_train




	'''  ========================================= pembagian data====================================== '''
	y = csv['hasil_bakat']	 # y_train
	x = csv[['jenis_kelamin', 'tinggi_badan', 'berat_badan', 'kemampuan_fisik','teknik_dasar']]
	x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)
	x_train_ = x_train.copy()
	y_train_ = y_train.copy()
	x_test_ = x_test.copy()
	y_test_ = y_test.copy()

	x_train_ = konvers_train(x_train_)
	y_train_ = konvers_target(y_train_)
	x_test_ = konvers_train(x_test_)
	y_test_ = konvers_target(y_test_)
	
	xy_train = gabung(x_train, y_train)
	xy_test = gabung(x_test, y_test)
	xy_train_ = xy_train.copy()
	xy_train_ = konvers_train(xy_train_)
	idealnya = xy_train_.copy()
	idealnya = konvers_ideal(idealnya)
	'''  =========================================end pembagian data====================================== '''
	
	'''  =========================================poengujian====================================== '''
	model = GaussianNB()
	model.fit(x_train_, y_train_)
	
	y_pred = model.predict(x_test_)
	y_prediksi = y_pred.copy()
	y_aktual = y_test_.copy()


	# precision = metrics.precision_score(kenyataan, prediksinya, average='weighted', zero_division=1)    # prcesion : (y_true, y_pred) ini dikomen
	precision = metrics.precision_score(y_aktual, y_prediksi, average=None)    # prcesion : (y_true, y_pred)
	recall = metrics.recall_score(y_aktual, y_prediksi, average=None)
	akurasi = metrics.accuracy_score(y_aktual, y_prediksi)

	'''  =========================================end poengujian====================================== '''



	'''  =========================================kirim nilai====================================== '''
	y_prediksi_ =  y_prediksi.copy()
	y_prediksi_ = np.where(y_prediksi_ == 0, 'Tidak Berbakat', 'Berbakat')

	# y_prediksi_ = konvers_target(y_prediksi_)
	xy_prediksi = gabung(x_test, y_prediksi_)

	context = {
		'xy_test' : xy_test,
		'xy_prediksi' : xy_prediksi,
		'precision' 						: round(precision[1], 2),
		'recall' 							: round(recall[1], 2),
		'akurasi' : round(akurasi, 2),
	}
	'''  =========================================end kirim nilai====================================== '''


	# ajar = nv.fit(x_train, y_train)
	# y_pred = nv.predict(x_test)

	# akurasi = metrics.accuracy_score(y_test, y_pred)
	# le = preprocessing.LabelEncoder()
	# listnya = ['t', 'tw']
	# le.fit(listnya)
	# kenyataan = le.transform(y_test)		# y_true
	# prediksinya = le.transform(y_pred)	# y_pred
	
	# precision = metrics.precision_score(kenyataan, prediksinya, average=None)    # prcesion : (y_true, y_pred)
	# precision = metrics.precision_score(kenyataan, prediksinya, average='weighted', zero_division=1)    # prcesion : (y_true, y_pred) ini dikomen
	# recall = metrics.recall_score(kenyataan, prediksinya, average='weighted')

	# data_y = pd.DataFrame(y)
	# data_y = data_y.apply(label_encoder.fit_transform)
	# yyy = data_y['prediksi']
	# clf = MixedNB(categorical_features=[0,1])       #discrete and continues data
	# clf.fit(x,yyy)
	# prediksi_mixed = clf.predict(x_test)
	# encoder_y_test = label_encoder.transform(y_test)
	
	# akurasi_mixed = accuracy_score(encoder_y_test, prediksi_mixed)

	# gabung = x_train.copy()
	# gabung.insert(7,'prediksi',y_train,True)
	# x_train_y_train = gabung.copy()

	
	# gabung['jk'] = np.where(gabung['jk'] == 0, 'perempuan', 'laki-laki')
	# gabung[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(gabung[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, 'tidak', 'ya')	# 2 kondisi ya/tidak
	# gabung['prediksi'] = np.where(gabung['prediksi'] == 'tw', 'Tepat Waktu', 'Terlambat')
	# gabung[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] = np.where(gabung[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] == 0, 'lebih kecil dari 3', 'lebih besar atau sama dengan 3')	# 2 kondisi ya/tidak

	# gabung_x_test = x_test.copy()
	# gabung_x_test.insert(7,'prediksi',y_test,True)
	# x_test_y_test = gabung_x_test.copy()

	
	# gabung_x_test['jk'] = np.where(gabung_x_test['jk'] == 0, 'perempuan', 'laki-laki')
	# gabung_x_test[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(gabung_x_test[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, 'tidak', 'ya')	# 2 kondisi ya/tidak
	# gabung_x_test['prediksi'] = np.where(gabung_x_test['prediksi'] == 'tw', 'Tepat Waktu', 'Terlambat')
	# gabung_x_test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] = np.where(gabung_x_test[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] == 0, 'lebih kecil dari 3', 'lebih besar atau sama dengan 3')	# 2 kondisi ya/tidak

	# gabung_y_pred = x_test.copy()
	# gabung_y_pred.insert(7,'prediksi',y_pred,True)
	# x_test_y_test = gabung_y_pred.copy()

	
	# gabung_y_pred['jk'] = np.where(gabung_y_pred['jk'] == 0, 'perempuan', 'laki-laki')
	# gabung_y_pred[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] = np.where(gabung_y_pred[['sam_bekerja','p_mengulang', 'p_cuti', 'a_papua']] == 0, 'tidak', 'ya')	# 2 kondisi ya/tidak
	# gabung_y_pred['prediksi'] = np.where(gabung_y_pred['prediksi'] == 'tw', 'Tepat Waktu', 'Terlambat')
	# gabung_y_pred[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] = np.where(gabung_y_pred[['ipk','ipk_prodi','ipk1','ipk2','ipk3','ipk4','ipk4','ipk5','ipk6']] == 0, 'lebih kecil dari 3', 'lebih besar atau sama dengan 3')	# 2 kondisi ya/tidak

	# context = {
		# 'db'	: db,
		# 'csv'	: csv,
		# 'x_train' : x_train,
		# 'x_test' : x_test,
		# 'y_train' : y_train,
		# 'y_test' : y_test,
		# 'y_pred' : y_pred,
		# 'akurasi' : round(akurasi, 2),
		# 'precision' 						: round(precision[1], 2),
		# 'recall' 							: round(recall, 2),
		# 'akurasi_mixed' : akurasi_mixed,
		# 'gabung'	: gabung,
		# 'gabung_x_test'	: gabung_x_test,
		# 'gabung_y_pred'	: gabung_y_pred,
	# }
	return render(request, 'myapp/pengujian.html', context)

def reset_data(request):
	Datas.objects.all().delete()
	return redirect('datas')