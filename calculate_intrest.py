initial_balance=int(input("enter the initial balance(k0)"))
intrest_rate=float(input("enter the intrest rate"))
time=int(input("enter the time in years"))

current_balance=initial_balance
current_year=0
while(current_year<time):
  current_balance=initial_balance*((1+intrest_rate/100)**time)
  current_year=current_year+1

print("current amount",current_balance)
