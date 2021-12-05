#!/usr/bin/env python

import argparse
from bs4 import BeautifulSoup
import os.path
import time
import urllib.request


def main():
    parser = setUpArgumentsParser()
    args = parser.parse_args()

    if (args.metadata):
        generateMetadata(args.urls)
    else:
        fetchWebPages(args.urls)


def setUpArgumentsParser():
    parser = argparse.ArgumentParser(
        description='Fetches web pages and saves them to disk')
    parser.add_argument('urls', metavar='urls', nargs='+',
                        help='A list of urls of web pages to download and save')
    parser.add_argument('--metadata', action='store_true',
                        help='Use this flag to see the metadata related to the urls')
    return parser


def generateMetadata(urls):
    for url in urls:
        try:
            print()
            generateMetadataForUrl(url)
        except Exception as e:
            print(url)
            print(e)


def generateMetadataForUrl(url):
    site = generateSiteName(url)
    print('site:', site)
    filename = site + '.html'
    if (os.path.exists(filename)):
        printMetadata(filename)
    else:
        print('not yet fetched')


def printMetadata(filename):
    f = open(filename, 'r')
    webContent = f.read()
    f.close
    soup = BeautifulSoup(webContent, 'html.parser')
    links = soup.find_all('a')
    print('num_links:', len(links))
    images = soup.find_all('img')
    print('images:', len(images))
    fetchedTime = time.gmtime(os.path.getmtime(filename))
    print(time.strftime("last_fetch: %a %b %d %Y %H:%M UTC", fetchedTime))


def fetchWebPages(urls):
    for url in urls:
        try:
            fetchAndSaveWebPage(url)
        except Exception as e:
            print(url)
            print(e)


def fetchAndSaveWebPage(url):
    webContent = fetchWebPage(url)
    saveToFile(url, webContent)


def fetchWebPage(url):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')
    return webContent


def saveToFile(url, webContent):
    site = generateSiteName(url)
    f = open(site + '.html', 'w')
    f.write(webContent)
    f.close


def generateSiteName(url):
    filename = url.replace('https://', '')
    filename = filename.replace('http://', '')
    return filename


if __name__ == "__main__":
    main()
