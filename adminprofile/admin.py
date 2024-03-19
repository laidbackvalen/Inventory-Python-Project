from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
from  .models import useradmin, items,returnmodel
admin.site.register(useradmin)
admin.site.register(returnmodel)

@admin.register(items)
class itemsAdmin(ImportExportActionModelAdmin):
    pass