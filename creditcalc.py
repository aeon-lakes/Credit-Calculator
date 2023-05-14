# Annuity Payment Calculation

import math

import argparse


# Calculates loan period (n)
# (loan_principal, annuity, annual_interest)
def periods_calc(p, a, a_i):
    n_i = a_i / (100 * 12)

    n = math.ceil(math.log(a / (a - (n_i * p)), 1 + n_i))

    years = math.floor(n / 12)

    months = n % 12
    if years > 1 and months > 1:
        print(f'It will take {years} years and {months} months to repay this '
              f'loan!')
    elif years == 0 and months > 1:
        print(f'It will take {months} months to repay this loan!')
    elif years > 1 and months == 0:
        print(f'It will take {years} years to repay this loan!')
    elif years == 1 and months == 1:
        print(
            f'It will take {years} year and {months} month to repay this loan!')
    elif years == 0 and months == 1:
        print(f'It will take {months} month to repay this loan!')

    print(f'Overpayment = {(a * n) - p}')
    return n


# Calculates ordinary annuity (A)
# (loan_principle, number_months, annual_interest)
def annuity_calc(p, n, a_i):
    n_i = a_i / (100 * 12)

    annuity = math.ceil(
        p * ((n_i * math.pow((1 + n_i), n)) / (math.pow((1 + n_i), n) - 1)))

    print(f'Your annuity payment = {annuity}!')
    print(f'Overpayment = {(annuity * n) - p}')

    return annuity


# Calculates Principal (P)
# (payment / annuity, periods, interest)
def principal_calc(annuity, n, a_i):
    n_i = a_i / (100 * 12)

    p = math.floor(annuity / (
            (n_i * math.pow((1 + n_i), n)) / (math.pow((1 + n_i), n) - 1)))

    print(f'Your loan principal = {p}!')
    print(f'Overpayment = {(annuity * n) - p}')

    return p


# Calculates Differentiated Payment
# (loan_principle, number_months / periods, interest)
def diff_calc(P, n, a_i):
    n_i = a_i / (100 * 12)

    cum = 0

    for m in range(1, n + 1):
        diff = math.ceil((P / n) + n_i * (P - (P * (m - 1) / n)))
        cum += diff
        print(f'Month {m}: payment is {diff}')

    print(f'Overpayment = {cum - P}')

    return ()

parser = argparse.ArgumentParser(description="This program will calculate Annuity or Differentiated Payments")
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)

args = parser.parse_args()
args_dict = vars(args)

not_none = sum(val is not None for val in args_dict.values())

if not_none == 4:
    pass
else:
    print('Incorrect parameters')
    exit()

if args.type not in ['diff', 'annuity']:
    print('Incorrect parameters')
    exit()

if args.interest is None:
    print('Incorrect parameters')
    exit()

if args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')
    exit()

if args.type == 'diff' and args.payment == None:
    diff_calc(args.principal, args.periods, args.interest)

if args.type == 'annuity'and args.payment == None:
    annuity_calc(args.principal, args.periods, args.interest)

if args.type == 'annuity' and args.principal == None:
    principal_calc(args.payment, args.periods, args.interest)

if args.type == 'annuity' and args.periods == None:
    periods_calc(args.principal, args.payment, args.interest)
