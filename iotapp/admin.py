from django.contrib import admin
from .models import IoTObject, IoTData

class IoTObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'auth_token')  # Spécifiez les champs à afficher dans la liste des objets


class IoTDataAdmin(admin.ModelAdmin):
    list_display = ('object',  'temperature', 'humidity')  # Spécifiez les champs à afficher dans la liste des objets




admin.site.register(IoTObject, IoTObjectAdmin) 
admin.site.register(IoTData, IoTDataAdmin) 