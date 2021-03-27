from income_statements.models import Income, income_statment_fields_map
import requests as req
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry


def alpha_vantage_income_statement_api(symbol, report_type):
    API_KEY = 'I7WB8M63PERU90OY'
    BASE_URL = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'.format(symbol, API_KEY)
    try:
        s = req.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        res = s.get(BASE_URL)
        json_response = res.json()
        if 'symbol' not in json_response:
            print(f'Ticker: {symbol} No Income Statement Data'.format(symbol))
            print(json_response)
            pass
        else:
            symbol = json_response['symbol']
            income_statements = json_response[report_type]

            for income_statement in income_statements:

                for field in income_statement.keys():
                    if field not in income_statment_fields_map.keys():
                        raise ValueError(f'Field: {field} is not in models'.format(field))

                for key in income_statment_fields_map.keys():
                    if key not in income_statement:
                        income_statement[income_statment_fields_map[key]] = 0.0
                    else:
                        if income_statement[key] == 'None':
                            income_statement[income_statment_fields_map[key]] = 0.0
                        else:
                            income_statement[income_statment_fields_map[key]] = income_statement[key]

                fiscal_date = income_statement['fiscalDateEnding']
                income = Income(
                    symbol=symbol,
                    report_type=report_type,
                    fiscal_year = fiscal_date.split('-')[0],
                    income_statement_field1 = income_statement['income_statement_field1'],
                    income_statement_field2 = income_statement['income_statement_field2'],
                    income_statement_field3 = income_statement['income_statement_field3'],
                    income_statement_field4 = income_statement['income_statement_field4'],
                    income_statement_field5 = income_statement['income_statement_field5'],
                    income_statement_field6 = income_statement['income_statement_field6'],
                    income_statement_field7 = income_statement['income_statement_field7'],
                    income_statement_field8 = income_statement['income_statement_field8'],
                    income_statement_field9 = income_statement['income_statement_field9'],
                    income_statement_field10 = income_statement['income_statement_field10'],
                    income_statement_field11 = income_statement['income_statement_field11'],
                    income_statement_field12 = income_statement['income_statement_field12'],
                    income_statement_field13 = income_statement['income_statement_field13'],
                    income_statement_field14 = income_statement['income_statement_field14'],
                    income_statement_field15 = income_statement['income_statement_field15'],
                    income_statement_field16 = income_statement['income_statement_field16'],
                    income_statement_field17 = income_statement['income_statement_field17'],
                    income_statement_field18 = income_statement['income_statement_field18'],
                    income_statement_field19 = income_statement['income_statement_field19'],
                    income_statement_field20 = income_statement['income_statement_field20'],
                    income_statement_field21 = income_statement['income_statement_field21'],
                    income_statement_field22 = income_statement['income_statement_field22'],
                    income_statement_field23 = income_statement['income_statement_field23'],
                    income_statement_field24 = income_statement['income_statement_field24'],
                    income_statement_field25 = income_statement['income_statement_field25'],
                    income_statement_field26 = income_statement['income_statement_field26'],
                    income_statement_field27 = income_statement['income_statement_field27'],
                    income_statement_field28 = income_statement['income_statement_field28'],
                    income_statement_field29 = income_statement['income_statement_field29'],
                    income_statement_field30 = income_statement['income_statement_field30'],
                    income_statement_field31 = income_statement['income_statement_field31'],
                    income_statement_field32 = income_statement['income_statement_field32'],
                    income_statement_field33 = income_statement['income_statement_field33'],
                    income_statement_field34 = income_statement['income_statement_field34'],
                    income_statement_field35 = income_statement['income_statement_field35'],
                    income_statement_field36 = income_statement['income_statement_field36'],
                    income_statement_field37 = income_statement['income_statement_field37'],
                    income_statement_field38 = income_statement['income_statement_field38'],
                    income_statement_field39 = income_statement['income_statement_field39'],
                    income_statement_field40 = income_statement['income_statement_field40'],
                )

                try:
                    income.save()
                    print(f'Ticker: {symbol} & {report_type} income statement on {fiscal_date} Data Saved'.format(symbol, fiscal_date, report_type))
                except:
                    pass

    except req.exceptions.RequestException as e:
        print(e)
