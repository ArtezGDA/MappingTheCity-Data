#!/usr/bin/python

import json

def main():
    """docstring for main"""
    with open('january_2016.json', 'r') as inputFile:
        scrapedData = json.load(inputFile)
    print "%d scrapedData" % (len(scrapedData))

if __name__ == '__main__':
    main()
