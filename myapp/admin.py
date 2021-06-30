from django.contrib import admin
from .models import *

# import export 
from import_export.admin import ImportExportModelAdmin

# class RincianAdmin(admin.ModelAdmin):
# 	exclude = ('jumlahnya',)

@admin.register(Datas)
class DatasAdmin(ImportExportModelAdmin):
	pass

@admin.register(DataSiswa)
class DatasAdmin(ImportExportModelAdmin):
	pass