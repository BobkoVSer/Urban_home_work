import bs4
import requests as rq
import logging

import requests.exceptions

logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        soup = bs4.BeautifulSoup (response.txt, 'lxml')
        print(response)
    except:
        print('NoConnection')
    if response.status_code == 200:
        logging.basicConfig (filename= 'success_response.log', level=logging.INFO)
        logger.info (f'Info: {site}', extra ={'response': response.text})
    elif response.status_code != 200:
        logging.basicConfig(filename='bad_response.log', level=logging.WARNING)
        logger.warning (f'{site}', extra ={'response':response.text})
    else:
        logging.basicConfig(filename='blocked_response.log', level=logging.ERROR)
        logger.error(f'ERROR: {site}', extra = {'response' : "NoConnection"})


