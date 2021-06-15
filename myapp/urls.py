from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('datas', views.datas, name='datas'),
	path('laporan', views.laporan, name='laporan'),
	path('reset_data', views.reset_data, name='reset_data'),
	path('pengujian', views.pengujian, name='pengujian'),
]