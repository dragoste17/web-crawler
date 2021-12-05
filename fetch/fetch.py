#!/usr/bin/env python

import urllib.request
import urllib.error
import urllib.parse

url = 'https://www.google.com'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

filename = url.replace('https://', '')
filename = filename.replace('http://', '')
f = open(filename + '.html', 'w')
f.write(webContent)
f.close
