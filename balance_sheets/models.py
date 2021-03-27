from django.db import models


class BalanceSheet(models.Model):
    symbol = models.CharField(max_length=10, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_year = models.CharField(max_length=10, default='1900-01-01')
    balance_statement_field1 = models.CharField(max_length=255, default='USD')
    balance_statement_field2 = models.FloatField(default=0.0)
    balance_statement_field3 = models.FloatField(default=0.0)
    balance_statement_field4 = models.FloatField(default=0.0)
    balance_statement_field5 = models.FloatField(default=0.0)
    balance_statement_field6 = models.FloatField(default=0.0)
    balance_statement_field7 = models.FloatField(default=0.0)
    balance_statement_field8 = models.FloatField(default=0.0)
    balance_statement_field10 = models.FloatField(default=0.0)
    balance_statement_field11 = models.FloatField(default=0.0)
    balance_statement_field12 = models.FloatField(default=0.0)
    balance_statement_field13 = models.FloatField(default=0.0)
    balance_statement_field14 = models.FloatField(default=0.0)
    balance_statement_field15 = models.FloatField(default=0.0)
    balance_statement_field16 = models.FloatField(default=0.0)
    balance_statement_field17 = models.FloatField(default=0.0)
    balance_statement_field18 = models.FloatField(default=0.0)
    balance_statement_field19 = models.FloatField(default=0.0)
    balance_statement_field20 = models.FloatField(default=0.0)
    balance_statement_field21 = models.FloatField(default=0.0)
    balance_statement_field22 = models.FloatField(default=0.0)
    balance_statement_field23 = models.FloatField(default=0.0)
    balance_statement_field24 = models.FloatField(default=0.0)
    balance_statement_field25 = models.FloatField(default=0.0)
    balance_statement_field26 = models.FloatField(default=0.0)
    balance_statement_field27 = models.FloatField(default=0.0)
    balance_statement_field28 = models.FloatField(default=0.0)
    balance_statement_field29 = models.FloatField(default=0.0)
    balance_statement_field30 = models.FloatField(default=0.0)
    balance_statement_field31 = models.FloatField(default=0.0)
    balance_statement_field32 = models.FloatField(default=0.0)
    balance_statement_field33 = models.FloatField(default=0.0)
    balance_statement_field34 = models.FloatField(default=0.0)
    balance_statement_field35 = models.FloatField(default=0.0)
    balance_statement_field36 = models.FloatField(default=0.0)
    balance_statement_field37 = models.FloatField(default=0.0)
    balance_statement_field38 = models.FloatField(default=0.0)
    balance_statement_field39 = models.FloatField(default=0.0)
    balance_statement_field40 = models.FloatField(default=0.0)
    balance_statement_field41 = models.FloatField(default=0.0)
    balance_statement_field42 = models.FloatField(default=0.0)
    balance_statement_field43 = models.FloatField(default=0.0)
    balance_statement_field44 = models.FloatField(default=0.0)
    balance_statement_field45 = models.FloatField(default=0.0)
    balance_statement_field46 = models.FloatField(default=0.0)
    balance_statement_field47 = models.FloatField(default=0.0)
    balance_statement_field48 = models.FloatField(default=0.0)
    balance_statement_field49 = models.FloatField(default=0.0)
    balance_statement_field50 = models.FloatField(default=0.0)
    balance_statement_field51 = models.FloatField(default=0.0)
    balance_statement_field52 = models.FloatField(default=0.0)
    balance_statement_field53 = models.FloatField(default=0.0)
    balance_statement_field54 = models.FloatField(default=0.0)
    balance_statement_field55 = models.FloatField(default=0.0)
    balance_statement_field56 = models.FloatField(default=0.0)
    balance_statement_field57 = models.FloatField(default=0.0)
    balance_statement_field58 = models.FloatField(default=0.0)
    balance_statement_field59 = models.FloatField(default=0.0)
    balance_statement_field60 = models.FloatField(default=0.0)
    balance_statement_field61 = models.FloatField(default=0.0)
    balance_statement_field62 = models.FloatField(default=0.0)
    balance_statement_field63 = models.FloatField(default=0.0)
    balance_statement_field64 = models.DateTimeField(default='1900-01-01')

    class Meta:
        unique_together = ('symbol', 'balance_statement_field64')


balance_sheet_map = {'reportedCurrency':'balance_statement_field1',
                     'totalAssets':'balance_statement_field2',
                     'intangibleAssets':'balance_statement_field3',
                     'earningAssets':'balance_statement_field4',
                     'otherCurrentAssets':'balance_statement_field5',
                     'totalLiabilities':'balance_statement_field6',
                     'totalShareholderEquity':'balance_statement_field7',
                     'deferredLongTermLiabilities':'balance_statement_field8',
                     'otherCurrentLiabilities':'balance_statement_field9',
                     'commonStock':'balance_statement_field10',
                     'retainedEarnings':'balance_statement_field11',
                     'otherLiabilities':'balance_statement_field12',
                     'goodwill':'balance_statement_field13',
                     'otherAssets':'balance_statement_field14',
                     'cash':'balance_statement_field15',
                     'totalCurrentLiabilities':'balance_statement_field16',
                     'shortTermDebt':'balance_statement_field17',
                     'currentLongTermDebt':'balance_statement_field18',
                     'otherShareholderEquity':'balance_statement_field19',
                     'propertyPlantEquipment':'balance_statement_field20',
                     'totalCurrentAssets':'balance_statement_field21',
                     'longTermInvestment':'balance_statement_field22',
                     'netTangibleAssets':'balance_statement_field23',
                     'shortTermInvestment':'balance_statement_field24',
                     'netReceivables':'balance_statement_field25',
                     'longTermDebt':'balance_statement_field26',
                     'inventory':'balance_statement_field27',
                     'accountsPayable':'balance_statement_field28',
                     'totalPermanentEquity':'balance_statement_field29',
                     'additionalPaidInCapital':'balance_statement_field30',
                     'commonStockTotalEquity':'balance_statement_field31',
                     'preferredStockTotalEquity':'balance_statement_field32',
                     'retainedEarningsTotalEquity':'balance_statement_field33',
                     'treasuryStock':'balance_statement_field34',
                     'accumulatedAmortization':'balance_statement_field35',
                     'otherNonCurrentAssets':'balance_statement_field36',
                     'totalNonCurrentAssets':'balance_statement_field37',
                     'capitalLeaseObligations':'balance_statement_field38',
                     'totalLongTermDebt':'balance_statement_field39',
                     'otherNonCurrentLiabilities':'balance_statement_field40',
                     'deferredLongTermAssetCharges':'balance_statement_field41',
                     'totalNonCurrentLiabilities':'balance_statement_field42',
                     'negativeGoodwill':'balance_statement_field43',
                     'warrants':'balance_statement_field44',
                     'preferredStockRedeemable':'balance_statement_field45',
                     'capitalSurplus':'balance_statement_field46',
                     'liabilitiesAndShareholderEquity':'balance_statement_field47',
                     'cashAndShortTermInvestments':'balance_statement_field48',
                     'accumulatedDepreciation':'balance_statement_field49',
                     'commonStockSharesOutstanding':'balance_statement_field50',
                     'cashAndCashEquivalentsAtCarryingValue':'balance_statement_field51',
                     'currentNetReceivables':'balance_statement_field52',
                     'accumulatedDepreciationAmortizationPPE':'balance_statement_field53',
                     'intangibleAssetsExcludingGoodwill':'balance_statement_field54',
                     'investments':'balance_statement_field55',
                     'longTermInvestments':'balance_statement_field56',
                     'shortTermInvestments':'balance_statement_field57',
                     'otherNonCurrrentAssets':'balance_statement_field58',
                     'currentAccountsPayable':'balance_statement_field59',
                     'deferredRevenue':'balance_statement_field60',
                     'currentDebt':'balance_statement_field61',
                     'longTermDebtNoncurrent':'balance_statement_field62',
                     'shortLongTermDebtTotal':'balance_statement_field63',
                     'fiscalDateEnding':'balance_statement_field64'}
