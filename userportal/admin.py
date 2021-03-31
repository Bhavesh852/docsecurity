from django.contrib import admin
from .models import Doc_Detail, Private_Doc, Contact

# Register your models here.
class AdminDoc_Detail(admin.ModelAdmin):
	list_display = ['doc_title', 'doc_category', 'doc_tech']

admin.site.register(Doc_Detail, AdminDoc_Detail)
admin.site.register(Private_Doc)
admin.site.register(Contact)
