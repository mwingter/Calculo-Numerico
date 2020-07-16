hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

p = 0

if(h > 40) :
	p = (40 * r) + (h - 40) * r * 1.5
else:
	p = h * r
    
print(p)