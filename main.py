# Main program to run Assignment 1

# from MortgagePayment import MortgagePayment
# from exchange_rates import ExchangeRates

# print("FINE3300 Assignment 1 Program")
# TODO: add user prompts here

from MortgagePayment import MortgagePayment

# Test the MortgagePayment class
if __name__ == "__main__":
    # Example from the assignment
    principal = 500000
    rate = 5.5
    years = 25

    calc = MortgagePayment(rate, years)
    payments = calc.payments(principal)

    print("\n--- Mortgage Payments Test ---")
    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")
