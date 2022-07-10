# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
from colorama import Back, Style

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')

    # json file
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    
    # text file
    with open('joker.txt', 'w') as dataFile:
        dataFile.write(r.json()['value'])

    # print
    print(f'{Back.BLUE}{r.json()}{Style.RESET_ALL}')

    return 1
