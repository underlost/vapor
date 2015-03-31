import functools
import steam
import re

from time import mktime
from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from steam import items
from steam import sim

import vapor.utils as steamutil

steam.api.key.set('870C28BC99B324034F4C0A9688311390')
steamutil.base.set_api_key('870C28BC99B324034F4C0A9688311390')

def VaporProfile(request, steam_id):
    vanity = steam.user.vanity_url(steam_id)
    id64 = str(vanity.id64)
    profile = steam.user.profile(id64)

    if profile.visibility == 3:
        games = steam.api.interface("IPlayerService").GetOwnedGames(steamid = id64, include_appinfo = 1, include_played_free_games = 1)
        game_count = games['response']['game_count']
        games_list = games['response']['games']

        games_played = []
        for game in games_list:
            if game['playtime_forever'] > 0:
                game['has_played'] = True
                games_played.append(game)
                
        context = { 'request': request, 'vanity_id': id64, 'game_count': game_count, 'games_list': games_list, 'games_played': games_played }
        return render_to_response('core/profile.html', context, context_instance=RequestContext(request))
    else:
        context = {'request': request,}
        return render_to_response('core/private.html', context, context_instance=RequestContext(request))


def VaporTF2Backback(request, steam_id):
    vanity = steam.user.vanity_url(steam_id)
    id64 = str(vanity.id64)
    profile = steam.user.profile(id64)
    if profile.visibility == 3:
        #bp = steam.api.interface("IEconItems_440").GetPlayerItems(steamid = id64)
        #backpack = steamutil.tf2.backpack(id64)
        BACKPACK_CACHE = '%s_BACKPACK_CACHE' % id64
        backpack = cache.get(BACKPACK_CACHE, None)
        if not backpack:
            backpack = steamutil.tf2.backpack(id64)
            cache.set(BACKPACK_CACHE, backpack, None) #Cache forever
        context = { 'request': request, 'vanity_id': id64, 'bp': backpack}
        return render_to_response('core/backpack.html', context, context_instance=RequestContext(request))
    else:
        context = {'request': request,}
        return render_to_response('core/private.html', context, context_instance=RequestContext(request))
