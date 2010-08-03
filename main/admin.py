#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-


from django.contrib import admin

from main.models import Company, CompanyCategory


class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(CompanyCategory, CompanyCategoryAdmin)

class CompanyAdmin(admin.ModelAdmin):
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
admin.site.register(Company, CompanyAdmin)
