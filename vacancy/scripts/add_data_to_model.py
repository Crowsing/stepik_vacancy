import os
import django
import vacancy.data as data


os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

import vacancy.models as models

# for specialty in data.specialties:
#     models.Specialty.objects.create(code=specialty['code'], title=specialty['title'])
#
# for company in data.companies:
#     models.Company.objects.create(
#         name=company['title'],
#         location=company['location'],
#         logo='https://place-hold.it/100x60',
#         description=company['description'],
#         employee_count=company['employee_count']
#     )
#
# for vacancy in data.jobs:
#     specialty = models.Specialty.objects.filter(code=vacancy['specialty']).first()
#     company = models.Company.objects.filter(id=int(vacancy['company'])).first()
#     models.Vacancy.objects.create(
#         title=vacancy['title'],
#         specialty=specialty,
#         company=company,
#         skills=vacancy['skills'],
#         description=vacancy['description'],
#         salary_min=vacancy['salary_from'],
#         salary_max=vacancy['salary_to'],
#         published_at=vacancy['posted']
#     )

