import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

import vacancy.models as models


def get_count_vacancies():
    """
    get count all vacancies
    :return: dict
    """
    result = {}

    for speciality in models.Specialty.objects.all():
        result[speciality.code] = models.Vacancy.objects.filter(specialty__code=speciality.code).count()

    return result


def get_count_companies():
    """
    get count all vacancies
    :return: dict
    """
    result = {}

    for company in models.Company.objects.all():
        result[company.company_id] = models.Vacancy.objects.filter(company__name=company.name).count()

    return result
