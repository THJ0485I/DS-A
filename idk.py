# defining functions 
"""
def functionname(para1, para2, ...):
  result = (para1 + para2) // 2
  return result 
  print("Hello world)
"""

# write a function, convertToList(), which takes in a string as a parameter. It then converts this string into a list of integers

str1 = "23,12,1,27,13,30"
str = "23,12,1,27,13,30"

def convertToList():
  result = s.split(',')
  for i inrange(len(result)):
    result[i] = int(result[i])
  return result

def convertToList2(s):
  return[int(x) for x ni s.split(',')]

mylist = convertToList(str)
mylist2 = convertToList2(str1)
print(mylist)
print(mylist2)
print(str1.split(','))
print(str2.split())


n = 5

def facLoops(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

print(facLoops(n))

def fac(n):
  # state base case 
  if n == 1: 
    return 1
  return  n * fac(n-1)

print(fac(n))

def fibanacci(n):
  if n <= 1
    return n
else:
  return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))

for i in range(n):
  print(fibonacci[i], end=' ')



def AddSum(k, n):
    total = 0
    for i in range(k, n + 1):
        total += i
    return total

# Get user input
k = int(input("Enter the starting number (k): "))
n = int(input("Enter the ending number (n): "))

# Check if input is valid
if k > n:
    print("Starting number must be less than or equal to ending number.")
else:
    result = AddSum(k, n)
    print(f"The sum from {k} to {n} is: {result}")


def AddSum(k, n):
  if k==0:
    return n
  for num in range(1, n+1)
    result += AddSum(k-1, num)
  return result

print(AddSum(14,14))

# A prime number is a natural number ewith exactly 2 unique factors: 1 and itself. The first prime is 2. Write a function to fidn the n-th nuber prime number. n=30, return 113
# 2 <= n n <= 20000

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Example usage
n = int(input("Enter n (2 <= n <= 20000): "))
if 2 <= n <= 20000:
    print(f"The {n}-th prime number is: {nth_prime(n)}")
else:
    print("Please enter n between 2 and 20000.")
