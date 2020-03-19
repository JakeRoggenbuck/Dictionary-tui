import requests
import json
import api_key

word = input('Word: ')

full_url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key.key}'
request = requests.get(full_url)
json_ = request.json()

print(json_)
