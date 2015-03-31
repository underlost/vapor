import json
import os
import urllib2
from time import strftime
import datetime
from optparse import make_option
import requests

from django.core.management.base import BaseCommand
from django.core.cache import cache

from dota2py import api

key = '870C28BC99B324034F4C0A9688311390'
RECENT_MATCHES = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=JSON&matches_requested=10&tournament_games_only=1&key="

class Command(BaseCommand):
    help = 'Fetches the recent matches from the web api and caches them.'

    def handle(self, **options):

        try:
            LATEST_MATCHES_CACHE = 'latest_matches_public'
            match_data = cache.get(LATEST_MATCHES_CACHE, None)
            if not match_data:
                match_data = api.get_match_history()["result"]["matches"]
                cache.set(LATEST_MATCHES_CACHE, match_data, 60 * 15) # 15 minutes
                print "Processing..."

        finally:
            print "Caching complete!"
