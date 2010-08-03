#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField


# TODO: replace address/linkedin/twitter/email/.../ with 'N-M' contact field.
# TODO: add a geo-tag and a versioning system



# Person

class Person(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    picture = models.ImageField(verbose_name=_("picture"), upload_to="person_picture", height_field="picture_width", width_field="picture_height", blank=True)
    picture_width = models.IntegerField(blank=True, null=True)
    picture_height = models.IntegerField(blank=True, null=True)
    twitter = models.CharField(verbose_name=_("twitter"), max_length=50, blank=True)
    linkedin = models.CharField(verbose_name=_("linkedin"), max_length=150, blank=True)
    blog = models.URLField(verbose_name=_("blog"), verify_exists=True, blank=True)
    blog_feed = models.URLField(verbose_name=_("blog (feed)"), verify_exists=True, blank=True)
    tags = TagField(verbose_name=_("tags"), blank=True)
    email = models.EmailField(verbose_name=_("e-mail"), blank=True)


class Staff(models.Model):
    person = models.ForeignKey("Person")
    company = models.ForeignKey("Company")

    position = models.CharField(verbose_name=_("position"), max_length=100)
    start = models.DateField(verbose_name=_("start"))
    end = models.DateField(verbose_name=_("end"))


# Investment

class InvestorCategory(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)

    class Meta:
        verbose_name_plural = "company categories"

    def __unicode__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    logo = models.ImageField(verbose_name=_("logo"), upload_to="company_logo", height_field="logo_width", width_field="logo_height", blank=True)
    logo_width = models.IntegerField(blank=True, null=True)
    logo_height = models.IntegerField(blank=True, null=True)
    website = models.URLField(verbose_name=_("website"), verify_exists=True, blank=True)
    description = models.TextField(verbose_name=_("description"), blank=True)
    category = models.ForeignKey(InvestorCategory, verbose_name=_("category"), blank=True, null=True)
    twitter = models.CharField(verbose_name=_("twitter"), max_length=50, blank=True)
    linkedin = models.CharField(verbose_name=_("linkedin"), max_length=150, blank=True)
    address = models.CharField(verbose_name=_("address"), max_length=150, blank=True)
    tags = TagField(verbose_name=_("tags"), blank=True)
    email = models.EmailField(verbose_name=_("e-mail"), blank=True)

INVESTMENT_TYPES = (
    ('round-a', _("Round A")),
)
class Investment(models.Model):
    investor = models.ForeignKey("Investor")
    company = models.ForeignKey("Company")

    investment_type = models.CharField(verbose_name=_("type"), max_length=50, choices=INVESTMENT_TYPES, blank=True, null=True)
    amount = models.DecimalField(verbose_name=_("amount"), max_digits=12, decimal_places=2, blank=True, null=True)


# Company

class CompanyCategory(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)

    class Meta:
        verbose_name_plural = "company categories"

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    logo = models.ImageField(verbose_name=_("logo"), upload_to="company_logo", height_field="logo_width", width_field="logo_height", blank=True)
    logo_width = models.IntegerField(blank=True, null=True)
    logo_height = models.IntegerField(blank=True, null=True)
    website = models.URLField(verbose_name=_("website"), verify_exists=True, blank=True)
    description = models.TextField(verbose_name=_("description"), blank=True)
    category = models.ForeignKey(CompanyCategory, verbose_name=_("category"), blank=True, null=True)
    twitter = models.CharField(verbose_name=_("twitter"), max_length=50, blank=True)
    linkedin = models.CharField(verbose_name=_("linkedin"), max_length=150, blank=True)
    address = models.CharField(verbose_name=_("address"), max_length=150, blank=True)
    employees = models.IntegerField(verbose_name=_("employees"), blank=True, null=True)
    tags = TagField(verbose_name=_("tags"), blank=True)
    email = models.EmailField(verbose_name=_("e-mail"), blank=True)
    competitors = models.ManyToManyField("self",
                            symmetrical=False,
                        )
    investors = models.ManyToManyField("Investor",
                            through="Investment",
                            symmetrical=False,
                        )

    people = models.ManyToManyField("Person",
                            through="Staff",
                            symmetrical=False,
                        )


    class Meta:
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name


