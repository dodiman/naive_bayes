from django.contrib import admin
from .models import Datas

# untuk import export
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Datas)		# ini untuk registrasi datas

@admin.register(Datas)						# ini juga untuk regsitrasi datas
class DatasAdmin(ImportExportModelAdmin):	
    pass