def add(a,b):
    answer=a+b
    return answer

def substract(c,d):
    difference=c-d
    return difference

def divide(e,f):
    dividend=e/f
    return dividend

def multiply(m,n):
    product=m*n
    return product

def remainder(y,z):
    modulus=y%z
    return modulus

def divide(y,z):
    divide=y//z
    return divide

def calculator(f,g):
    addition=f+g
    return addition

def even_odd(n):
    if n % 2==0:
        print("Even Number")
    else:print("Odd number")

    # positional arguments

def sum_multiplication(sum,multiplication):
    return (f"The sum of 2 and 6 {sum} and product is {multiplication}")
print(sum_multiplication(6+2,6*2))
# print(sum_multiplication(8,12))

    
# default arguments
def names(firstname="a",secondname="b"):
    return (f"my name is {firstname} {secondname}")
print(names())
print(names(firstname="Angeth"))
print(names(firstname="Becca",secondname="Herjok"))

# positional  *single
def firstname(*names):
    for name in names:
        print(f"Hello {name}")
        # final=[name for name in names]
        # print(f"hello {final}")
    firstname("Angeth","Herjok","Becky","Rebecca")

    # **kwargs
def firstname(**names):
    result=[]
    for name in names.values():
        result+=name
        return result

# write a function that checks if a word is a palindrome.Return true if it is
# and False if it is not.Words noon,madam,radar,civic
