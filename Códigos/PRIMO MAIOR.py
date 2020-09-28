def primo_sim(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
    else:
        i += 1
    return True
                
def maior_primo(z):
    y = 2
    primo = primo_sim(z)
    
    if primo == True:
            return z
    else:
        while primo == False:
          if z >= y:
             z % y == 0
             primo = int 
             return primo

