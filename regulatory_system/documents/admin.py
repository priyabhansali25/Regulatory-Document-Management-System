from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'uploaded_at')

admin.site.register(Document, DocumentAdmin)

# Register your models here.
