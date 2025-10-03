# Part 1: MortgagePayment class
# This module defines a class that computes Canadian mortgage payments
# for monthly, semi-monthly, bi-weekly, weekly, and accelerated payment schedules

class MortgagePayment:
    def __init__(self, quoted_rate_percent: float, years: int):
        self.quoted_rate_percent = quoted_rate_percent
        self.years = years

    def _ear_from_semiannual(self) -> float:
        # converts the percent rate user provides to a decimal
        j = self.quoted_rate_percent / 100
        # formula for converting semi annual rate to EAR
        return (1 + j/2) ** 2 - 1

    def _periodic_rate(self, payments_per_year: int) -> float:
        ear = self._ear_from_semiannual()
        # provides the per payment interest rate
        return (1 + ear) ** (1 / payments_per_year) - 1

    def _annuity_payment(self, principal: float, r: float, n: int) -> float:
        # takes 3 inputs: principal = amount borrowed, r = periodic interest rate, n = number of payments
        if r == 0:
            return principal / n  # If the interest is 0%, the formula would not work
        # Standard annuity formula for loans
        return principal * (r / (1 - (1 + r) ** (-n)))

    def payments(self, principal: float) -> tuple[float, float, float, float, float, float]:
        # Monthly
        r_m = self._periodic_rate(12)
        n_m = self.years * 12
        monthly = self._annuity_payment(principal, r_m, n_m)

        # Semi-monthly (24/yr)
        r_sm = self._periodic_rate(24)
        n_sm = self.years * 24
        semi_monthly = self._annuity_payment(principal, r_sm, n_sm)

        # Bi-weekly (26/yr)
        r_bw = self._periodic_rate(26)
        n_bw = self.years * 26
        bi_weekly = self._annuity_payment(principal, r_bw, n_bw)

        # Weekly (52/yr)
        r_wk = self._periodic_rate(52)
        n_wk = self.years * 52
        weekly = self._annuity_payment(principal, r_wk, n_wk)

        # Accelerated versions are defined relative to monthly
        accel_bi_weekly = monthly / 2
        accel_weekly = monthly / 4

        return (
            round(monthly, 2),
            round(semi_monthly, 2),
            round(bi_weekly, 2),
            round(weekly, 2),
            round(accel_bi_weekly, 2),
            round(accel_weekly, 2),
        )
