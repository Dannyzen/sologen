#!/usr/bin/env python

import requests
import json
import os
from string import Template
import yaml

try:
    config = yaml.load(file('config.yaml', 'r'))
except yaml.YAMLError, exc:
    print "Do you have a config.yaml? If not, check out the README.md for more...", exc

key = config['key']
url = "https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key="
headers = {'content-type': 'application/json'}

def get_short_link(web_link):
    payload = {"dynamicLinkInfo":{"dynamicLinkDomain": "tamnews.page.link","link": web_link, "navigationInfo": { "enableForcedRedirect": "1"}, }, "suffix": { "option": "SHORT"}}
    response = requests.post( url+key, data=json.dumps(payload), headers=headers)
    extraction = json.loads(response.text)
    # print(extraction)
    short_link = extraction['shortLink']
    return short_link

def append_template_to_file(link, linkText, description):
    f=open("content.html", "a+")
    tempy = Template( '<a href="$linky">$linkyText</a>$descripty</br> \n')
    f.write(tempy.substitute(linky=link, linkyText=linkText, descripty=description))

def create_entry():
    web_link = raw_input('What is the link?: ')
    linkText = raw_input('What is the link text?: ')
    description = raw_input('What is the description: ')
    print("Just a sec, making the short link....")
    short_link = get_short_link(web_link)
    append_template_to_file(short_link, linkText, description)
    print("Wrote entry to content.html")

if len(key) < 0:
    print("Set an API Key")
else:
    while True:
        create_entry()
