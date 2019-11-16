import os, requests, uuid, json

def translate(og_lang, new_langs, text):
    url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from=' + og_lang
    for new_lang in new_langs:
        params = params + "&to=" + new_lang
    final_url = url + path + params

    headers =   {
    'Ocp-Apim-Subscription-Key': '36ab09f8ddbf4945b7cb46cc56893e56',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    request = requests.post(final_url, headers=headers, json=body)
    response = request.json()
    return (response[0]['translations'])

def wiki_url(term, lang):
    url = "https://" + lang + ".wikipedia.org/w/index.php?search=" + term + "&title=Special%3ASearch&go=Go&ns0=1" 
    request = requests.post(url=url)
    print(request.url)

def search(og_lang, new_langs, term):
    translations = translate(og_lang, new_langs, term)
    wiki_url(term, og_lang)
    for translation in translations:
        wiki_url(translation['text'], translation['to'])

word = input("Enter a search term: ")
search('en', ['fr', 'de', 'it', 'nl', 'lv', 'nb'], word)
