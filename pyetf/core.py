import requests
import bs4
import re


categories = [
    "#etf-ticker-profile",
    "#etf-ticker-valuation-dividend",
    "#expense",
    "#holdings",
    "#performance",
    "#technicals",
    "#realtime-rating",
]

url = "https://etfdb.com/etf/SPY/"
spy = url + categories[0]
print(spy)

r = requests.get(spy)
soup = bs4.BeautifulSoup(r.text, 'html.parser')


def get_vitals_section(soup: bs4.BeautifulSoup):
    ticker_body = soup.find("div", {'id': 'etf-ticker-body'}).find('div', class_='row')
    vitals = {i.select_one(":nth-child(1)").text.strip(): i.select_one(":nth-child(2)").text.strip() for i in
              ticker_body.find_all('div', class_='row')}
    vitals.update({'Section': ticker_body.find('h3').text, 'Analyst Report': ticker_body.find('p').text.strip()})
    return vitals


def get_etf_database_theme(soup: bs4.BeautifulSoup):
    theme = soup.find("div", {'id' : 'etf-ticker-body'}).find_all('div', class_='ticker-assets')[1]
    theme_dict = {i.select_one(":nth-child(1)").text.strip() : i.select_one(":nth-child(2)").text.strip() for i in theme.find_all('div', class_='row')}
    theme_dict.update({'Section' :  'ETF Database Themes'} )
    return theme_dict


def get_factset_classification(soup: bs4.BeautifulSoup):
    factset = soup.find("div", {'id' : 'factset-classification'}).find_all('li')
    factset_dict = {i.select_one(":nth-child(1)").text.strip() : i.select_one(":nth-child(2)").text.strip() for i in factset}
    factset_dict.update({'Section' :  'FactSet Classifications'} )
    return factset_dict


def get_trading_data(soup: bs4.BeautifulSoup):
    trading_data =  soup.find("div", {'class': 'data-trading bar-charts-table'}).find_all('li')
    trading_dict = {i.select_one(":nth-child(1)").text.strip(): i.select_one(":nth-child(2)").text.strip() for i in trading_data}
    trading_dict.update({'Section' :  'Trading Data'} )
    return trading_dict


url2 = url + categories[1]
r2 = requests.get(url2)
soup = bs4.BeautifulSoup(r2.text, 'html.parser')


def get_etf_valuation(soup: bs4.BeautifulSoup):
    regex = re.compile('.*h4 center.*')
    valuation = soup.find('div', {'id': 'etf-ticker-valuation-dividend'}).find('div', {'id': 'valuation'}).find_all(
        'div', class_='row')
    values = [x.text for x in valuation[1].find_all('div', class_='text-center')]
    titles = [x.text for x in valuation[1].find_all('div', class_=regex)]
    results = dict(zip(titles, [{values[i], values[i + 1]} for i in range(len(values) // 2)]))
    return results

def get_etf_dividends(soup: bs4.BeautifulSoup):
    results = {}
    dividend = soup.find('div', {'id': 'etf-ticker-valuation-dividend'}).find('div', {'id': 'dividend'}).find('tbody')
    rows = [x.find_all('td') for x in dividend.find_all('tr')]
    category = None
    for row in rows:
        for idx, td in enumerate(row):
            data_th = td.get('data-th')
            text = td.text.strip()
            if idx == 0:
                category = text
                continue
            else:
                results[category] = {}
                results[category][data_th] = text

    return results

