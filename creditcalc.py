import argparse
import math as m
parser = argparse.ArgumentParser()
parser.add_argument("--type",)
parser.add_argument("--principal",)
parser.add_argument("--periods",)
parser.add_argument("--interest",)
parser.add_argument("--payment",)
args = parser.parse_args()

if args.type == None:
    print("Incorrect parameters")
if args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif args.interest == None:
    print("Incorrect parameters")
elif args.type == "annuity" and args.principal and args.payment and args.interest:
    p = int(args.principal)
    a = int(args.payment)
    i = float(args.interest)
    if p < 0 or a < 0 or i < 0:
        print("Incorrect parameters")
    else:
        i1 = i / (12 * 100)
        a1 = a / (a - (i1 * p))
        n = m.log(a1, (1 + i1))
        n1 = m.floor(n / 12)
        n2 = m.ceil(abs(n1 - (n / 12)) * 12)
        if n1 == 1 and n2 == 0:
            print("It will take", n1, "year to repay this loan!")
        elif n1 == 0 and n2 > 1:
            print("It will take", n1, "months to repay this loan!")
        elif n1 == 0 and n2 == 1:
            print("It will take 1 month to repay this loan!")
        elif n1 > 1 and n2 == 0 or n2 == 12:
            print("It will take", n1 + 1, "years to repay this loan!")
        else:
            print("It will take", n1, "years and", n2, "months to repay this loan!")
        print("Overpayment =", ((m.ceil(n) * int(args.payment)) - int(args.principal)))

elif args.type == "annuity" and args.payment and args.interest and args.periods:
    a = int(args.payment)
    n = int(args.periods)
    i = float(args.interest)
    if a < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
    else:
        i1 = i / (12 * 100)
        p = (a * (m.pow((1 + i1), n) - 1)) / (i1 * m.pow((1 + i1), n))
        print("Your monthly payment =", m.floor(p), "!")
        print("Overpayment =", ((n * a) - m.floor(p)))

elif args.type == "annuity" and args.principal and args.interest and args.periods:
    p = int(args.principal)
    n = int(args.periods)
    i = int(args.interest)
    if p < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
    else:
        i1 = i / (12 * 100)
        a = (p * m.pow((1 + i1), n) * i1) / (m.pow((1 + i1), n) - 1)
        print("Your monthly payment =", m.ceil(a), "!")
        print("Overpayment =", ((m.ceil(a) * n) - p))
elif args.type == "diff" and args.principal and args.periods and args.interest:
    p = int(args.principal)
    n = int(args.periods)
    i = float(args.interest)
    if p < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
    else:
        i1 = i / (12 * 100)
        add = 0
        for x in range(1, n + 1):
            d = (p / n) + (i1 * (p - ((p * (x - 1)) / n)))
            dx = m.ceil(d)
            print("Month", x, ": payment is", dx)
            add += dx
        print("")
        print("Overpayment =", (add - p))
else:
    print("Incorrect parameters")



