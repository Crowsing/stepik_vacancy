from django.http import Http404
from django.shortcuts import render

from vacancy.models import Specialty, Company, Vacancy
from vacancy.scripts.get_count import get_count_vacancies, get_count_companies


def main_view(request):
    context = {
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
        'count_vacancies': get_count_vacancies(),
        'count_companies': get_count_companies()
    }
    return render(request, 'vacancy/index.html', context=context)


def cat_view(request, vacancies_cat):
    correct_vacancies_cat = Specialty.objects.filter(code=vacancies_cat).exists()

    if correct_vacancies_cat:
        return render(request, 'vacancy/vacancies.html', context={
                                'vacancy_cat': vacancies_cat,
                                'vacancies': Vacancy.objects.filter(specialty__code=vacancies_cat)
                            }
                      )
    else:
        raise Http404


def companies_view(request, company_id):
    correct_company_id = Company.objects.filter(company_id=company_id).exists()

    if correct_company_id:
        return render(request, 'vacancy/company.html', context={
                            'company': Company.objects.filter(company_id=company_id).first(),
                            'vacancies_by_company': Vacancy.objects.filter(company_id=company_id)
                        }
                      )
    else:
        raise Http404


def vacancy_view(request, vacancy_id):
    if vacancy_id:
        if Vacancy.objects.filter(vacancy_id=vacancy_id).exists():
            return render(request, 'vacancy/vacancy.html', context={
                                    'vacancy': Vacancy.objects.filter(vacancy_id=vacancy_id).first()
                                }
                          )
        else:
            raise Http404

    context = {
        'vacancies': Vacancy.objects.all(),
    }
    return render(request, 'vacancy/vacancies.html', context=context)
