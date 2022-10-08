def fibonacci (n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1.
     In this series, the next integer is determined by summing the previous two. This gives us:

     0, 1, 1, 2, 3, 5, 8, 13, ...
     Note When asking for the nth number in series presume starting at zero.

   fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.

    Parameters
    ----------
   n : which is the number whoose the series finish on it 

    Returns
    -------
    int
        the number of fibonacci series which finish on it 

    See

    Examples
    --------
    >>> fibonacci(1) == 1
    
    >>> fibonacci(7) == 13
   
    >>> fibonacci("tt") == "please Enter your number"
   
    """
    if type(n)!= int: 
           return "please Enter your number"   

    if n == 0:
          return 0
    if n == 1:
           return 1

   
   
    # recurrence relation
    return fibonacci(n - 1) + fibonacci(n - 2);

def lucas (n):

   """
    The Lucas Numbers{:target="_blank"} are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

      2, 1, 3, 4, 7, 11, 18, 29, ...

    Parameters
    ----------
     n : which is the number whoose the series finish on it 

    Returns
    -------
    int
        the number of lucas series which finish on it 

    See

    Examples
    --------
    >>> lucas(0) == 2
    
    >>>  lucas(7) == 29
   
    >>> lucas("tt") == "please Enter your number"
   
   """
   if type(n)!= int: 
    return "please Enter your number"   

   if n == 0:
        return 2
   if n == 1:
       return 1

           
   
    # recurrence relation
   return lucas(n - 1) + lucas(n - 2)



def sum_series(n, num1=0 ,num2=1):
    """
   The SUM  Numbers series are a related series of integers that start with the values n1 and n2 . The resulting series looks like this:

      n1,n2,n2+n1=n3,n3+n2=n4,n4+n3=n5 ...

    Parameters
    ----------
    n1:the intilize int that refer to the first number
    n2 : the second number that intilize to the second number of series
     n : which is the number whoose the series finish on it 

    Returns
    -------
    int
        the number of sum series which finish on it 

    See

    Examples
    --------
    >>>      sum_series("yy",0,1) == "please Enter your number"

    
    >>>  sum_series(9,num1=0,num2=1) == 34
   
    >>>  sum_series(9,num1=2,num2=1) == 76
   
    """

    if type(n)!= int: 
     return "please Enter your number"  

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