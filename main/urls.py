#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-

from django.conf.urls.defaults import patterns, handler404, handler500, url  #pylint:disable-msg=W0611

urlpatterns = patterns('',
    url(r'^$', 'main.views.index'),
)

