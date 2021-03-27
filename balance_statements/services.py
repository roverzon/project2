import logging
from balance_statements.models import BalanceSheet, balance_sheet_map
from pgfinancials.models import NoFinancialRecord
import requests as req
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry


def alpha_vantage_balance_sheet_api(symbol, report_type):
    logging.basicConfig(level=logging.DEBUG)
    API_KEY = 'I7WB8M63PERU90OY'
    BASE_URL = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}'.format(symbol, API_KEY)
    try:
        s = req.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        res = s.get(BASE_URL)
        json_response = res.json()
        if 'symbol' not in json_response:
            record = NoFinancialRecord(symbol=symbol, source='Alpha_Vantage', api_name='BALANCE_SHEET')
            record.save()
            print(f'Ticker: {symbol} No Balance Data'.format(symbol))
        else:
            symbol = json_response['symbol']
            balance_sheets = json_response[report_type]

            for balance_sheet in balance_sheets:
                for field in balance_sheet.keys():
                    if field not in balance_sheet_map.keys():
                        raise ValueError(f'Field: {field} is not in models'.format(field))

                for key in balance_sheet_map.keys():
                    if key not in balance_sheet:
                        balance_sheet[balance_sheet_map[key]] = 0.0
                    else:
                        if balance_sheet[key] == 'None':
                            balance_sheet[balance_sheet_map[key]] = 0.0
                        else:
                            balance_sheet[balance_sheet_map[key]] = balance_sheet[key]

                fiscal_date = balance_sheet['fiscalDateEnding']
                balance_sheet = BalanceSheet(
                    symbol=symbol,
                    report_type=report_type,
                    fiscal_year = fiscal_date.split('-')[0],
                    balance_statement_field1 = balance_sheet['balance_statement_field1'],
                    balance_statement_field2 = balance_sheet['balance_statement_field2'],
                    balance_statement_field3 = balance_sheet['balance_statement_field3'],
                    balance_statement_field4 = balance_sheet['balance_statement_field4'],
                    balance_statement_field5 = balance_sheet['balance_statement_field5'],
                    balance_statement_field6 = balance_sheet['balance_statement_field6'],
                    balance_statement_field7 = balance_sheet['balance_statement_field7'],
                    balance_statement_field8 = balance_sheet['balance_statement_field8'],
                    balance_statement_field10 = balance_sheet['balance_statement_field10'],
                    balance_statement_field11 = balance_sheet['balance_statement_field11'],
                    balance_statement_field12 = balance_sheet['balance_statement_field12'],
                    balance_statement_field13 = balance_sheet['balance_statement_field13'],
                    balance_statement_field14 = balance_sheet['balance_statement_field14'],
                    balance_statement_field15 = balance_sheet['balance_statement_field15'],
                    balance_statement_field16 = balance_sheet['balance_statement_field16'],
                    balance_statement_field17 = balance_sheet['balance_statement_field17'],
                    balance_statement_field18 = balance_sheet['balance_statement_field18'],
                    balance_statement_field19 = balance_sheet['balance_statement_field19'],
                    balance_statement_field20 = balance_sheet['balance_statement_field20'],
                    balance_statement_field21 = balance_sheet['balance_statement_field21'],
                    balance_statement_field22 = balance_sheet['balance_statement_field22'],
                    balance_statement_field23 = balance_sheet['balance_statement_field23'],
                    balance_statement_field24 = balance_sheet['balance_statement_field24'],
                    balance_statement_field25 = balance_sheet['balance_statement_field25'],
                    balance_statement_field26 = balance_sheet['balance_statement_field26'],
                    balance_statement_field27 = balance_sheet['balance_statement_field27'],
                    balance_statement_field28 = balance_sheet['balance_statement_field28'],
                    balance_statement_field29 = balance_sheet['balance_statement_field29'],
                    balance_statement_field30 = balance_sheet['balance_statement_field30'],
                    balance_statement_field31 = balance_sheet['balance_statement_field31'],
                    balance_statement_field32 = balance_sheet['balance_statement_field32'],
                    balance_statement_field33 = balance_sheet['balance_statement_field33'],
                    balance_statement_field34 = balance_sheet['balance_statement_field34'],
                    balance_statement_field35 = balance_sheet['balance_statement_field35'],
                    balance_statement_field36 = balance_sheet['balance_statement_field36'],
                    balance_statement_field37 = balance_sheet['balance_statement_field37'],
                    balance_statement_field38 = balance_sheet['balance_statement_field38'],
                    balance_statement_field39 = balance_sheet['balance_statement_field39'],
                    balance_statement_field40 = balance_sheet['balance_statement_field40'],
                    balance_statement_field41 = balance_sheet['balance_statement_field41'],
                    balance_statement_field42 = balance_sheet['balance_statement_field42'],
                    balance_statement_field43 = balance_sheet['balance_statement_field43'],
                    balance_statement_field44 = balance_sheet['balance_statement_field44'],
                    balance_statement_field45 = balance_sheet['balance_statement_field45'],
                    balance_statement_field46 = balance_sheet['balance_statement_field46'],
                    balance_statement_field47 = balance_sheet['balance_statement_field47'],
                    balance_statement_field48 = balance_sheet['balance_statement_field48'],
                    balance_statement_field49 = balance_sheet['balance_statement_field49'],
                    balance_statement_field50 = balance_sheet['balance_statement_field50'],
                    balance_statement_field51 = balance_sheet['balance_statement_field51'],
                    balance_statement_field52 = balance_sheet['balance_statement_field52'],
                    balance_statement_field53 = balance_sheet['balance_statement_field53'],
                    balance_statement_field54 = balance_sheet['balance_statement_field54'],
                    balance_statement_field55 = balance_sheet['balance_statement_field55'],
                    balance_statement_field56 = balance_sheet['balance_statement_field56'],
                    balance_statement_field57 = balance_sheet['balance_statement_field57'],
                    balance_statement_field58 = balance_sheet['balance_statement_field58'],
                    balance_statement_field59 = balance_sheet['balance_statement_field59'],
                    balance_statement_field60 = balance_sheet['balance_statement_field60'],
                    balance_statement_field61 = balance_sheet['balance_statement_field61'],
                    balance_statement_field62 = balance_sheet['balance_statement_field62'],
                    balance_statement_field63 = balance_sheet['balance_statement_field63'],
                    balance_statement_field64 = balance_sheet['balance_statement_field64'],
                )

                try:
                    balance_sheet.save()
                    print(f'Ticker: {symbol} & {report_type} Balance Sheet on {fiscal_date} Data Saved'.format(symbol, fiscal_date, report_type))
                except:
                    pass

    except req.exceptions.RequestException as e:
        print(e)
