from cash_flows.models import CashFlow, cash_flow_fields_map
from financials.models import NoFinancialRecord
import requests as req
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry


def alpha_vantage_cash_flow_api(symbol, report_type):
    API_KEY = 'I7WB8M63PERU90OY'
    BASE_URL = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}'.\
        format(symbol=symbol, API_KEY=API_KEY)
    try:
        s = req.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        res = s.get(BASE_URL)
        json_response = res.json()

        if 'symbol' not in json_response:
            record = NoFinancialRecord(symbol=symbol, source='Alpha_Vantage', api_name='CASH_FLOW')
            record.save()
            print(f'Ticker: {symbol} No Cash Flow Data'.format(symbol=symbol))
        else:
            symbol = json_response['symbol']
            cash_flows = json_response[report_type]

            for cash_flow in cash_flows:
                for field in cash_flow.keys():
                    if field not in cash_flow_fields_map.keys():
                        raise ValueError(f'Field: {field} is not in models'.format(field=field))

                for key in cash_flow_fields_map.keys():
                    if key not in cash_flow:
                        cash_flow[cash_flow_fields_map[key]] = 0.0
                    else:
                        if cash_flow[key] == 'None':
                            cash_flow[cash_flow_fields_map[key]] = 0.0
                        else:
                            cash_flow[cash_flow_fields_map[key]] = cash_flow[key]

                fiscal_date = cash_flow['fiscalDateEnding']
                cash = CashFlow(
                    symbol=symbol,
                    report_type=report_type,
                    fiscal_year = fiscal_date.split('-')[0],
                    cash_flow_field1 = cash_flow['cash_flow_field1'],
                    cash_flow_field2 = cash_flow['cash_flow_field2'],
                    cash_flow_field3 = cash_flow['cash_flow_field3'],
                    cash_flow_field4 = cash_flow['cash_flow_field4'],
                    cash_flow_field5 = cash_flow['cash_flow_field5'],
                    cash_flow_field6 = cash_flow['cash_flow_field6'],
                    cash_flow_field7 = cash_flow['cash_flow_field7'],
                    cash_flow_field8 = cash_flow['cash_flow_field8'],
                    cash_flow_field9 = cash_flow['cash_flow_field9'],
                    cash_flow_field10 = cash_flow['cash_flow_field10'],
                    cash_flow_field11 = cash_flow['cash_flow_field11'],
                    cash_flow_field12 = cash_flow['cash_flow_field12'],
                    cash_flow_field13 = cash_flow['cash_flow_field13'],
                    cash_flow_field14 = cash_flow['cash_flow_field14'],
                    cash_flow_field15 = cash_flow['cash_flow_field15'],
                    cash_flow_field16 = cash_flow['cash_flow_field16'],
                    cash_flow_field17 = cash_flow['cash_flow_field17'],
                    cash_flow_field18 = cash_flow['cash_flow_field18'],
                    cash_flow_field19 = cash_flow['cash_flow_field19'],
                    cash_flow_field20 = cash_flow['cash_flow_field20'],
                    cash_flow_field21 = cash_flow['cash_flow_field21'],
                    cash_flow_field22 = cash_flow['cash_flow_field22'],
                    cash_flow_field23 = cash_flow['cash_flow_field23'],
                    cash_flow_field24 = cash_flow['cash_flow_field24'],
                    cash_flow_field25 = cash_flow['cash_flow_field25'],
                    cash_flow_field26 = cash_flow['cash_flow_field26'],
                    cash_flow_field27 = cash_flow['cash_flow_field27'],
                    cash_flow_field28 = cash_flow['cash_flow_field28'],
                    cash_flow_field29 = cash_flow['cash_flow_field29'],
                    cash_flow_field30 = cash_flow['cash_flow_field30'],
                    cash_flow_field31 = cash_flow['cash_flow_field31'],
                    cash_flow_field32 = cash_flow['cash_flow_field32'],
                    cash_flow_field33 = cash_flow['cash_flow_field33'],
                    cash_flow_field34 = cash_flow['cash_flow_field34'],
                    cash_flow_field35 = cash_flow['cash_flow_field35'],
                    cash_flow_field36 = cash_flow['cash_flow_field36'],
                    cash_flow_field37 = cash_flow['cash_flow_field37'],
                    cash_flow_field38 = cash_flow['cash_flow_field38'],
                    cash_flow_field39 = cash_flow['cash_flow_field39'],
                    cash_flow_field40 = cash_flow['cash_flow_field40'],
                    cash_flow_field41 = cash_flow['cash_flow_field41'],
                    cash_flow_field42 = cash_flow['cash_flow_field42'],
                    cash_flow_field43 = cash_flow['cash_flow_field43'],
                )

                try:
                    cash.save()
                    print(f'Ticker: {symbol} & {report_type} Cash Flow on {fiscal_date} Data Saved'.
                          format(symbol=symbol, fiscal_date=fiscal_date, report_type=report_type))
                except:
                    pass

    except req.exceptions.RequestException as e:
        print(e)
