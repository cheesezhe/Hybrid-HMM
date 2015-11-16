__author__ = 'Administrator'
#coding=utf-8
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
url = "http://baike.baidu.com/link?url=5iAUIFQF-Z0CHFwW1UrD-p_FOOkmnJ-7xbb-n4LSC3QSiy2mehcQuJXRSUp6cbN1nouDGul3IFZ6z40HAv6pk6EBN4EaBBTvdvh2w_cofs6HGpsBnGAs4sbFOyleFN3s"
n = 1
while(n<=10000):
    html = getHtml(url)
    print n
    print html