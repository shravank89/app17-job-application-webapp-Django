from django.contrib import admin
from .models import DbForm

class DbFormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    readonly_fields = ("occupation",)

admin.site.register(DbForm, DbFormAdmin)

