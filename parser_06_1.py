import datetime
import requests
from bs4 import BeautifulSoup as Bs
import csv


def write_cmc_top():
    url = "https://coinmarketcap.com/ru/"
    html = requests.get(url)
    soup = Bs(html.text, 'lxml')
    div = soup.find('div', class_="sc-ae0cff98-2 tLNRm")
    table = div.find('tbody')
    tr = table.find_all('tr', style="cursor:pointer")[:20]
    all_types = []
    coast = []
    int_coast = []
    for p in tr:
        value = p.find('p', {'font-weight': 'semibold'}).text
        coin = p.find('span', {'data-nosnippet': 'true', 'class': 'sc-11478e5d-1'}).text
        all_types.append(value)
        coast.append(coin[1:])
        int_coast.append(int(coin[1:].replace(',', '')))
    data_file_name = datetime.datetime.now().strftime("%H.%M. %d.%m.%Y") + '.csv'
    with open(data_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Name', 'MC', 'MP'])
        count = 0
        for row in range(len(all_types)):
            writer.writerow([all_types[count], coast[count], f'{round(int_coast[count] / sum(int_coast) * 100)}%'])
            count += 1
    print(f"Данные успешно записаны в файл: {data_file_name}")


write_cmc_top()