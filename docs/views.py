from django.shortcuts import render, redirect
from django.http import HttpResponse
# NOVO #
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import document
from .forms import DocumentForm


def index(request):

    return HttpResponse('<h1>teste</h1><br><h1>SEJA BEM VINDO</h1>')

def teste(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = document(docfile = request.FILES['docfile'])
            newdoc.save()
            messages.add_message(request, messages.SUCCESS, "Seu arquivo foi enviado com sucesso!")
            # Redirect to the document list after POST
            return redirect('list')
    else:
        form = DocumentForm() # A empty, unbound form

    
    documents = document.objects.all()

    
    return render(request,'list.html',{'documents': documents, 'form': form})
    
