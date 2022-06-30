import requests
import pandas as pd


class FmpGatherer():
    """Class to communicate with the FinancialModelingPrep REST API
    https://site.financialmodelingprep.com/developer/docs/
    """

    def __init__(self, api_key):
        self.api_key = api_key
    

    def get_core_information(self, symbol):
        """Retrieves company information from the company-core-information endpoint

        Args:
            symbol (string): ticker of the company e.g. MSFT for Microsoft

        Returns:
            data: response content in json format
        """
        url = "https://financialmodelingprep.com/api/v4/company-core-information"
        params = {
            "apikey" : self.api_key,
            "symbol" : symbol,
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data
    

    def get_income_statement(self, n_periods, cik=None, symbol=None, quartery=False):
        """Retrieves the income statement from the income statement endpoint

        Args:
            n_periods (int): Last number of periods to retrieve starting from today
            cik (string, optional): _description_. SEC unique CIK identifier
            symbol (string, optional): _description_. ticker of the company e.g. MSFT for Microsoft
            quartery (bool, optional): _description_. Defaults to False. If set to true retrieves annual data

        Returns:
            _type_: _description_
        """
        if cik is not None:
            url = "https://financialmodelingprep.com/api/v3/income-statement/{a}".format(a=cik)
        if symbol is not None:
            url = "https://financialmodelingprep.com/api/v3/income-statement/{a}".format(a=symbol)
        params = {
            "api_key" : self.api_key,
            "limit" : n_periods,
        }
        if quartery: params["period"] = "quarter"
        response = requests.get(url, params=params)
        data = response.json()
        return data       








class WikipediaGatherer():


    def __init__(self):
        return None

    
    def get_constituents_table(self):
        return None


    def get_changes_table(self):
        return None
