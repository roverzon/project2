from overviews.models import Overview, overview_fields_map
import requests as req
import numpy as np

def alpha_vantage_overview_api(symbol):
    API_KEY = 'I7WB8M63PERU90OY'
    BASE_URL = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}={API_KEY}'.format(symbol, API_KEY)
    try:
        res = req.get(BASE_URL)
        json_response = res.json()
        if 'Symbol' not in json_response:
            print(f'Ticker: {symbol} Not in Overview Data'.format(symbol))
            pass
        else:
            overview = json_response
            for field in overview.copy():
                if field not in overview_fields_map.keys():
                    raise ValueError(f'Field: {field} is not in models'.format(field))

                for key in overview_fields_map.keys():
                    if key not in overview:
                        overview[overview_fields_map[key]] = 0.0
                    else:
                        if overview[key] == 'None' and key not in ['DividendDate', 'ExDividendDate', 'LastSplitDate']:
                            overview[overview_fields_map[key]] = 0.0
                        elif overview[key] == 'None' and key in ['DividendDate', 'ExDividendDate', 'LastSplitDate']:
                            overview[overview_fields_map[key]] = '1900-01-01'
                        else:
                            overview[overview_fields_map[key]] = overview[key]

            ov = Overview(
                symbol=symbol,
                overview_field1=overview['overview_field1'],
                overview_field2=overview['overview_field2'],
                overview_field3=overview['overview_field3'],
                overview_field4=overview['overview_field4'],
                overview_field5=overview['overview_field5'],
                overview_field6=overview['overview_field6'],
                overview_field7=overview['overview_field7'],
                overview_field8=overview['overview_field8'],
                overview_field9=overview['overview_field9'],
                overview_field10=overview['overview_field10'],
                overview_field11=overview['overview_field11'],
                overview_field12=overview['overview_field12'],
                overview_field13=overview['overview_field13'],
                overview_field14=overview['overview_field14'],
                overview_field15=overview['overview_field15'],
                overview_field16=overview['overview_field16'],
                overview_field17=overview['overview_field17'],
                overview_field18=overview['overview_field18'],
                overview_field19=overview['overview_field19'],
                overview_field20=overview['overview_field20'],
                overview_field21=overview['overview_field21'],
                overview_field22=overview['overview_field22'],
                overview_field23=overview['overview_field23'],
                overview_field24=overview['overview_field24'],
                overview_field25=overview['overview_field25'],
                overview_field26=overview['overview_field26'],
                overview_field27=overview['overview_field27'],
                overview_field28=overview['overview_field28'],
                overview_field29=overview['overview_field29'],
                overview_field30=overview['overview_field30'],
                overview_field31=overview['overview_field31'],
                overview_field32=overview['overview_field32'],
                overview_field33=overview['overview_field33'],
                overview_field34=overview['overview_field34'],
                overview_field35=overview['overview_field35'],
                overview_field36=overview['overview_field36'],
                overview_field37=overview['overview_field37'],
                overview_field38=overview['overview_field38'],
                overview_field39=overview['overview_field39'],
                overview_field40=overview['overview_field40'],
                overview_field41=overview['overview_field41'],
                overview_field42=overview['overview_field42'],
                overview_field43=overview['overview_field43'],
                overview_field44=overview['overview_field44'],
                overview_field45=overview['overview_field45'],
                overview_field46=overview['overview_field46'],
                overview_field47=overview['overview_field47'],
                overview_field48=overview['overview_field48'],
                overview_field49=overview['overview_field49'],
                overview_field50=overview['overview_field50'],
                overview_field51=overview['overview_field51'],
                overview_field52=overview['overview_field52'],
                overview_field53=overview['overview_field53'],
                overview_field54=overview['overview_field54'],
                overview_field55=overview['overview_field55'],
                overview_field56=overview['overview_field56'],
                overview_field57=overview['overview_field57'],
            )


            ov.save()
            print(f'Ticker: {symbol} Overview Data Saved'.format(symbol))

    except req.exceptions.RequestException as e:
        print(e)

