def buzz():  
    print"buzz"

def fizz():
    print"fizz"

def imprime_fizzbuzz():
    print"fizzbuzz"  

def numeracao(numero):
    print (numero)


def fizzbuzz():
    #if(numero %3==0 and numero%5==0):
       # imprime_fizzbuzz()
    #elif(numero%5==0):
       # fizz()
    #elif(numero %3==0):
        #buzz()
    #else:
        #numeracao(numero)
    for i in range(101):
        if(i %3==0 and i%5==0):
            imprime_fizzbuzz()
        elif(i %5==0):
            fizz()
        elif(i %3==0):
            buzz()
        else:
            numeracao(i)

fizzbuzz()
#imprime de 1 a 100, mostrando os valores do fizzbuzz