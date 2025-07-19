# Python-codes

1 ## Swap Two Numbers Without Using a Temporary Variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)

Output: Enter first number (a): 6
Enter second number (b): 5
After swapping: a = 5 , b = 6



2 ## Check Whether a Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

Output: Enter a number:5
        odd


3 ## Factorial Without Using Recursion
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

Output: Enter a number: 8
Factorial of 8 is 40320


4 ## Check if a Year is a Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

Output:Enter a year: 2000
leap year


5 ## Find the Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is", largest)

output:Enter first number: 56
Enter second number: 87
Enter third number: 99
The largest number is 99


6 ## Print Fibonacci Series up to n Terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Enter number of terms: "))
fibonacci(terms)

output: Enter number of terms: 5
0 1 1 2 3 Enter an integer: 8
Number of digits: 1


7 ##  Count Number of Digits in an Integer
def count_digits(n):
    n = abs(n)  # Handle negative numbers
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count if count > 0 else 1  # Account for 0

num = int(input("Enter an integer: "))
print("Number of digits:", count_digits(num))

output: Enter an integer: 8
Number of digits: 1



8 ## Reverse a String Using a Loop
text = input("Enter a string: ")
reversed_str = ""

for char in text:
    reversed_str = char + reversed_str

print("Reversed string:", reversed_str)

output:output: Enter a string: teju
Reversed string: ujet


9 ##Find the Sum of All Elements in a List
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = 0

for num in numbers:
    total += num

print("Sum of elements:", total)

output: Enter numbers separated by space: 4 5 6 7 
Sum of elements: 22


10  ## Check if a Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

output: Enter a number: 88
88 is not a prime number














