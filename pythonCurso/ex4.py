# Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay should be the normal rate 
# for hours up to 40 and 1.5*rate for the hourly rate for 
# all hours worked above 40 hours. 

def computepay(h,r):
    if (h > 40):
        p = (40*r) + (h-40)*r*1.5
    else:
        p = h * r

    return p
   

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)