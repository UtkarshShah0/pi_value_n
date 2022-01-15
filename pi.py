from mpmath import mp
a=int(input("Enter number of places after decimal: "))
mp.dps=a+1
print(mp.pi)
