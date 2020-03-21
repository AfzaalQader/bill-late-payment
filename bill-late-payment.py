#Bill late payment
#For 5 months (12% extra bill on current bill) starting bill is 6565
current_bill = 6565
extra_charges = 0
for i in range(1,6):
  extra_charges = (12/100) * current_bill
  current_bill += extra_charges
  print("Your current bill is {} with extra charges {} for late bill payment".format(round(current_bill,2),round(extra_charges,2)))
