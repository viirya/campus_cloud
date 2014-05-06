#!/usr/bin/python

import urllib
import os
import re
import sys

def parse_hashtags_from_tweet(tweet):

    matches = re.findall('(#(?![#\s])(.(?!\s))*\S)', tweet)
    for match in matches:
        print match[0]


for line in sys.stdin:
    line = line.strip()
    parse_hashtags_from_tweet(line)


