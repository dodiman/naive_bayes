from import_export import resources
from .models import *

class DatasResources(resources.ModelResource):
	class Meta:
		model = Datas

class DataSiswaResources(resources.ModelResource):
	class Meta:
		model = DataSiswa