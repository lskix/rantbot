import json
import requests

def searchWiki(phrase):

    searchUrl = "https://she-raandtheprincessesofpower.fandom.com/api/v1/Search/List?query="+ phrase.replace(" ", "+") +"&limit=1&minArticleQuality=10&batch=1&namespaces=0%2C14"
    response = requests.get(searchUrl)
    data = json.loads(response.content.decode('utf-8'))
    snippet = ""
    snippet = snippet + data['items'][0]['snippet'] + "... " + data['items'][0]['url']
    return snippet