from django.db import models
from django.utils import timezone


class Overview(models.Model):
    overview_field1=models.CharField(max_length=255, blank=False, default='')
    overview_field2=models.CharField(max_length=255, blank=False, default='')
    overview_field3=models.CharField(max_length=255, blank=False, default='')
    overview_field4=models.CharField(max_length=2000, blank=False, default='')
    overview_field5=models.CharField(max_length=255, blank=False, default='')
    overview_field6=models.CharField(max_length=255, blank=False, default='')
    overview_field7=models.CharField(max_length=255, blank=False, default='')
    overview_field8=models.CharField(max_length=255, blank=False, default='')
    overview_field9=models.CharField(max_length=255, blank=False, default='')
    overview_field10=models.CharField(max_length=255, blank=False, default='')
    overview_field11=models.DateTimeField(null=True)
    overview_field12=models.BigIntegerField(null=True)
    overview_field13=models.BigIntegerField(null=True)
    overview_field14=models.FloatField(null=True)
    overview_field15=models.FloatField(null=True)
    overview_field16=models.FloatField(null=True)
    overview_field17=models.FloatField(null=True)
    overview_field18=models.FloatField(null=True)
    overview_field19=models.FloatField(null=True)
    overview_field20=models.FloatField(null=True)
    overview_field21=models.FloatField(null=True)
    overview_field22=models.FloatField(null=True)
    overview_field23=models.FloatField(null=True)
    overview_field24=models.FloatField(null=True)
    overview_field25=models.BigIntegerField(null=True)
    overview_field26=models.BigIntegerField(null=True)
    overview_field27=models.FloatField(null=True)
    overview_field28=models.FloatField(null=True)
    overview_field29=models.FloatField(null=True)
    overview_field30=models.FloatField(null=True)
    overview_field31=models.FloatField(null=True)
    overview_field32=models.FloatField(null=True)
    overview_field33=models.FloatField(null=True)
    overview_field34=models.FloatField(null=True)
    overview_field35=models.FloatField(null=True)
    overview_field36=models.FloatField(null=True)
    overview_field37=models.FloatField(null=True)
    overview_field38=models.FloatField(null=True)
    overview_field39=models.FloatField(null=True)
    overview_field40=models.FloatField(null=True)
    overview_field41=models.FloatField(null=True)
    overview_field42=models.BigIntegerField(null=True)
    overview_field43=models.BigIntegerField(null=True)
    overview_field44=models.BigIntegerField(null=True)
    overview_field45=models.BigIntegerField(null=True)
    overview_field46=models.FloatField(null=True)
    overview_field47=models.FloatField(null=True)
    overview_field48=models.FloatField(null=True)
    overview_field49=models.FloatField(null=True)
    overview_field50=models.FloatField(null=True)
    overview_field51=models.FloatField(null=True)
    overview_field52=models.FloatField(null=True)
    overview_field53=models.FloatField(null=True)
    overview_field54=models.DateTimeField(null=True)
    overview_field55=models.DateTimeField(null=True)
    overview_field56=models.CharField(max_length=255, null=True)
    overview_field57=models.DateTimeField(null=True)
    overview_field58=models.DateTimeField(default=timezone.now)
    overview_field59=models.CharField(max_length=255, null=True)
    overview_field60=models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ('overview_field1', 'overview_field58')


overview_fields_map = {'Symbol' : 'overview_field1',
                       'AssetType' : 'overview_field2',
                       'Name' : 'overview_field3',
                       'Description' : 'overview_field4',
                       'Exchange' : 'overview_field5',
                       'Currency' : 'overview_field6',
                       'Sector' : 'overview_field7',
                       'Industry' : 'overview_field8',
                       'FullTimeEmployees' : 'overview_field9',
                       'FiscalYearEnd' : 'overview_field10',
                       'LatestQuarter' : 'overview_field11',
                       'MarketCapitalization' : 'overview_field12',
                       'EBITDA': 'overview_field13',
                       'PERatio': 'overview_field14',
                       'PEGRatio': 'overview_field15',
                       'BookValue': 'overview_field16',
                       'DividendPerShare': 'overview_field17',
                       'DividendYield': 'overview_field18',
                       'EPS': 'overview_field19',
                       'RevenuePerShareTTM' : 'overview_field20',
                       'ProfitMargin' : 'overview_field21',
                       'OperatingMarginTTM' : 'overview_field22',
                       'ReturnOnAssetsTTM' : 'overview_field23',
                       'ReturnOnEquityTTM' : 'overview_field24',
                       'RevenueTTM' : 'overview_field25',
                       'GrossProfitTTM' : 'overview_field26',
                       'DilutedEPSTTM' : 'overview_field27',
                       'QuarterlyEarningsGrowthYOY' : 'overview_field28',
                       'QuarterlyRevenueGrowthYOY' : 'overview_field29',
                       'AnalystTargetPrice' : 'overview_field30',
                       'TrailingPE' : 'overview_field31',
                       'ForwardPE' : 'overview_field32',
                       'PriceToSalesRatioTTM' : 'overview_field33',
                       'PriceToBookRatio' : 'overview_field34',
                       'EVToRevenue' : 'overview_field35',
                       'EVToEBITDA' : 'overview_field36',
                       'Beta' : 'overview_field37',
                       '52WeekHigh' : 'overview_field38',
                       '52WeekLow' : 'overview_field39',
                       '50DayMovingAverage' : 'overview_field40',
                       '200DayMovingAverage' : 'overview_field41',
                       'SharesOutstanding' : 'overview_field42',
                       'SharesFloat' : 'overview_field43',
                       'SharesShort' : 'overview_field44',
                       'SharesShortPriorMonth' : 'overview_field45',
                       'ShortRatio' : 'overview_field46',
                       'ShortPercentOutstanding' : 'overview_field47',
                       'ShortPercentFloat' : 'overview_field48',
                       'PercentInsiders' : 'overview_field49',
                       'PercentInstitutions' : 'overview_field50',
                       'ForwardAnnualDividendRate' : 'overview_field51',
                       'ForwardAnnualDividendYield' : 'overview_field52',
                       'PayoutRatio': 'overview_field53',
                       'DividendDate': 'overview_field54',
                       'ExDividendDate': 'overview_field55',
                       'LastSplitFactor': 'overview_field56',
                       'LastSplitDate': 'overview_field57',
                       'created_at': 'overview_field58',
                       'Country': 'overview_field59',
                       'Address': 'overview_field60',}
