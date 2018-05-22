from django.shortcuts import render
import requests
from sgc.models import DocumentTable
import pdb


def home(request):
    response = requests.get('http://104.200.28.178/todo/api/v1.0/get_documents?node_folder_portal=00f44da9-4686-4410-a9e3-e4ec21b48bb0')
    documentos = response.json()
    if len(documentos['RESULTADOS']) > 0:
        table = DocumentTable(documentos['RESULTADOS'], template_name='django_tables2/bootstrap.html')
        return render(request, 'sgc/home.html', { 'documentos' : table })
    else:
        return render(request, 'sgc/home.html', "NO EXISTE DOCUMENTOS")
# Create your views here.
