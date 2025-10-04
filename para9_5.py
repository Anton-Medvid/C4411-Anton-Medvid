from bs4 import BeautifulSoup
import requests
res_parse_list = []
response = requests.get('https://coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('div', {'class': 'sc-fa25c04c-o'})
    #print(soup_list)
    '''for elem in soup_list:
        print(elem.find('<span>').text)
        res = soup_list[0].find('span')
    '''
    res = soup_list[0].find('span')
    print(res.text)