print("Mobile Recharge")

number = input("Enter number: ")
plan = input("Enter plan: ")

if plan == 199:
    validity = 28
elif plan == 399:
    validity = 56
else:
    validity = 0

print("Number:", number)
print("Validity:", validity)

for i in range(3):
    print("Recharged")

print("End")
