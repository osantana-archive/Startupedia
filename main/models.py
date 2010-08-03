#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class CompanyCategory(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)

    class Meta:
        verbose_name_plural = "company categories"

    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    logo = models.ImageField(verbose_name=_("logo"), upload_to="company_logo", height_field="logo_width", width_field="logo_height")
    logo_width = models.IntegerField()
    logo_height = models.IntegerField()
    description = models.TextField(verbose_name=_("description"))
    website = models.URLField(verbose_name=_("website"), verify_exists=True)
    email = models.EmailField(verbose_name=_("e-mail"))
    address = models.CharField(verbose_name=_("address"), max_length=150)
    category = models.ForeignKey(CompanyCategory, verbose_name=_("category"))
    twitter = models.CharField(verbose_name=_("twitter"), max_length=50)
    linkedin = models.CharField(verbose_name=_("linkedin"), max_length=150)
    employees = models.IntegerField(verbose_name=_("employees"))

    class Meta:
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name


# TODO: replace address/linkedin/twitter/email/.../ with 'N-M' contact field.
# TODO: add a geo-tag and a versioning system

