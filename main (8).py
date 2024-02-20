# 1)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    result = num1 + num2
    print("sum of the two positive numbers:", result)
elif num1 < 0 and num2 < 0:
    result = num1 * num2 
    print("Product of the two negative numbers:", result)
elif num1 == 0 or num2 == 0:
    print("Cannot perform calculations with 0")
else:
     if num1 > num2:
         result = num1 - num2
     else:
        result = num - num1
        print("Differece between the two numbers:", result)
# 2)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    result = num1 + num2
    print("sum of the two positive numbers:", result)
elif num1 < 0 and num2 < 0:
    result = num1 * num2 
    print("Product of the two negative numbers:", result)
elif num1 == 0 or num2 == 0:
    print("Cannot perform calculations with 0")
else:
     if num1 > num2:
         result = num1 - num2
     else:
        result = num - num1
        print("Differece between the two numbers:", result)

#3)
num_emails = int(input("Enter the nuber of emails:" ))

if num_emails > 100:
    print("sending out a newsletter to subscribers")
else:
    print("No need to send a newsletter")

