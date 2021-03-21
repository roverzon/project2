from django.db import models


class Income(models.Model):
    symbol = models.CharField(max_length=255, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_year = models.CharField(max_length=10)
    reported_currency = models.CharField(max_length=10)
    income_statement_field1 = models.CharField(max_length=255, default='USD')
    income_statement_field2 = models.FloatField(default=0.0)
    income_statement_field3 = models.FloatField(default=0.0)
    income_statement_field4 = models.FloatField(default=0.0)
    income_statement_field5 = models.FloatField(default=0.0)
    income_statement_field6 = models.FloatField(default=0.0)
    income_statement_field7 = models.FloatField(default=0.0)
    income_statement_field8 = models.FloatField(default=0.0)
    income_statement_field9 = models.FloatField(default=0.0)
    income_statement_field10 = models.FloatField(default=0.0)
    income_statement_field11 = models.FloatField(default=0.0)
    income_statement_field12 = models.FloatField(default=0.0)
    income_statement_field13 = models.FloatField(default=0.0)
    income_statement_field14 = models.FloatField(default=0.0)
    income_statement_field15 = models.FloatField(default=0.0)
    income_statement_field16 = models.FloatField(default=0.0)
    income_statement_field17 = models.FloatField(default=0.0)
    income_statement_field18 = models.FloatField(default=0.0)
    income_statement_field19 = models.FloatField(default=0.0)
    income_statement_field20 = models.FloatField(default=0.0)
    income_statement_field21 = models.FloatField(default=0.0)
    income_statement_field22 = models.FloatField(default=0.0)
    income_statement_field23 = models.FloatField(default=0.0)
    income_statement_field24 = models.FloatField(default=0.0)
    income_statement_field25 = models.FloatField(default=0.0)
    income_statement_field26 = models.FloatField(default=0.0)
    income_statement_field27 = models.FloatField(default=0.0)
    income_statement_field28 = models.FloatField(default=0.0)
    income_statement_field29 = models.FloatField(default=0.0)
    income_statement_field30 = models.FloatField(default=0.0)
    income_statement_field31 = models.FloatField(default=0.0)
    income_statement_field32 = models.FloatField(default=0.0)
    income_statement_field33 = models.FloatField(default=0.0)
    income_statement_field34 = models.FloatField(default=0.0)
    income_statement_field35 = models.FloatField(default=0.0)
    income_statement_field36 = models.FloatField(default=0.0)
    income_statement_field37 = models.FloatField(default=0.0)
    income_statement_field38 = models.FloatField(default=0.0)
    income_statement_field39 = models.DateTimeField()
    income_statement_field40 = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('symbol', 'income_statement_field39')


income_statment_fields_map = {'reportedCurrency':'income_statement_field1',
                              'totalRevenue':'income_statement_field2',
                              'totalOperatingExpense':'income_statement_field3',
                              'costOfRevenue':'income_statement_field4',
                              'grossProfit':'income_statement_field5',
                              'ebit':'income_statement_field6',
                              'ebitda':'income_statement_field7',
                              'netIncome':'income_statement_field8',
                              'researchAndDevelopment':'income_statement_field9',
                              'effectOfAccounting_charges':'income_statement_field10',
                              'incomeBeforeTax':'income_statement_field11',
                              'minorityInterest':'income_statement_field12',
                              'sellingGeneralAdministrative':'income_statement_field13',
                              'otherNonOperatingIncome':'income_statement_field14',
                              'operatingIncome':'income_statement_field15',
                              'otherOperatingExpense':'income_statement_field16',
                              'interestExpense':'income_statement_field17',
                              'taxProvision':'income_statement_field18',
                              'interestIncome':'income_statement_field19',
                              'netInterestIncome':'income_statement_field20',
                              'extraordinaryItems':'income_statement_field21',
                              'nonRecurring':'income_statement_field22',
                              'otherItems':'income_statement_field23',
                              'incomeTaxExpense':'income_statement_field24',
                              'totalOtherIncomeExpense':'income_statement_field25',
                              'discontinuedOperations':'income_statement_field26',
                              'netIncomefromContinuingOperations':'income_statement_field27',
                              'netIncomeApplicableToCommonShares':'income_statement_field28',
                              'preferredStockAndOtherAdjustments':'income_statement_field29',
                              'costofGoodsAndServicesSold':'income_statement_field30',
                              'sellingGeneralAndAdministrative':'income_statement_field31',
                              'operatingExpenses':'income_statement_field32',
                              'investmentIncomeNet':'income_statement_field33',
                              'nonInterestIncome':'income_statement_field34',
                              'depreciation':'income_statement_field35',
                              'depreciationAndAmortization':'income_statement_field36',
                              'interestAndDebtExpense':'income_statement_field37',
                              'comprehensiveIncomeNetOfTax':'income_statement_field38',
                              'fiscalDateEnding': 'income_statement_field39',
                              'netIncomeFromContinuingOperations': 'income_statement_field40',
                              }

