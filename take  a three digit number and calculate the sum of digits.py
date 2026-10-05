# take a three digit number and calculate the sum of digits
num=int(input("enter the three digit number:"))
a=num//100
b=num//10%10
c=num%10
sum_of_digits=a+b+c
print("the sum of digit is:",sum_of_digits)
