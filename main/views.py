#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('main/index.html', context_instance=RequestContext(request))

