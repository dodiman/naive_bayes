from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('datas', views.datas, name='datas'),
	path('data_siswa', views.data_siswa, name='data_siswa'),
	path('laporan', views.laporan, name='laporan'),
	path('reset_data', views.reset_data, name='reset_data'),
	path('reset_data_siswa', views.reset_data_siswa, name='reset_data_siswa'),
	path('pengujian', views.pengujian, name='pengujian'),
]