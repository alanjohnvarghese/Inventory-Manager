# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tool,ToolLog
# Register your models here.

#
admin.site.register(Tool)
admin.site.register(ToolLog)
