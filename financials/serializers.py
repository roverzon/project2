from rest_framework import serializers
from financials.models import Financial


class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial

        fields = (
            'symbol',
            'period',
            'calendarDate',
            'reportPeriod',
            'updated',
            'dateKey',
            'accumulatedOtherComprehensiveIncome',
            'assets',
            'assetsAverage',
            'assetsCurrent',
            'assetsNonCurrent',
            'assetTurnover',
            'bookValuePerShare',
            'capitalExpenditure',
            'cashAndEquivalents',
            'cashAndEquivalentsUSD',
            'costOfRevenue',
            'consolidatedIncome',
            'currentRatio',
            'debtToEquityRatio',
            'debt',
            'debtCurrent',
            'debtNonCurrent',
            'debtUSD',
            'deferredRevenue',
            'depreciationAmortizationAndAccretion',
            'deposits',
            'dividendYield',
            'dividendsPerBasicCommonShare',
            'earningBeforeInterestTaxes',
            'earningsBeforeInterestTaxesDepreciationAmortization',
            'EBITDAMargin',
            'earningsBeforeInterestTaxesDepreciationAmortizationUSD',
            'earningBeforeInterestTaxesUSD',
            'earningsBeforeTax',
            'earningsPerBasicShare',
            'earningsPerDilutedShare',
            'earningsPerBasicShareUSD',
            'shareholdersEquity',
            'averageEquity',
            'shareholdersEquityUSD',
            'enterpriseValue',
            'enterpriseValueOverEBIT',
            'enterpriseValueOverEBITDA',
            'freeCashFlow',
            'freeCashFlowPerShare',
            'foreignCurrencyUSDExchangeRate',
            'grossProfit',
            'grossMargin',
            'goodwillAndIntangibleAssets',
            'interestExpense',
            'investedCapital',
            'investedCapitalAverage',
            'inventory',
            'investments',
            'investmentsCurrent',
            'investmentsNonCurrent',
            'totalLiabilities',
            'currentLiabilities',
            'liabilitiesNonCurrent',
            'marketCapitalization',
            'netCashFlow',
            'netCashFlowBusinessAcquisitionsDisposals',
            'issuanceEquityShares',
            'issuanceDebtSecurities',
            'paymentDividendsOtherCashDistributions',
            'netCashFlowFromFinancing',
            'netCashFlowFromInvesting',
            'netCashFlowInvestmentAcquisitionsDisposals',
            'netCashFlowFromOperations',
            'effectOfExchangeRateChangesOnCash',
            'netIncome',
            'netIncomeCommonStock',
            'netIncomeCommonStockUSD',
            'netLossIncomeFromDiscontinuedOperations',
            'netIncomeToNonControllingInterests',
            'profitMargin',
            'operatingExpenses',
            'operatingIncome',
            'tradeAndNonTradePayables',
            'payoutRatio',
            'priceToBookValue',
            'priceEarnings',
            'priceToEarningsRatio',
            'propertyPlantEquipmentNet',
            'preferredDividendsIncomeStatementImpact',
            'sharePriceAdjustedClose',
            'priceSales',
            'priceToSalesRatio',
            'tradeAndNonTradeReceivables',
            'accumulatedRetainedEarningsDeficit',
            'revenues',
            'revenuesUSD',
            'researchAndDevelopmentExpense',
            'returnOnAverageAssets',
            'returnOnAverageEquity',
            'returnOnInvestedCapital',
            'returnOnSales',
            'shareBasedCompensation',
            'sellingGeneralAndAdministrativeExpense',
            'shareFactor',
            'shares',
            'weightedAverageShares',
            'weightedAverageSharesDiluted',
            'salesPerShare',
            'tangibleAssetValue',
            'taxAssets',
            'incomeTaxExpense',
            'taxLiabilities',
            'tangibleAssetsBookValuePerShare',
            'workingCapital',
        )
