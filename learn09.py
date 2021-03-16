has_high_income = True
has_good_credit = True

if has_high_income & has_good_credit:
    print(f'Eligible for a loan')
else:
    print(f'Not eligible for a loan')

has_good_income = False
has_bank_balance = True

if has_good_income or has_bank_balance:
    print(f'Eligible for a loan')
else:
    print(f'Not eligible for a loan')

has_decent_credit = True
has_criminal_record = True

if has_decent_credit == True and has_criminal_record == False:
    print(f'Eligible for a loan')
else:
    print(f'Not eligible for a loan')
