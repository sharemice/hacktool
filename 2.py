import urllib2
import cookielib
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
response=opener.open(raw_input())
cookie.save(ignore_discard=Ture,ignore_expires=Ture)
