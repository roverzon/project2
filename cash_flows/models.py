from django.db import models


class CashFlow(models.Model):
    symbol = models.CharField(max_length=10, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_year = models.CharField(max_length=10, default='1900')
    cash_flow_field1 = models.FloatField(default=0.0)
    cash_flow_field2 = models.FloatField(default=0.0)
    cash_flow_field3 = models.FloatField(default=0.0)
    cash_flow_field4 = models.FloatField(default=0.0)
    cash_flow_field5 = models.FloatField(default=0.0)
    cash_flow_field6 = models.FloatField(default=0.0)
    cash_flow_field7 = models.FloatField(default=0.0)
    cash_flow_field8 = models.FloatField(default=0.0)
    cash_flow_field9 = models.FloatField(default=0.0)
    cash_flow_field10 = models.FloatField(default=0.0)
    cash_flow_field11 = models.FloatField(default=0.0)
    cash_flow_field12 = models.FloatField(default=0.0)
    cash_flow_field13 = models.FloatField(default=0.0)
    cash_flow_field14 = models.FloatField(default=0.0)
    cash_flow_field15 = models.FloatField(default=0.0)
    cash_flow_field16 = models.FloatField(default=0.0)
    cash_flow_field17 = models.FloatField(default=0.0)
    cash_flow_field18 = models.FloatField(default=0.0)
    cash_flow_field19 = models.FloatField(default=0.0)
    cash_flow_field20 = models.FloatField(default=0.0)
    cash_flow_field21 = models.FloatField(default=0.0)
    cash_flow_field22 = models.FloatField(default=0.0)
    cash_flow_field23 = models.FloatField(default=0.0)
    cash_flow_field24 = models.FloatField(default=0.0)
    cash_flow_field25 = models.FloatField(default=0.0)
    cash_flow_field26 = models.FloatField(default=0.0)
    cash_flow_field27 = models.FloatField(default=0.0)
    cash_flow_field28 = models.FloatField(default=0.0)
    cash_flow_field29 = models.FloatField(default=0.0)
    cash_flow_field30 = models.FloatField(default=0.0)
    cash_flow_field31 = models.FloatField(default=0.0)
    cash_flow_field32 = models.FloatField(default=0.0)
    cash_flow_field33 = models.FloatField(default=0.0)
    cash_flow_field34 = models.FloatField(default=0.0)
    cash_flow_field35 = models.FloatField(default=0.0)
    cash_flow_field36 = models.FloatField(default=0.0)
    cash_flow_field37 = models.FloatField(default=0.0)
    cash_flow_field38 = models.FloatField(default=0.0)
    cash_flow_field39 = models.FloatField(default=0.0)
    cash_flow_field40 = models.FloatField(default=0.0)
    cash_flow_field41 = models.FloatField(default=0.0)
    cash_flow_field42 = models.CharField(max_length=255, default='USD')
    cash_flow_field43 = models.DateTimeField()

    class Meta:
        unique_together = ('symbol', 'fiscal_date_ending')


cash_flow_fields_map = {'changeInLiabilities':'cash_flow_field1',
                        'OperatingCashflow':'cash_flow_field2',
                        'paymentsForOperatingActivities':'cash_flow_field3',
                        'proceedsFromOperatingActivities':'cash_flow_field4',
                        'changeInOperating_liabilities':'cash_flow_field5',
                        'changeInOperating_assets':'cash_flow_field6',
                        'depreciation_depletion_and_amortization':'cash_flow_field7',
                        'capitalExpenditures':'cash_flow_field8',
                        'changeInReceivables':'cash_flow_field9',
                        'changeInInventory':'cash_flow_field10',
                        'profitLoss':'cash_flow_field11',
                        'cashflowFromInvestment':'cash_flow_field12',
                        'cashflowFromFinancing':'cash_flow_field13',
                        'proceedsFromRepaymentsOfShortTermDebt':'cash_flow_field14',
                        'paymentsForRepurchaseOfCommonStock':'cash_flow_field15',
                        'paymentsForRepurchaseOfEquity':'cash_flow_field16',
                        'paymentsForRepurchaseOfPreferredStock':'cash_flow_field17',
                        'dividendPayout':'cash_flow_field18',
                        'dividendPayoutCommonStock':'cash_flow_field19',
                        'dividendPayoutPreferredStock':'cash_flow_field20',
                        'proceedsFromIssuanceOfCommonStock':'cash_flow_field21',
                        'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet':'cash_flow_field22',
                        'proceedsFromIssuanceOfPreferredStock':'cash_flow_field23',
                        'proceedsFromRepurchaseOfEquity':'cash_flow_field24',
                        'proceedsFromSaleOfTreasuryStock':'cash_flow_field25',
                        'changeInCashAndCashEquivalents':'cash_flow_field26',
                        'changeInExchangeRate':'cash_flow_field27',
                        'netIncome':'cash_flow_field28',
                        'netBorrowings':'cash_flow_field29',
                        'otherCashflowFrom_Financing ':'cash_flow_field30',
                        'changeInOperatingFromFinancing ':'cash_flow_field31',
                        'changeInCash ':'cash_flow_field32',
                        'stockSaleAndPurchase ':'cash_flow_field33',
                        'otherOperatingCashflow ':'cash_flow_field34',
                        'changeInNetIncome ':'cash_flow_field35',
                        'depreciation ':'cash_flow_field36',
                        'investments ':'cash_flow_field37',
                        'changeInOperatingActivities ':'cash_flow_field38',
                        'changeInAccountReceivables ':'cash_flow_field39',
                        'changeInCashAndCashEquivalent ':'cash_flow_field40',
                        'otherCashflowFromInvestment':'cash_flow_field41',
                        'reportedCurrency': 'cash_flow_field42',
                        'fiscalDateEnding': 'cash_flow_field43'}
