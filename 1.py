mport urllib2
import cookielib
cookie=cookie.cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=Ture,ignore_expires=Ture)
req=urllib2.Request(raw_input())
op=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(op)
response=opener.open(req)
print response.read()
