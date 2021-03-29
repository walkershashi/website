from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here.
def index(request):
    all_albums = Album.objects.all()

    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }

    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except:
        raise Http404("Album does not exists")
    
    return render(request, 'music/detail.html', {'album': album})