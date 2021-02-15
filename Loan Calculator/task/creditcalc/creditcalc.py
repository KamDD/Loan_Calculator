import math
import argparse


def calculate_number_of_months(loan, monthly_payment, interest):
    interest = interest / (12 * 100)
    num_months = math.ceil(math.log(monthly_payment / (monthly_payment - interest * loan), 1 + interest))
    return num_months


def calculate_annuity_monthly(loan, num_months, interest):
    interest = interest / (12 * 100)
    ann_monthly = math.ceil(
        loan * (interest * math.pow(1 + interest, num_months) / (math.pow(1 + interest, num_months) - 1)))
    return ann_monthly


def calculate_loan_principal(annuity_payment, num_months, interest):
    interest = interest / (12 * 100)
    loan_principal = round(annuity_payment / (
            interest * math.pow(1 + interest, num_months) / (math.pow(1 + interest, num_months) - 1)))
    return loan_principal


def months_to_year(months):
    years = months // 12
    months = months % 12
    duration_repayment = [years, months]
    return duration_repayment


def calc_diff_payments(loan, num_months, interest):
    interest = interest / (12 * 100)
    diff_pay = []
    for each_month in range(1, num_months + 1):
        diff_pay.append(math.ceil((loan / num_months) + interest * (loan - (loan * (each_month - 1) / num_months))))
    return diff_pay

def calc_overpayment_annuity(loan, num_months, annuity_payment):
    overpayment = num_months * annuity_payment - loan
    return  overpayment

def calc_overpayment_diff(loan, months_payments):
    sum = 0
    for month_pay in months_payments:
        sum += month_pay
    overpayment = sum - loan
    return overpayment


parser = argparse.ArgumentParser(description="This program calculates variables of\
annuity or differentiated type of loan.")
parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="Choose \"annuity\" or \"diff\" (differentiate) type loan.")
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)
parser.add_argument("--payment", type = float)
parser.add_argument("--principal", type = float)

args = parser.parse_args()

all_options = [args.periods, args.payment, args.principal, args.interest]
diff_options = [args.periods, args.principal, args.interest]
annuity_options = [args.periods, args.payment, args.principal, args.interest]
invalid_annuity_args = [1 for arg in annuity_options if arg is None]
is_negative = [False for any in all_options if (any != None and any < 0)]

if len(invalid_annuity_args) > 1 or args.type is None or args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif False in is_negative:
    print("Incorrect parameters")

else:  # if no error in input arguments, then do:
    type_calculation = args.type
    data = []
    handle_year = ''
    handle_month = ''
    # annuity monthly payment amount
    if type_calculation == "annuity":
        if args.payment is None:

            annuity_monthly = calculate_annuity_monthly(args.principal, args.periods, args.interest)
            print(f"Your monthly payment = {annuity_monthly}!")
            overpayment = calc_overpayment_annuity(args.principal, args.periods, annuity_monthly)
            print()
            print(f"Overpayment = {overpayment:.0f}")

        elif args.periods is None:

            number_of_months = calculate_number_of_months(args.principal, args.payment, args.interest)
            duration = months_to_year(number_of_months)

            if duration[0] == 1:
                handle_year = '1' + ' year'
            elif duration[0] > 1:
                handle_year = str(int(duration[0])) + ' years'

            if duration[1] == 1:
                handle_month = '1 month'
            elif duration[1] > 1:
                handle_month = str(int(duration[1])) + ' months'

            if duration[0] != 0 and duration[1] != 0:
                print(f"It will take {handle_year} and {handle_month} to repay this loan!")
            elif duration[0] == 0 and duration[1] != 0:
                print(f"It will take {handle_month} to repay this loan!")
            elif duration[0] != 0 and duration[1] == 0:
                print(f"It will take {handle_year} to repay this loan!")
            overpayment = calc_overpayment_annuity(args.principal, number_of_months, args.payment)
            print()
            print(f"Overpayment = {overpayment:.0f}")

        elif args.principal is None:

            loan_principal = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {loan_principal}!")
            overpayment = calc_overpayment_annuity(loan_principal, args.periods, args.payment)
            print()
            print(f"Overpayment = {overpayment:.0f}")

    elif type_calculation == "diff":
        diff_payments = calc_diff_payments(args.principal, args.periods, args.interest)
        for index in range(len(diff_payments)):
            print(f"Month {index + 1}: payment is {diff_payments[index]}")
        overpayment = calc_overpayment_diff(args.principal, diff_payments)
        print()
        print(f"Overpayment = {overpayment:.0f}")