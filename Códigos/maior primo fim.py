def maior_primo(x):

    primo = []
    for i in range(x):
        d = 0
        for j in range(x):
            if i%(j+1) == 0: 
              d += 1
        if d == 2:
          primo.append(i)

    return(max(primo))
