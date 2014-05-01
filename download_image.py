#!/usr/bin/python

import urllib
import os
import re
import sys

def crawl_image_from_url(url, filename):

    #print("crawling " + url + " ...")
    try: 
        f = open("/tmp/" + filename, 'wb')
        f.write(urllib.urlopen(url).read())
        f.close()
        os.system("/opt/hadoop/hadoop/bin/hdfs dfs -put /tmp/" + filename + " /user/hduser/images/" + filename)
    except Exception as e:
        return "Error: " + url

    return url

def regex_image(url):
    m = re.search('.*\/(.*)', url)
    return m.group(1)

for line in sys.stdin:
    line = line.strip()
    filename = regex_image(line)
    print crawl_image_from_url(line, filename)


