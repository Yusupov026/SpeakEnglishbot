import requests


app_id = "be28069f"
app_key = "80d714765747ebb5bf4e81a330d6d8d6"
language = "en-gb"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"{sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

# res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]["audioFile"]:
    audio = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]["audioFile"]
    return output,audio

if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('python'))

