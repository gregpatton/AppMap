#!/usr/bin/python2.7 -tt
# Application Mapping with Python Experiment

import sys
import urllib, urllib2

def wgetoutput(url, outputfile):
  try:
    urllib.urlretrieve(url, outputfile)
    print 'Report Complete: ' + outputfile
  except IOError:
    print 'problem reading url:', url
  return

def wgetoutputpost(url, site, outputfile):
  try:
    params = urllib.urlencode({'remoteAddress' : site})
    req = urllib2.Request(url, params)
    req.add_header('Referer', 'http://www.yougetsignal.com/tools/web-sites-on-web-server/')
    r = urllib2.urlopen(req)
    f = open(outputfile,'w')
    f.write(r.read())
    print 'Report Complete: ' + outputfile
  except IOError:
    print 'problem reading url:', url
  return

def getsiteinfo(site):
    urlTechStack = 'http://builtwith.com/'
    urlWhoIs = 'http://who.is/whois/'
    urlOtherSites = 'http://www.yougetsignal.com/tools/web-sites-on-web-server/php/get-web-sites-on-web-server-json-data.php'
    wgetoutput(urlTechStack + site, 'builtwith.htm')
    wgetoutput(urlWhoIs + site, 'whois.htm')
    wgetoutputpost(urlOtherSites, site, 'sites.htm')
    return

def main():
    if len(sys.argv) >= 2:
        getsiteinfo(sys.argv[1])
        info = 'Analysis Complete.  View report.htm for results'
    else:
        info = 'No site provided in command line arguments'
    print info

if __name__ == '__main__':
	main()

