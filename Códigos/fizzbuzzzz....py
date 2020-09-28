def fizzbuzz(x):
    
    if x % 3 == 0 and x % 5 > 0:
        
        return("Fizz")

    if x % 5 == 0 and x % 3 > 0:
        
        return("Buzz")

    if x % 5 == 0 and x % 3 == 0:
        
        return("FizzBuzz")

    if x % 5 > 0 and x % 3 > 0:
        
        return(x)

    
    
