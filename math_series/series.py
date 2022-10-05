def fibonacci (n):
 if type(n)!= int: 
   return "please inter your number"   

 if n == 0:
        return 0
 if n == 1:
       return 1

   
   
    # recurrence relation
 return fibonacci(n - 1) + fibonacci(n - 2);

def lucas (n):
   if type(n)!= int: 
    return "please inter your number"   

   if n == 0:
        return 2
   if n == 1:
       return 1

           
   
    # recurrence relation
   return lucas(n - 1) + lucas(n - 2)

def sum_series(n, num1=0 ,num2=1):
   if type(n)!= int: 
    return "please inter your number"  

   if num1 == 0 & num2 == 1 :
      return fibonacci(n)

   elif num1 ==2 & num2==1 :
      return lucas(n)
   else:
       for i in range(2, n + 1) :
        c = num1 + num2
        num1 = num2
        num2 = c
     
   return num2



if __name__=="__main__":
   nterms = int(input("How many terms with fubunaci series? "))    
   print (fibonacci(nterms))
   num = int (input("How many terms with lucas series ? "))
   print(lucas(num))
   print ("fibonacci sum is ",fibonacci(9))
   print("lucas sum is ",lucas(9))
   print("the sum-_series is",sum_series("yy",num1=0,num2=1))
   print("the sum-_series is",sum_series(9,num1=0,num2=1))
   print("the sum-_series is",sum_series(9,num1=2,num2=1))
   print("the sum-_series is",sum_series(5,num1=4,num2=5))