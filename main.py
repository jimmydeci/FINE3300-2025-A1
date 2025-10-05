# Main program to run Assignment 1

from ExchangeRates import ExchangeRates
from MortgagePayment import MortgagePayment

# Test the MortgagePayment class
if __name__ == "__main__":
    # Example from the assignment
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the quoted annual interest rate (%): "))
    years = int(input("Enter the amortization period (in years): "))

    calc = MortgagePayment(rate, years)
    payments = calc.payments(principal)

    print("\n--- Mortgage Payments Test ---")
    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")

    # Test the ExchangeRates class
    print("\n--- Exchange Rates Test ---")

    xr = ExchangeRates("BankOfCanadaExchangeRates.csv")

    # Prompt the user for conversions
    amount = float(input("Enter amount: "))
    from_curr = input("Convert from (USD or CAD): ")
    to_curr = input("Convert to (USD or CAD): ")

    try:
        result = xr.convert(amount, from_curr, to_curr)
        print(f"{amount} {from_curr.upper()} = {result} {to_curr.upper()}")
    except ValueError as e:
        print("Error:", e)
