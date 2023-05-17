import banidb_local as banidb


def voice_search(text):


    shabad = banidb.search(text, searchtype=1)
    print('Total Results: ', shabad['total_results'])
    print('Total Pages: ', shabad['total_pages'])


    


    # # print(shabad)
    for i in range(shabad['total_pages']):

        print(f'page_{i + 1}: ', len(shabad['pages_data'][f'page_{i + 1}']))

        for j in range(len(shabad['pages_data'][f'page_{i + 1}'])):

            verse = shabad['pages_data'][f'page_{i + 1}'][j]['verse']
            shabad_id = shabad['pages_data'][f'page_{i + 1}'][j]['shabad_id']
            verse_id = shabad['pages_data'][f'page_{i + 1}'][j]['verse_id']
            print(f'result {j + 1} | {verse} | url: http://sttm.co/s/{shabad_id}/{verse_id}')

        print()
        print()

        

    # # print(shabad_id, verse_id)
    # # return shabad
    # # return f'shabad url: http://sttm.co/s/{shabad_id}/{verse_id}'

    #         print(f'result {i + 1} url: http://sttm.co/s/{shabad_id}/{verse_id}')
    # else:
    #     print(f'no results found please retry.')

# voice_search('GAkj')