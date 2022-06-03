#Activity 1: Define a function to return the number of factors of a given number(including the number itself), for eg, factors of 6 are 1,2,3 and 6 itself, so no. of factors of 6 is 4

def countFactors(num):
  factor = 1
  c = 0
  while(factor<=num):
    if(num%factor==0):
      c = c+1
    factor = factor + 1
  return c

x = int(input("Enter your number: "))
a= countFactors(x)
print('There are total',a,'factors')

  






#Activity 2: Input a number from user and using the above function check if the number is prime or not.