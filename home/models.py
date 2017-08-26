# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
"""
class UserProfile(models.Model):
    friends=models.ManyToManyField("self",related_name="friends",)
    user=models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE)

def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile=UserProfile(user=user)
        user_profile.save()
post_save.connect(create_user_profile,sender=User)

"""

class Tool(models.Model):
    name = models.CharField(max_length=200,default="tool")
    tool_id = models.CharField(max_length=20,primary_key=True)
    current = models.ForeignKey(User,default=None,null=True,blank=True)
    current_time = models.DateTimeField(default=None,null=True,blank=True)
    
    def __str__(self):
        return self.tool_id + " - " + self.name

class ToolLog(models.Model):
    tool = models.ForeignKey(Tool)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.datetime.now())
    status = models.IntegerField(default=1) # 1 = put; 0 = get  

    def __str__(self):
        if self.status:
            return self.tool.name + " returned by " + self.user.username
        else:
            return self.tool.name + " taken by " + self.user.username
        
