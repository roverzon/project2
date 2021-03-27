import logging
from polygon import RESTClient
from pgfinancials.models import Financial,NoFinancialRecord, pg_financial_map


def polygon_financial_api(symbol):
    logging.basicConfig(level=logging.DEBUG)
    with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
        try:
            rep = client.reference_stock_financials(symbol=symbol, limit=50)
            financials = rep.results

            if len(financials) == 0:
                record = NoFinancialRecord(symbol=symbol, source='Polygon', api_name='financial')
                record.save()
                print(f'Symbol:{symbol} has no data in Polygon.io'.format(symbol))
            else:
                for financial in financials:
                    for field in financial.keys():
                        if field not in pg_financial_map.keys():
                            raise ValueError(f'Field: {field} is not in models'.format(field))
                    for key in pg_financial_map.keys():
                        if key not in financial:
                            financial[pg_financial_map[key]] = 0.0
                        else:
                            financial[pg_financial_map[key]] = financial[key]

                    date_key = financial['pgfinancial_field5']
                    f = Financial(
                        symbol=symbol,
                        pgfinancial_field1 = financial['pgfinancial_field1'],
                        pgfinancial_field2 = financial['pgfinancial_field2'],
                        pgfinancial_field3 = financial['pgfinancial_field3'],
                        pgfinancial_field4 = financial['pgfinancial_field4'],
                        pgfinancial_field5 = financial['pgfinancial_field5'],
                        pgfinancial_field6 = financial['pgfinancial_field6'],
                        pgfinancial_field7 = financial['pgfinancial_field7'],
                        pgfinancial_field8 = financial['pgfinancial_field8'],
                        pgfinancial_field9 = financial['pgfinancial_field9'],
                        pgfinancial_field10 = financial['pgfinancial_field10'],
                        pgfinancial_field11 = financial['pgfinancial_field11'],
                        pgfinancial_field12 = financial['pgfinancial_field12'],
                        pgfinancial_field13 = financial['pgfinancial_field13'],
                        pgfinancial_field14 = financial['pgfinancial_field14'],
                        pgfinancial_field15 = financial['pgfinancial_field15'],
                        pgfinancial_field16 = financial['pgfinancial_field16'],
                        pgfinancial_field17 = financial['pgfinancial_field17'],
                        pgfinancial_field18 = financial['pgfinancial_field18'],
                        pgfinancial_field19 = financial['pgfinancial_field19'],
                        pgfinancial_field20 = financial['pgfinancial_field20'],
                        pgfinancial_field21 = financial['pgfinancial_field21'],
                        pgfinancial_field22 = financial['pgfinancial_field22'],
                        pgfinancial_field23 = financial['pgfinancial_field23'],
                        pgfinancial_field24 = financial['pgfinancial_field24'],
                        pgfinancial_field25 = financial['pgfinancial_field25'],
                        pgfinancial_field26 = financial['pgfinancial_field26'],
                        pgfinancial_field27 = financial['pgfinancial_field27'],
                        pgfinancial_field28 = financial['pgfinancial_field28'],
                        pgfinancial_field29 = financial['pgfinancial_field29'],
                        pgfinancial_field30 = financial['pgfinancial_field30'],
                        pgfinancial_field31 = financial['pgfinancial_field31'],
                        pgfinancial_field32 = financial['pgfinancial_field32'],
                        pgfinancial_field33 = financial['pgfinancial_field33'],
                        pgfinancial_field34 = financial['pgfinancial_field34'],
                        pgfinancial_field35 = financial['pgfinancial_field35'],
                        pgfinancial_field36 = financial['pgfinancial_field36'],
                        pgfinancial_field37 = financial['pgfinancial_field37'],
                        pgfinancial_field38 = financial['pgfinancial_field38'],
                        pgfinancial_field39 = financial['pgfinancial_field39'],
                        pgfinancial_field40 = financial['pgfinancial_field40'],
                        pgfinancial_field41 = financial['pgfinancial_field41'],
                        pgfinancial_field42 = financial['pgfinancial_field42'],
                        pgfinancial_field43 = financial['pgfinancial_field43'],
                        pgfinancial_field44 = financial['pgfinancial_field44'],
                        pgfinancial_field45 = financial['pgfinancial_field45'],
                        pgfinancial_field46 = financial['pgfinancial_field46'],
                        pgfinancial_field47 = financial['pgfinancial_field47'],
                        pgfinancial_field48 = financial['pgfinancial_field48'],
                        pgfinancial_field49 = financial['pgfinancial_field49'],
                        pgfinancial_field50 = financial['pgfinancial_field50'],
                        pgfinancial_field51 = financial['pgfinancial_field51'],
                        pgfinancial_field52 = financial['pgfinancial_field52'],
                        pgfinancial_field53 = financial['pgfinancial_field53'],
                        pgfinancial_field54 = financial['pgfinancial_field54'],
                        pgfinancial_field55 = financial['pgfinancial_field55'],
                        pgfinancial_field56 = financial['pgfinancial_field56'],
                        pgfinancial_field57 = financial['pgfinancial_field57'],
                        pgfinancial_field58 = financial['pgfinancial_field58'],
                        pgfinancial_field59 = financial['pgfinancial_field59'],
                        pgfinancial_field60 = financial['pgfinancial_field60'],
                        pgfinancial_field61 = financial['pgfinancial_field61'],
                        pgfinancial_field62 = financial['pgfinancial_field62'],
                        pgfinancial_field63 = financial['pgfinancial_field63'],
                        pgfinancial_field64 = financial['pgfinancial_field64'],
                        pgfinancial_field65 = financial['pgfinancial_field65'],
                        pgfinancial_field66 = financial['pgfinancial_field66'],
                        pgfinancial_field67 = financial['pgfinancial_field67'],
                        pgfinancial_field68 = financial['pgfinancial_field68'],
                        pgfinancial_field69 = financial['pgfinancial_field69'],
                        pgfinancial_field70 = financial['pgfinancial_field70'],
                        pgfinancial_field71 = financial['pgfinancial_field71'],
                        pgfinancial_field72 = financial['pgfinancial_field72'],
                        pgfinancial_field73 = financial['pgfinancial_field73'],
                        pgfinancial_field74 = financial['pgfinancial_field74'],
                        pgfinancial_field75 = financial['pgfinancial_field75'],
                        pgfinancial_field76 = financial['pgfinancial_field76'],
                        pgfinancial_field77 = financial['pgfinancial_field77'],
                        pgfinancial_field78 = financial['pgfinancial_field78'],
                        pgfinancial_field79 = financial['pgfinancial_field79'],
                        pgfinancial_field80 = financial['pgfinancial_field80'],
                        pgfinancial_field81 = financial['pgfinancial_field81'],
                        pgfinancial_field82 = financial['pgfinancial_field82'],
                        pgfinancial_field83 = financial['pgfinancial_field83'],
                        pgfinancial_field84 = financial['pgfinancial_field84'],
                        pgfinancial_field85 = financial['pgfinancial_field85'],
                        pgfinancial_field86 = financial['pgfinancial_field86'],
                        pgfinancial_field87 = financial['pgfinancial_field87'],
                        pgfinancial_field88 = financial['pgfinancial_field88'],
                        pgfinancial_field89 = financial['pgfinancial_field89'],
                        pgfinancial_field90 = financial['pgfinancial_field90'],
                        pgfinancial_field91 = financial['pgfinancial_field91'],
                        pgfinancial_field92 = financial['pgfinancial_field92'],
                        pgfinancial_field93 = financial['pgfinancial_field93'],
                        pgfinancial_field94 = financial['pgfinancial_field94'],
                        pgfinancial_field95 = financial['pgfinancial_field95'],
                        pgfinancial_field96 = financial['pgfinancial_field96'],
                        pgfinancial_field97 = financial['pgfinancial_field97'],
                        pgfinancial_field98 = financial['pgfinancial_field98'],
                        pgfinancial_field99 = financial['pgfinancial_field99'],
                        pgfinancial_field100 = financial['pgfinancial_field100'],
                        pgfinancial_field101 = financial['pgfinancial_field101'],
                        pgfinancial_field102 = financial['pgfinancial_field102'],
                        pgfinancial_field103 = financial['pgfinancial_field103'],
                        pgfinancial_field104 = financial['pgfinancial_field104'],
                        pgfinancial_field105 = financial['pgfinancial_field105'],
                        pgfinancial_field106 = financial['pgfinancial_field106'],
                        pgfinancial_field107 = financial['pgfinancial_field107'],
                        pgfinancial_field108 = financial['pgfinancial_field108'],
                        pgfinancial_field109 = financial['pgfinancial_field109'],
                    )

                    f.save()
                    print(f'Ticker: {symbol} & {date_key} Financial Data Saved'.format(symbol, date_key))
        except:
            ValueError(f'Symbol:{symbol} has no data in Polygon.io'.format(symbol))
