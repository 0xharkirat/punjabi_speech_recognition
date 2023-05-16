import requests

url = 'https://api.banidb.com/v2'


def search_type():
    types = {
        0: 'First letter each word from start (Gurmukhi)',
        1: 'First letter each word anywhere (Gurmukhi)',
        2: 'Full Word (Gurmukhi)',
        3: 'Full Word Translation (English)',
        4: 'Romanized Gurmukhi (English)',
        5: 'Ang',
        6: 'Main Letter (Gurmukhi)',
        7: 'Romanized first letter anywhere (English)'
    }
    return types


def search(query, searchtype=1, source='all', larivaar=False,
           ang=None, raag=None, writer='all', page=1, results=None):
    if len(query) > 2:
        res = f"{url}/search/{query}?"
        url_address = {
            'searchtype': searchtype,
            'source': source,
            'ang': ang,
            'raag': raag,
            'writer': writer,
            'page': page,
            'results': results
            }
        for i in url_address.keys():
            res = f"{res}{i}={url_address[i]}&"
        response = requests.get(res)
        json_blob = response.json()
        info = json_blob['resultsInfo']
        total_res = info['totalResults']
        results = {'total_results': total_res}
        current_page = info['pages']['page']
        total_pages = info['pages']['totalPages']  # Total Pages
        results['total_pages'] = total_pages
        pages = {}
        for page in range(current_page, total_pages+1):
            response = requests.get(res)
            json_blob = response.json()
            info = json_blob['resultsInfo']
            pg = f"page_{page}"
            verses = []
            for verse in json_blob['verses']:
                # print(verse)
                verse_dict = {'shabad_id': verse['shabadId'],
                              'verse_id': verse['verseId']
                              }
                if larivaar is True:
                    verse_dict['lari'] = verse['larivaar']['unicode']
                else:
                    verse_dict['verse'] = verse['verse']['unicode']
                verse_dict['steek'] = {
                    'en': verse['translation']['en']['bdb'],
                    'pu': verse['translation']['pu']['bdb']['unicode']
                    }
                verse_dict['source'] = {
                    'pu': verse['source']['unicode'],
                    'en': verse['source']['english'],
                    'ang': verse['pageNo'],
                    'raagpu': verse['raag']['unicode'],
                    'raagen': verse['raag']['english'],
                    'writer': verse['writer']['english'],
                    'verseId': verse['verseId']
                    
                    }
                verses.append(verse_dict)
            pages[pg] = verses
            if 'nextPage' in info['pages'].keys():
                res = info['pages']['nextPage']
        results['pages_data'] = pages
        return results

    else:
        raise Exception('Query length should be >= 3!')
    




