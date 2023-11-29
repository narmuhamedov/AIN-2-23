from django.shortcuts import render, get_object_or_404
from .models import StringRun, FilmModel, AfishaTable, Slider
from django.views import generic


class MainView(generic.View):
    def get(self, request):
        string_ = StringRun.objects.all()
        film_list = FilmModel.objects.all()
        afisha_list = AfishaTable.objects.all()
        slider = Slider.objects.all()
        return render(
            request,
            template_name='main_page/index.html',
            context={
                'string_': string_,
                'film_list': film_list,
                'afisha_list': afisha_list,
                'slider': slider,
            }
        )


class FilmDetailView(generic.DetailView):
    template_name = 'main_page/film_detail.html'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(FilmModel, id=film_id)

class Search(generic.ListView):
    template_name = "main_page/index.html"
    context_object_name = "film_list"
    paginate_by = 5

    def get_queryset(self):
        return FilmModel.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
