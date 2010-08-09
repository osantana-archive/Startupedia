#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-


from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from reversion.admin import VersionAdmin

from main.models import Person
from main.models import Company
from main.models import CompanyCategory
from main.models import Investor
from main.models import InvestorCategory



class StaffInline(admin.StackedInline):
    model = Company.people.through
    extra = 1
    verbose_name = _("staff")
    verbose_name_plural = _("staff")

class InvestorsInline(admin.StackedInline):
    model = Company.investors.through
    extra = 1
    verbose_name = _("investor")
    verbose_name_plural = _("investors")

class CompetitorsInline(admin.StackedInline):
    model = Company.competitors.through
    fk_name = "from_company"
    extra = 1
    verbose_name = _("competitor")
    verbose_name_plural = _("competitors")

# Person
class PersonAdmin(VersionAdmin):
    list_display = (
        'name',
        'blog',
        'email',
        'twitter',
    )
    exclude = (
        'picture_width',
        'picture_height',
    )
admin.site.register(Person, PersonAdmin)


# Investor
class InvestorCategoryAdmin(VersionAdmin):
    list_display = (
        'name',
    )
admin.site.register(InvestorCategory, InvestorCategoryAdmin)

class InvestorAdmin(VersionAdmin):
    list_display = (
        'name',
        'website',
        'email',
        'twitter',
    )
    exclude = (
        'logo_width',
        'logo_height',
    )
admin.site.register(Investor, InvestorAdmin)


# Company
class CompanyCategoryAdmin(VersionAdmin):
    list_display = (
        'name',
    )
admin.site.register(CompanyCategory, CompanyCategoryAdmin)

class CompanyAdmin(VersionAdmin):
    list_display = (
        'name',
        'website',
        'email',
        'twitter',
    )
    exclude = (
        'logo_width',
        'logo_height',
        'competitors',
        'investors',
        'people',
    )
    inlines = (
        StaffInline,
        InvestorsInline,
        CompetitorsInline,
    )
admin.site.register(Company, CompanyAdmin)

