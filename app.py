import requests
import json
import api_key
import pprint
from termcolor import colored


def get_words(word_json: dict, word_type: str) -> list:
    """Return list of words based on word type e.g. 'syn_list'"""
    try:
        return [item['wd'] for item in word_json[1]['def'][0]['sseq'][0][0][1][word_type][0]]
    except:
        raise Exception("Sorry, word not found")

def print_word_list(word_list: list):
    """Goes through the words and prints them"""
    for word in word_list:
        print(word)

if __name__ == "__main__":
    word = input('Word: ')

    word_url = f"references/thesaurus/json/{word}?key={api_key.key}"
    full_url = f"https://www.dictionaryapi.com/api/v3/{word_url}"
    request = requests.get(full_url)
    json_ = request.json()

    syn = get_words(json_, "syn_list")
    ant = get_words(json_, "ant_list")

    print(word)

    print(colored('\nSynonyms\n', 'green'))
    print(print_word_list(syn))

    print(colored('\nAntonyms\n', 'red'))
    print(print_word_list(ant))
