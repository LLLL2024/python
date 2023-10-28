#if applicant has high income OR good credit
#   Eligible for loan
#AND: both
#OR： at least one
#NOT:

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
