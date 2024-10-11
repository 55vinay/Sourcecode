# Python program to check if the number is an Armstrong number or not
#Examples for Armstrong number
'''
1.num=1634 ( n=4)
# as n=4 the power value is 4
=1^4 + 6^4 + 3^4 + 4^4
=1 + 1296 + 81 + 256
=1634

#num==sum of power of digits hence armstrong number

2.num=123 (n=3)
=1^3 + 2^3 + 3^3
=1 + 8 + 27
=36
# not armstrong number

'''

# take input from the user
num = int(input("Enter a number: "))

# to take length of number
#converting to str because int is not iterable
p=len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** p
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
