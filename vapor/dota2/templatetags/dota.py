from __future__ import absolute_import
from urlparse import urlparse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.shortcuts import redirect, render, get_object_or_404
from django import template

from time import mktime
from datetime import datetime

import steam
from dota2py import api

key = '870C28BC99B324034F4C0A9688311390'
api.set_api_key(key)
steam.api.key.set(key)

register = template.Library()



@register.filter
def steam_name(value):
	if value == 4294967295 or '':
		name = 'private'
		#name = steam.user.vanity_url(steam64)
		#name = steam64
	else:
		steam32 = int(value)
		steam64 = steam32+76561197960265728
		profile = steam.user.profile(str(steam64))
		name = profile.persona.encode('utf-8')
		#name = steam64
	return str(name)

@register.filter
def steam_time(value):
	ft = datetime.fromtimestamp(float(value))
	return ft

def get_heroes():
    res = steam.api.interface("IEconDOTA2_570").GetHeroes(language="en_US").get("result")
    return {x["id"]: x["localized_name"] for x in res.get("heroes")}

@register.filter
def get_hero_name(hero_id):
    try:
        return [get_heroes().get(x) for x in hero_id]
    except TypeError:
        return get_heroes().get(hero_id)
