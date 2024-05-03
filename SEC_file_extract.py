from sec_edgar_downloader import Downloader

start_year = "1993"
end_year = "2024"

dl = Downloader("IIITB", "YS.Snigdha@iiitb.ac.in")

class SEC_10K:
    def __init__(self, companies):
        self.companies = companies

    def all_10k(self):
        for _ in self.companies:
            Company_10K(_).download(start_year, end_year)

class Company_10K:
    def __init__(self, ticker):
        self.ticker = ticker
    def download(self, start_year, end_year):
        limits = int(end_year) - int(start_year)
        dl.get("10-K", self.ticker, limit = limits)
SEC_10K(["INTC", "NVDA", "QCOM", "MSFT"]).all_10k()
