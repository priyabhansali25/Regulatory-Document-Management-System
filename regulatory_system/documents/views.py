from django.shortcuts import render
from .models import Document

def document_list(request):
    query = request.GET.get('q')
    
    if query:
        documents = Document.objects.filter(title__icontains=query) | \
                    Document.objects.filter(document_type__icontains=query)
    else:
        documents = Document.objects.all()
   
    return render(request, 'documents/document_list.html',{'documents': documents,'query':query})

# Create your views here.
