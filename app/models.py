from django.db import models


class Company(models.Model):
    entity = models.IntegerField(default=0)
    name = models.CharField(max_length=45)
    url = models.TextField(default='Null')
    logourl = models.TextField(default='Null')
    # technologies = models.ManyToManyField(Tech, related_name="companies_using")

class Tech(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    companies_using = models.ManyToManyField(Company, related_name="technologies")

class Entry(models.Model):
    company = models.CharField(max_length=45)
    tech = models.CharField(max_length=45)
    category = models.CharField(max_length=45)



