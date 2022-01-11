from django.contrib import admin

# Register your models he
from storage.models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):

    list_display = ["number", "description", "location"]