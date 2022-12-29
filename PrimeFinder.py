#primefinder
x=int(input("Enter a number you need to check whether prime number or not: "))

#list contains continuos prime numbers
list=[1,2,3]

#Main func
def find_prime(x):
    for i in range(2,x):
        if x%i==0 and x not in list:
            return False
    return True

#if-else to find it is prime or not
if find_prime(x):
    print(f"{x} is a prime number")
  
else:
    print(f"{x} is not a prime number")