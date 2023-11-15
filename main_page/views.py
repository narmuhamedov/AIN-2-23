from django.shortcuts import render, get_object_or_404
from .models import StringRun, FilmModel

def main_view(request):
    if request.method == 'GET':
        string_ = StringRun.objects.all()
        film_list = FilmModel.objects.all()
        return render(request, template_name='main_page/index.html',
                      context={
                          'string_': string_,
                          'film_list': film_list,
                      })


def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(FilmModel, id=id)
        return render(request, template_name='main_page/film_detail.html', context={
            'film_id':film_id
        })