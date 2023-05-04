def even_numbers():
    x=range(10)
    for i in x:
        if i % 2==0:
            print(i)

def odd_numbers():
    x=range(10)    
    for i in x:
        if i % 2!=0:
            print(i)

def divisible_five():
    x=range(50)
    for i in x:
        if i % 5==0:
            print(f"{i} is divisible by 5") 
        else:
            print(f"{i} is not divisible by 5")   

def multiple_comparison():
    x=range(50)
    for i in x:
        if i % 5==0:
            print(f"{i} is divisible by 5")
        elif i % 7==0:
            print(f"{i} is divisible by 7")
        elif i%9==0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is not divisible by 5,7 or 9")

def odd_or_even():
    x=range(20)
    for i in x:
        if i % 2==0 and i % 3==0:
            print(f"{i} is diisble by both 2 and 3")
        elif i % 2==0 or i % 3==0:
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3")   

def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1   

def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x % 3==0:
            continue
        print(x)
            
# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50.
def an_even_numbers():
    y=0
    while y<=50:
        y+=1
        if y % 2!=0:
            continue
        print(y) 

# Write a function that takes an integer argument and prints "Prime" 
# if the number is prime, and "Not prime" if the number is not prime.
def prime_number(num=13):
    if num % 1==0 and num % 13==0:
        print("Prime")
    else:
        print("Not prime")
    

# Write a function that takes a list of integers as input and prints
# the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    sum=0
    for number in numbers:
        if number % 2==0:
            sum=sum+number
        print(sum)
# sum_even_numbers([1,2,3,4,5,6,7,8,9])

# Write a function that takes any two integers as input, and prints
# the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_all_interger(num=10,num1=30):
    sum=0
    for n in range(num,num1+1):
        if n % 3==0:
            sum=sum+n
            print(sum)
