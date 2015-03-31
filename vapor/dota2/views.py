import json
import urllib2
import functools
from time import mktime, strftime
from datetime import datetime
import requests

from gevent import monkey
monkey.patch_all()

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.cache import cache
from django.views.decorators.cache import cache_page

import steam
from dota2py import api

key = '870C28BC99B324034F4C0A9688311390'
api.set_api_key(key)
steam.api.key.set(key)
RECENT_MATCHES = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=JSON&matches_requested=10&tournament_games_only=1&key="

def LatestMatchesView(request):

	#LATEST_MATCHES_CACHE = 'latest_matches_public'
	#match_data = cache.get(LATEST_MATCHES_CACHE, None)
	#if not match_data:
#		match_data = api.get_match_history(matches_requested=10, min_players=4)["result"]["matches"]
#		cache.set(LATEST_MATCHES_CACHE, match_data, 60 * 15) # 15 minutes
	match_data = steam.api.interface("IDOTA2Match_570").GetMatchHistory(matches_requested=10, min_players=4)

	context = {'request': request, 'match_data': match_data, }
	return render_to_response('dota2/recent_matches.html', context,
		context_instance=RequestContext(request))

def LatestMatchesViewForUser(request):
	account_id = int(api.get_steam_id("underlost")["response"]["steamid"])
	matches = api.get_match_history(account_id=None)["result"]["matches"]
	context = {'request': request, 'matches': matches, }
	return render_to_response('dota2/matches.html', context,
		context_instance=RequestContext(request))

def LiveLeaguesView(request):
	matches = api.get_live_league_games()["result"]
	context = {'request':request, 'matches': matches,}
	return render_to_response('dota2/matches.html', context,
		context_instance=RequestContext(request))

def SingleMatch(request, match_id):
	match = api.get_match_details(match_id[0]["match_id"])
	context = {'request': request, 'match':match,}
	return render_to_response('dota2/match_detail.html', context,
		context_instance=RequestContext(request))

def LeagueListingView(request):
	leagues = api.get_league_listing()
	context = {'request':request, 'leagues': leagues,}
	return render_to_response('dota2/leagues.html', context,
		context_instance=RequestContext(request))

def HeroListView(request):
	heroes = api.get_heroes()
	context = {'request': request, 'heroes': heroes,}
	return render_to_response('dota2/heroes.html', context,
		context_instance=RequestContext(request))
