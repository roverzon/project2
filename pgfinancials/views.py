from django.http.response import JsonResponse
from rest_framework import status
from tickers.models import Ticker
from pgfinancials.models import Financial
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from pgfinancials.tasks import tickers_all_financials_async
from polygon import RESTClient
from random import sample


@api_view(['GET'])
@permission_classes([AllowAny])
def func1(request):
    if request.method == 'GET':
        symbols = sample([(t.symbol, ) for t in Ticker.objects.all()], 10)
        jobs = tickers_all_financials_async.chunks(symbols, 10)
        jobs.apply_async()
        return JsonResponse({'message': 'financials data send to background '},  status=status.HTTP_200_OK)


@api_view(['GET'])
def financial_ticker_polygon(request, symbol):
    if request.method == 'GET':
        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
            rep = client.reference_stock_financials(symbol=symbol, limit=10)
            results = rep.results
            for result in results:
                result['accumulatedOtherComprehensiveIncome'] = 0.0 if 'accumulatedOtherComprehensiveIncome' not in result else result['accumulatedOtherComprehensiveIncome']
                result['assets'] = 0.0 if 'assets' not in result else result['assets']
                result['assetsAverage'] = 0.0 if 'assetsAverage' not in result else result['assetsAverage']
                result['assetsCurrent'] = 0.0 if 'assetsCurrent' not in result else result['assetsCurrent']
                result['assetsNonCurrent'] = 0.0 if 'assetsNonCurrent' not in result else result['assetsNonCurrent']
                result['assetTurnover'] = 0.0 if 'assetTurnover' not in result else result['assetTurnover']
                result['bookValuePerShare'] = 0.0 if 'bookValuePerShare' not in result else result['bookValuePerShare']
                result['capitalExpenditure'] = 0.0 if 'capitalExpenditure' not in result else result['capitalExpenditure']
                result['cashAndEquivalents'] = 0.0 if 'cashAndEquivalents' not in result else result['cashAndEquivalents']
                result['cashAndEquivalentsUSD'] = 0.0 if 'cashAndEquivalentsUSD' not in result else result['cashAndEquivalentsUSD']
                result['costOfRevenue'] = 0.0 if 'costOfRevenue' not in result else result['costOfRevenue']
                result['consolidatedIncome'] = 0.0 if 'consolidatedIncome' not in result else result['consolidatedIncome']
                result['currentRatio'] = 0.0 if 'currentRatio' not in result else result['currentRatio']
                result['debtToEquityRatio'] = 0.0 if 'debtToEquityRatio' not in result else result['debtToEquityRatio']
                result['debt'] = 0.0 if 'debt' not in result else result['debt']
                result['debtCurrent'] = 0.0 if 'debtCurrent' not in result else result['debtCurrent']
                result['debtNonCurrent'] = 0.0 if 'debtNonCurrent' not in result else result['debtNonCurrent']
                result['debtUSD'] = 0.0 if 'debtUSD' not in result else result['debtUSD']
                result['deferredRevenue'] = 0.0 if 'deferredRevenue' not in result else result['deferredRevenue']
                result['depreciationAmortizationAndAccretion'] = 0.0 if 'depreciationAmortizationAndAccretion' not in result else result['depreciationAmortizationAndAccretion']
                result['deposits'] = 0.0 if 'deposits' not in result else result['deposits']
                result['dividendYield'] = 0.0 if 'dividendYield' not in result else result['dividendYield']
                result['dividendsPerBasicCommonShare'] = 0.0 if 'dividendsPerBasicCommonShare' not in result else result['dividendsPerBasicCommonShare']
                result['earningBeforeInterestTaxes'] = 0.0 if 'earningBeforeInterestTaxes' not in result else result['earningBeforeInterestTaxes']
                result['earningsBeforeInterestTaxesDepreciationAmortization'] = 0.0 if 'earningsBeforeInterestTaxesDepreciationAmortization' not in result else result['earningsBeforeInterestTaxesDepreciationAmortization']
                result['EBITDAMargin'] = 0.0 if 'EBITDAMargin' not in result else result['EBITDAMargin']
                result['earningsBeforeInterestTaxesDepreciationAmortizationUSD'] = 0.0 if 'earningsBeforeInterestTaxesDepreciationAmortizationUSD' not in result else result['earningsBeforeInterestTaxesDepreciationAmortizationUSD']
                result['earningBeforeInterestTaxesUSD'] = 0.0 if 'earningBeforeInterestTaxesUSD' not in result else result['earningBeforeInterestTaxesUSD']
                result['earningsBeforeTax'] = 0.0 if 'earningsBeforeTax' not in result else result['earningsBeforeTax']
                result['earningsPerBasicShare'] = 0.0 if 'earningsPerBasicShare' not in result else result['earningsPerBasicShare']
                result['earningsPerDilutedShare'] = 0.0 if 'earningsPerDilutedShare' not in result else result['earningsPerDilutedShare']
                result['earningsPerBasicShareUSD'] = 0.0 if 'earningsPerBasicShareUSD' not in result else result['earningsPerBasicShareUSD']
                result['shareholdersEquity'] = 0.0 if 'shareholdersEquity' not in result else result['shareholdersEquity']
                result['averageEquity'] = 0.0 if 'averageEquity' not in result else result['averageEquity']
                result['shareholdersEquityUSD'] = 0.0 if 'shareholdersEquityUSD' not in result else result['shareholdersEquityUSD']
                result['enterpriseValue'] = 0.0 if 'enterpriseValue' not in result else result['enterpriseValue']
                result['enterpriseValueOverEBIT'] = 0.0 if 'enterpriseValueOverEBIT' not in result else result['enterpriseValueOverEBIT']
                result['enterpriseValueOverEBITDA'] = 0.0 if 'enterpriseValueOverEBITDA' not in result else result['enterpriseValueOverEBITDA']
                result['freeCashFlow'] = 0.0 if 'freeCashFlow' not in result else result['freeCashFlow']
                result['freeCashFlowPerShare'] = 0.0 if 'freeCashFlowPerShare' not in result else result['freeCashFlowPerShare']
                result['foreignCurrencyUSDExchangeRate'] = 0.0 if 'foreignCurrencyUSDExchangeRate' not in result else result['foreignCurrencyUSDExchangeRate']
                result['grossProfit'] = 0.0 if 'grossProfit' not in result else result['grossProfit']
                result['grossMargin'] = 0.0 if 'grossMargin' not in result else result['grossMargin']
                result['goodwillAndIntangibleAssets'] = 0.0 if 'goodwillAndIntangibleAssets' not in result else result['goodwillAndIntangibleAssets']
                result['interestExpense'] = 0.0 if 'interestExpense' not in result else result['interestExpense']
                result['investedCapital'] = 0.0 if 'investedCapital' not in result else result['investedCapital']
                result['investedCapitalAverage'] = 0.0 if 'investedCapitalAverage' not in result else result['investedCapitalAverage']
                result['inventory'] = 0.0 if 'inventory' not in result else result['inventory']
                result['investments'] = 0.0 if 'investments' not in result else result['investments']
                result['investmentsCurrent'] = 0.0 if 'investmentsCurrent' not in result else result['investmentsCurrent']
                result['investmentsNonCurrent'] = 0.0 if 'investmentsNonCurrent' not in result else result['investmentsNonCurrent']
                result['totalLiabilities'] = 0.0 if 'totalLiabilities' not in result else result['totalLiabilities']
                result['currentLiabilities'] = 0.0 if 'currentLiabilities' not in result else result['currentLiabilities']
                result['liabilitiesNonCurrent'] = 0.0 if 'liabilitiesNonCurrent' not in result else result['liabilitiesNonCurrent']
                result['marketCapitalization'] = 0.0 if 'marketCapitalization' not in result else result['marketCapitalization']
                result['netCashFlow'] = 0.0 if 'netCashFlow' not in result else result['netCashFlow']
                result['netCashFlowBusinessAcquisitionsDisposals'] = 0.0 if 'netCashFlowBusinessAcquisitionsDisposals' not in result else result['netCashFlowBusinessAcquisitionsDisposals']
                result['issuanceEquityShares'] = 0.0 if 'issuanceEquityShares' not in result else result['issuanceEquityShares']
                result['issuanceDebtSecurities'] = 0.0 if 'issuanceDebtSecurities' not in result else result['issuanceDebtSecurities']
                result['paymentDividendsOtherCashDistributions'] = 0.0 if 'paymentDividendsOtherCashDistributions' not in result else result['paymentDividendsOtherCashDistributions']
                result['netCashFlowFromFinancing'] = 0.0 if 'netCashFlowFromFinancing' not in result else result['netCashFlowFromFinancing']
                result['netCashFlowFromInvesting'] = 0.0 if 'netCashFlowFromInvesting' not in result else result['netCashFlowFromInvesting']
                result['netCashFlowInvestmentAcquisitionsDisposals'] = 0.0 if 'netCashFlowInvestmentAcquisitionsDisposals' not in result else result['netCashFlowInvestmentAcquisitionsDisposals']
                result['netCashFlowFromOperations'] = 0.0 if 'netCashFlowFromOperations' not in result else result['netCashFlowFromOperations']
                result['effectOfExchangeRateChangesOnCash'] = 0.0 if 'effectOfExchangeRateChangesOnCash' not in result else result['effectOfExchangeRateChangesOnCash']
                result['netIncome'] = 0.0 if 'netIncome' not in result else result['netIncome']
                result['netIncomeCommonStock'] = 0.0 if 'netIncomeCommonStock' not in result else result['netIncomeCommonStock']
                result['netIncomeCommonStockUSD'] = 0.0 if 'netIncomeCommonStockUSD' not in result else result['netIncomeCommonStockUSD']
                result['netLossIncomeFromDiscontinuedOperations'] = 0.0 if 'netLossIncomeFromDiscontinuedOperations' not in result else result['netLossIncomeFromDiscontinuedOperations']
                result['netIncomeToNonControllingInterests'] = 0.0 if 'netIncomeToNonControllingInterests' not in result else result['netIncomeToNonControllingInterests']
                result['profitMargin'] = 0.0 if 'profitMargin' not in result else result['profitMargin']
                result['operatingExpenses'] = 0.0 if 'operatingExpenses' not in result else result['operatingExpenses']
                result['operatingIncome'] = 0.0 if 'operatingIncome' not in result else result['operatingIncome']
                result['tradeAndNonTradePayables'] = 0.0 if 'tradeAndNonTradePayables' not in result else result['tradeAndNonTradePayables']
                result['payoutRatio'] = 0.0 if 'payoutRatio' not in result else result['payoutRatio']
                result['priceToBookValue'] = 0.0 if 'priceToBookValue' not in result else result['priceToBookValue']
                result['priceEarnings'] = 0.0 if 'priceEarnings' not in result else result['priceEarnings']
                result['priceToEarningsRatio'] = 0.0 if 'priceToEarningsRatio' not in result else result['priceToEarningsRatio']
                result['propertyPlantEquipmentNet'] = 0.0 if 'propertyPlantEquipmentNet' not in result else result['propertyPlantEquipmentNet']
                result['preferredDividendsIncomeStatementImpact'] = 0.0 if 'preferredDividendsIncomeStatementImpact' not in result else result['preferredDividendsIncomeStatementImpact']
                result['sharePriceAdjustedClose'] = 0.0 if 'sharePriceAdjustedClose' not in result else result['sharePriceAdjustedClose']
                result['priceSales'] = 0.0 if 'priceSales' not in result else result['priceSales']
                result['priceToSalesRatio'] = 0.0 if 'priceToSalesRatio' not in result else result['priceToSalesRatio']
                result['tradeAndNonTradeReceivables'] = 0.0 if 'tradeAndNonTradeReceivables' not in result else result['tradeAndNonTradeReceivables']
                result['accumulatedRetainedEarningsDeficit'] = 0.0 if 'accumulatedRetainedEarningsDeficit' not in result else result['accumulatedRetainedEarningsDeficit']
                result['revenues'] = 0.0 if 'revenues' not in result else result['revenues']
                result['revenuesUSD'] = 0.0 if 'revenuesUSD' not in result else result['revenuesUSD']
                result['researchAndDevelopmentExpense'] = 0.0 if 'researchAndDevelopmentExpense' not in result else result['researchAndDevelopmentExpense']
                result['returnOnAverageAssets'] = 0.0 if 'returnOnAverageAssets' not in result else result['returnOnAverageAssets']
                result['returnOnAverageEquity'] = 0.0 if 'returnOnAverageEquity' not in result else result['returnOnAverageEquity']
                result['returnOnInvestedCapital'] = 0.0 if 'returnOnInvestedCapital' not in result else result['returnOnInvestedCapital']
                result['returnOnSales'] = 0.0 if 'returnOnSales' not in result else result['returnOnSales']
                result['shareBasedCompensation'] = 0.0 if 'shareBasedCompensation' not in result else result['shareBasedCompensation']
                result['sellingGeneralAndAdministrativeExpense'] = 0.0 if 'sellingGeneralAndAdministrativeExpense' not in result else result['sellingGeneralAndAdministrativeExpense']
                result['shareFactor'] = 0.0 if 'shareFactor' not in result else result['shareFactor']
                result['shares'] = 0.0 if 'shares' not in result else result['shares']
                result['weightedAverageShares'] = 0.0 if 'weightedAverageShares' not in result else result['weightedAverageShares']
                result['weightedAverageSharesDiluted'] = 0.0 if 'weightedAverageSharesDiluted' not in result else result['weightedAverageSharesDiluted']
                result['salesPerShare'] = 0.0 if 'salesPerShare' not in result else result['salesPerShare']
                result['tangibleAssetValue'] = 0.0 if 'tangibleAssetValue' not in result else result['tangibleAssetValue']
                result['taxAssets'] = 0.0 if 'taxAssets' not in result else result['taxAssets']
                result['incomeTaxExpense'] = 0.0 if 'incomeTaxExpense' not in result else result['incomeTaxExpense']
                result['taxLiabilities'] = 0.0 if 'taxLiabilities' not in result else result['taxLiabilities']
                result['tangibleAssetsBookValuePerShare'] = 0.0 if 'tangibleAssetsBookValuePerShare' not in result else result['tangibleAssetsBookValuePerShare']
                result['workingCapital'] = 0.0 if 'workingCapital' not in result else result['workingCapital']

                financial = Financial(
                    symbol = result['ticker'],
                    period = result['period'],
                    calendarDate = result['calendarDate'],
                    reportPeriod = result['reportPeriod'],
                    updated = result['updated'],
                    dateKey = result['dateKey'],
                    accumulatedOtherComprehensiveIncome = result['accumulatedOtherComprehensiveIncome'],
                    assets = result['assets'],
                    assetsAverage = result['assetsAverage'],
                    assetsCurrent = result['assetsCurrent'],
                    assetsNonCurrent = result['assetsNonCurrent'],
                    assetTurnover = result['assetTurnover'],
                    bookValuePerShare = result['bookValuePerShare'],
                    capitalExpenditure = result['capitalExpenditure'],
                    cashAndEquivalents = result['cashAndEquivalents'],
                    cashAndEquivalentsUSD = result['cashAndEquivalentsUSD'],
                    costOfRevenue = result['costOfRevenue'],
                    consolidatedIncome = result['consolidatedIncome'],
                    currentRatio = result['currentRatio'],
                    debtToEquityRatio = result['debtToEquityRatio'],
                    debt = result['debt'],
                    debtCurrent = result['debtCurrent'],
                    debtNonCurrent = result['debtNonCurrent'],
                    debtUSD = result['debtUSD'],
                    deferredRevenue = result['deferredRevenue'],
                    depreciationAmortizationAndAccretion = result['depreciationAmortizationAndAccretion'],
                    deposits = result['deposits'],
                    dividendYield = result['dividendYield'],
                    dividendsPerBasicCommonShare = result['dividendsPerBasicCommonShare'],
                    earningBeforeInterestTaxes = result['earningBeforeInterestTaxes'],
                    earningsBeforeInterestTaxesDepreciationAmortization = result['earningsBeforeInterestTaxesDepreciationAmortization'],
                    EBITDAMargin = result['EBITDAMargin'],
                    earningsBeforeInterestTaxesDepreciationAmortizationUSD = result['earningsBeforeInterestTaxesDepreciationAmortizationUSD'],
                    earningBeforeInterestTaxesUSD = result['earningBeforeInterestTaxesUSD'],
                    earningsBeforeTax = result['earningsBeforeTax'],
                    earningsPerBasicShare = result['earningsPerBasicShare'],
                    earningsPerDilutedShare = result['earningsPerDilutedShare'],
                    earningsPerBasicShareUSD = result['earningsPerBasicShareUSD'],
                    shareholdersEquity = result['shareholdersEquity'],
                    averageEquity = result['averageEquity'],
                    shareholdersEquityUSD = result['shareholdersEquityUSD'],
                    enterpriseValue = result['enterpriseValue'],
                    enterpriseValueOverEBIT = result['enterpriseValueOverEBIT'],
                    enterpriseValueOverEBITDA = result['enterpriseValueOverEBITDA'],
                    freeCashFlow = result['freeCashFlow'],
                    freeCashFlowPerShare = result['freeCashFlowPerShare'],
                    foreignCurrencyUSDExchangeRate = result['foreignCurrencyUSDExchangeRate'],
                    grossProfit = result['grossProfit'],
                    grossMargin = result['grossMargin'],
                    goodwillAndIntangibleAssets = result['goodwillAndIntangibleAssets'],
                    interestExpense = result['interestExpense'],
                    investedCapital = result['investedCapital'],
                    investedCapitalAverage = result['investedCapitalAverage'],
                    inventory = result['inventory'],
                    investments = result['investments'],
                    investmentsCurrent = result['investmentsCurrent'],
                    investmentsNonCurrent = result['investmentsNonCurrent'],
                    totalLiabilities = result['totalLiabilities'],
                    currentLiabilities = result['currentLiabilities'],
                    liabilitiesNonCurrent = result['liabilitiesNonCurrent'],
                    marketCapitalization = result['marketCapitalization'],
                    netCashFlow = result['netCashFlow'],
                    netCashFlowBusinessAcquisitionsDisposals = result['netCashFlowBusinessAcquisitionsDisposals'],
                    issuanceEquityShares = result['issuanceEquityShares'],
                    issuanceDebtSecurities = result['issuanceDebtSecurities'],
                    paymentDividendsOtherCashDistributions = result['paymentDividendsOtherCashDistributions'],
                    netCashFlowFromFinancing = result['netCashFlowFromFinancing'],
                    netCashFlowFromInvesting = result['netCashFlowFromInvesting'],
                    netCashFlowInvestmentAcquisitionsDisposals = result['netCashFlowInvestmentAcquisitionsDisposals'],
                    netCashFlowFromOperations = result['netCashFlowFromOperations'],
                    effectOfExchangeRateChangesOnCash = result['effectOfExchangeRateChangesOnCash'],
                    netIncome = result['netIncome'],
                    netIncomeCommonStock = result['netIncomeCommonStock'],
                    netIncomeCommonStockUSD = result['netIncomeCommonStockUSD'],
                    netLossIncomeFromDiscontinuedOperations = result['netLossIncomeFromDiscontinuedOperations'],
                    netIncomeToNonControllingInterests = result['netIncomeToNonControllingInterests'],
                    profitMargin = result['profitMargin'],
                    operatingExpenses = result['operatingExpenses'],
                    operatingIncome = result['operatingIncome'],
                    tradeAndNonTradePayables = result['tradeAndNonTradePayables'],
                    payoutRatio = result['payoutRatio'],
                    priceToBookValue = result['priceToBookValue'],
                    priceEarnings = result['priceEarnings'],
                    priceToEarningsRatio = result['priceToEarningsRatio'],
                    propertyPlantEquipmentNet = result['propertyPlantEquipmentNet'],
                    preferredDividendsIncomeStatementImpact = result['preferredDividendsIncomeStatementImpact'],
                    sharePriceAdjustedClose = result['sharePriceAdjustedClose'],
                    priceSales = result['priceSales'],
                    priceToSalesRatio = result['priceToSalesRatio'],
                    tradeAndNonTradeReceivables = result['tradeAndNonTradeReceivables'],
                    accumulatedRetainedEarningsDeficit = result['accumulatedRetainedEarningsDeficit'],
                    revenues = result['revenues'],
                    revenuesUSD = result['revenuesUSD'],
                    researchAndDevelopmentExpense = result['researchAndDevelopmentExpense'],
                    returnOnAverageAssets = result['returnOnAverageAssets'],
                    returnOnAverageEquity = result['returnOnAverageEquity'],
                    returnOnInvestedCapital = result['returnOnInvestedCapital'],
                    returnOnSales = result['returnOnSales'],
                    shareBasedCompensation = result['shareBasedCompensation'],
                    sellingGeneralAndAdministrativeExpense = result['sellingGeneralAndAdministrativeExpense'],
                    shareFactor = result['shareFactor'],
                    shares = result['shares'],
                    weightedAverageShares = result['weightedAverageShares'],
                    weightedAverageSharesDiluted = result['weightedAverageSharesDiluted'],
                    salesPerShare = result['salesPerShare'],
                    tangibleAssetValue = result['tangibleAssetValue'],
                    taxAssets = result['taxAssets'],
                    incomeTaxExpense = result['incomeTaxExpense'],
                    taxLiabilities = result['taxLiabilities'],
                    tangibleAssetsBookValuePerShare = result['tangibleAssetsBookValuePerShare'],
                    workingCapital = result['workingCapital']
                )

                try:
                    financial.save()
                except:
                    pass
        return JsonResponse({'message':'success'}, status=status.HTTP_200_OK)
