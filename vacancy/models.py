from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=32)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'Company with id={self.pk}'


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=32)
    picture = models.URLField(default='https://place-hold.it/100x60')

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'

    def __str__(self):
        return f'Specialty with id={self.pk}'


class Vacancy(models.Model):
    title = models.CharField(max_length=32)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'Vacancy with id={self.pk}'

    def clean(self):
        if self.salary_min > self.salary_max:
            raise ValidationError(_('Invalid salary_min or salary_max. salary_min must be less or equal to salary_max'))


