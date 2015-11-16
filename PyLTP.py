# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This example shows how to use Python to access the LTP API to perform full
# stack Chinese text analysis including word segmentation, POS tagging, dep-
# endency parsing, name entity recognization and semantic role labeling and
# get the result in specified format.

import urllib2, urllib
import sys

if __name__ == '__main__':
    uri_base = "http://ltpapi.voicecloud.cn/analysis/?"
    api_key  = "7132G4z1HE3SYMFjSAPvDSxtNcmA1jScSE5XumAI"

    f = open("E:\\PyProj\\Others\\rite_sentence.txt")
    fw = open("E:\\PyProj\\Others\\rite_pos.txt",'w')

    line = f.readline()
    while(line):
        text     = line
        # Note that if your text contain special characters such as linefeed or '&',
        # you need to use urlencode to encode your data
        text     = urllib.quote(text)
        format   = "plain"
        pattern  = "pos"

        url      = (uri_base
                   + "api_key=" + api_key + "&"
                   + "text="    + text    + "&"
                   + "format="  + format  + "&"
                   + "pattern=" + pattern)

        try:
            response = urllib2.urlopen(url)
            content  = response.read().strip()
            print content
            fw.write(line+content+'\n')
        except urllib2.HTTPError, e:
            print >> sys.stderr, e.reason
        line = f.readline()
    fw.close()
    f.close()


