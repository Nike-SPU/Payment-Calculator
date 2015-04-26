__author__ = 'Nnamdi'
balance = 2000
   #balance is customer balance and can be any value
percentB = balance*.035
   #percentB is the balance after your defined percentage (Default is 3.5%)
paymin = max(percentB, 10)
   #The default minimum flat rate value is $10 and can be changed to any value
paymax = min(paymin, balance)
print(paymax)


