var = list()
var = []

input1 = int(input("Enter first range:"))
input2 = int(input("Enter second range:"))

for i in range(input1,input2 + 1):
   var.append(i**2)

odd = []
even = []

for i in var:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)