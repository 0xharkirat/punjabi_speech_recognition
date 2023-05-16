import banidb_local as banidb


def voice_search(text):


    shabad = banidb.search(text, searchtype=0)


    shabad_id = shabad['pages_data']['page_1'][0]['shabad_id']
    verse_id = shabad['pages_data']['page_1'][0]['verse_id']

    # print(shabad_id, verse_id)
    # return shabad
    return f'shabad url: http://sttm.co/s/{shabad_id}/{verse_id}'

    # print(f'shabad url: http://sttm.co/s/{shabad_id}/{verse_id}')
