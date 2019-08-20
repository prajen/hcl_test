#!/usr/bin/python

import urllib2
import json
import sys

try:
 if len(sys.argv) <= 1:
   print "Usage: macfetcher.py <MacAddress>"
   sys.exit(1)
 else:
  mac=sys.argv[1]
  url='https://api.macaddress.io/v1?apiKey=at_UaQyuVClWpZrHLSB6ZEy0necJUptr&output=json&search='+mac
  #print url
  response = urllib2.urlopen(url)
  data = json.load(response)
  vendor=data['vendorDetails']['companyName']
  if vendor:
   print "The vendor associated with MAC is :"+vendor
  else:
   print "There is something amiss with the MAC address"
   sys.exit(2)
except  urllib2.URLError:
 print "There is something wrong most likely a connection issue" 
