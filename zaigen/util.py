def calculate_mortage_repayment(principal, term, rate):
    # convert to monthly
    rate = rate/12
    term_months = term*12
    numerator = rate*principal*pow(1+rate, term_months)
    denominator = pow(1+rate, term_months) - 1
    monthly_repayment = numerator/denominator
    return monthly_repayment*12
