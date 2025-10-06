# Description: Defines a class that reads Bank of Canada exchange rate data (CSV)
#              and converts between USD and CAD currencies.

import csv


class ExchangeRates:
    def __init__(self, csv_file: str):
        self.rate = None
        with open(csv_file, 'r') as file:
            reader = list(csv.reader(file))
            header = reader[0]       # column titles
            last_row = reader[-1]    # most recent row of data

            # Find column for USD/CAD
            usd_cad_index = header.index("USD/CAD")
            self.rate = float(last_row[usd_cad_index])  # Store the latest rate

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        f = from_currency.upper().strip()      # f = input currency
        t = to_currency.upper().strip()        # t = target currency

        if f == "USD" and t == "CAD":
            return round(amount * self.rate, 2)
        elif f == "CAD" and t == "USD":
            return round(amount / self.rate, 2)
        else:
            raise ValueError("Only USD<->CAD conversions are supported.")
