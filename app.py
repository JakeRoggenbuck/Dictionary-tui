import requests
import json
import api_key
import pprint
from termcolor import colored

word = input('Word: ')

full_url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key.key}'
request = requests.get(full_url)
json_ = request.json()

print(f'{word}')
print(colored('\nSynonyms\n', 'green'))
syn = [print(item['wd']) for item in json_[1]['def'][0]['sseq'][0][0][1]['syn_list'][0]]
print(colored('\nAntonyms\n', 'red'))
ant = [print(item['wd']) for item in json_[1]['def'][0]['sseq'][0][0][1]['ant_list'][0]]
