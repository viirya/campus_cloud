#!/usr/bin/python

import urllib
import os
import re
import sys
from dateutil import parser

def parse_hashtags_from_tweet(tweet, created_at):

    time = parse_datetime_from_tweet(created_at)

    matches = re.findall('(#(?![#\s])(.(?!\s))*\S)', tweet)
    for match in matches:
        print match[0] + "\t" + str(time)

def parse_datetime_from_tweet(created_at):

    duration = parser.parse(created_at) - parser.parse("Thu Jan 1 00:00:00 +0000 2013")
    return duration.total_seconds()

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    created_at = fields[len(fields) - 1]
    tweet = " ".join(fields[0:len(fields) - 1])    
    if len(fields) >= 2:
        parse_hashtags_from_tweet(tweet, created_at)


