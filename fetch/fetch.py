#!/usr/bin/env python

import argparse
import urllib.request
import urllib.error
import urllib.parse


def main():
    urls = parseUrlsToList()
    for url in urls:
        try:
            fetchAndSaveWebPage(url)
        except Exception as e:
            print(url)
            print(e)


def parseUrlsToList():
    parser = argparse.ArgumentParser(
        description="Fetches web pages and saves them to disk")
    parser.add_argument('urls', metavar='urls', nargs='+',
                        help='a list of urls of web pages to download and save')
    args = parser.parse_args()
    return args.urls


def fetchAndSaveWebPage(url):
    webContent = fetchWebPage(url)
    saveToFile(url, webContent)


def fetchWebPage(url):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')
    return webContent


def saveToFile(url, webContent):
    filename = url.replace('https://', '')
    filename = filename.replace('http://', '')
    f = open(filename + '.html', 'w')
    f.write(webContent)
    f.close


if __name__ == "__main__":
    main()
