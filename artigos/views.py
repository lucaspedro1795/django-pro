from django.shortcuts import render
from .models import Artigo
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
    artigos = Artigo.objects.all()
    template = loader.get_template('artigos/index.html')

    busca = request.GET.get('search')
    if busca:
        artigos = Artigo.objects.filter(Rotulo = busca)

    context = {
        'artigos': artigos,
    }


    return HttpResponse(template.render(context, request))

def detail(request, artigo_id):
    try:
        artigo = Artigo.objects.get(pk=artigo_id)
    except Artigo.DoesNotExist:
        raise Http404("Artigos inexistentes.")
    return render(request, 'artigos/detail.html', {'artigo': artigo})

