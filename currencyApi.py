import requests

def transformMonoData(data):
    USD_ISO_CODE = 840
    EUR_ISO_CODE = 978
    UAH_ISO_CODE = 980
    usd = next(filter(lambda currency: currency['currencyCodeA'] == USD_ISO_CODE and currency['currencyCodeB'] == UAH_ISO_CODE, data), None)
    eur = next(filter(lambda currency: currency['currencyCodeA'] == EUR_ISO_CODE and currency['currencyCodeB'] == UAH_ISO_CODE, data), None)
    mdict = {
        'title': 'MONO',
        'USD': {
            'buy': usd['rateBuy'],
            'sell': usd['rateSell']
        }, 
        'EUR' : {
            'buy': eur['rateBuy'],
            'sell': eur['rateSell']  
        }
    }
    return mdict

def transformPrivatData(data):
    usd = next(filter(lambda currency: currency['ccy'] == 'USD', data), None)
    eur = next(filter(lambda currency: currency['ccy'] == 'EUR', data), None)
    pdict = {
        'title': 'PRIVAT',
        'USD': {
            'buy': usd['buy'],
            'sell': usd['sale']
        }, 
        'EUR' : {
            'buy': eur['buy'],
            'sell': eur['sale']  
        }
    }
    return pdict

privatData = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
monoData = requests.get('https://api.monobank.ua/bank/currency')
mdict = transformMonoData(monoData.json())
pdict = transformPrivatData(privatData.json())

print("{:^15.6}|{:^15.6}|{:^15.6}|".format('', mdict['title'], pdict['title']))
print("{:^15.8}|{:^15.2f}|{:^15.5}|".format('USD buy', mdict['USD']['buy'], pdict['USD']['buy']))
print("{:^15.8}|{:^15.2f}|{:^15.5}|".format('USD sell', mdict['USD']['sell'], pdict['USD']['sell']))
print("{:^15.8}|{:^15.2f}|{:^15.5}|".format('EUR buy', mdict['EUR']['buy'], pdict['EUR']['buy']))
print("{:^15.8}|{:^15.2f}|{:^15.5}|".format('EUR sell', mdict['EUR']['sell'], pdict['EUR']['sell']))