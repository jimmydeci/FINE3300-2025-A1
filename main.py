# Main program to run Assignment 1

from ExchangeRates import ExchangeRates
from MortgagePayment import MortgagePayment


def run_mortgage():
    print("\n--- Mortgage Payments ---")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the quoted annual interest rate (%): "))
    years = int(input("Enter the amortization period (in years): "))

    calc = MortgagePayment(rate, years)
    payments = calc.payments(principal)

    print("\n--- Mortgage Payment Results ---")
    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")


def run_exchange_rates():
    print("\n--- Exchange Rates ---")
    # Make sure the CSV file path matches your setup
    xr = ExchangeRates("BankOfCanadaExchangeRates.csv")

    amount = float(input("Enter amount: "))
    from_curr = input("Convert from (USD or CAD): ")
    to_curr = input("Convert to (USD or CAD): ")

    try:
        result = xr.convert(amount, from_curr, to_curr)
        print(f"{amount} {from_curr.upper()} = {result} {to_curr.upper()}")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    while True:
        print("\n=== Assignment 1 Program ===")
        print("1. Mortgage Payment Calculator")
        print("2. Currency Converter (USD/CAD)")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            run_mortgage()
        elif choice == "2":
            run_exchange_rates()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
