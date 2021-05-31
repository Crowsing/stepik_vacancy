from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from vacancy.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = "vacancy/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(vacancies_count=Count('vacancies'))
        context['companies'] = Company.objects.annotate(companies_count=Count('vacancies'))

        return context


class CatView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancy/vacancies.html'

    def get_queryset(self):
        return (
            self.model.objects
            .filter(specialty__code=self.kwargs['vacancy_cat'])
            .select_related('specialty', 'company')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy_title'] = get_object_or_404(Specialty, code=self.kwargs['vacancy_cat'])

        return context


class CompanyView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancy/company.html'

    def get_queryset(self):
        return (
            self.model.objects
            .filter(company__id=self.kwargs['company_id'])
            .select_related('specialty', 'company')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, id=self.kwargs['company_id'])

        return context


class VacanciesView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancy/vacancies.html'
    queryset = model.objects.select_related('specialty', 'company')


class VacancyView(DetailView):
    model = Vacancy
    context_object_name = 'vacancy'
    template_name = 'vacancy/vacancy.html'
    queryset = model.objects.select_related('specialty', 'company')


def custom_handler404(request, exception):
    return HttpResponseNotFound("404 Страница не найдена")


def custom_handler500(request):
    return HttpResponseServerError("500 Server Error")