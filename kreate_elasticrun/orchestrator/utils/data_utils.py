import requests
import constants

def fetch_data(state, apmc, commodity, start_date, end_date):

    payload = str(constants.APMC_PAYLOAD)
    payload = payload.format(state, apmc, commodity, start_date, end_date)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "enam.gov.in",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "107",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", constants.APMC_ENDPOINT, data=payload, headers=headers)

    print(response.text)


def fetch_news(query):

    querystring = {"key": constants.GOOGLE_API_KEY, "q": query,
                   "cx": constants.GOOGLE_CSE}

    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "www.googleapis.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", constants.GOOGLE_SEARCH_URL, headers=headers, params=querystring)

    print(response.text)

def fetch_global_costs(query):

    url = "https://markets.ft.com/data/commodities/tearsheet/summary"

    querystring = {"c": "Wheat"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "f34b8c82-e56d-4225-b104-216cfbe08f6e,54c36691-a1c1-4ea0-a497-3959bec83523",
        'Host': "markets.ft.com",
        'Cookie': "1751%5F0=9098B036049FEFEDB0EAD3E3EF03510739188EDC3F81093D6204C86E1D135497; GZIP=1",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def fetch_mcx_price():
    import quandl
    quandl.ApiConfig.api_key = 'SHaVbA8FBUhGS59udfdB'
    ts = quandl.get('MCX/GMU2018', start_date='2018-08-30', end_date='2018-09-05')
    print(ts)

fetch_data('MAHARASHTRA', 'NAGPUR', 'WHEAT', '2017-01-01', '2019-01-01')
#fetch_global_costs("wheat")

#fetch_mcx_price()