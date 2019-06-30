

#calculo media

def medias_notas(n1,n2,n3):
        notas_somadas = n1 + n2 + n3
        media = notas_somadas / 3
        print(media, "media")
        # print((n1 + n2 + n3)/3)
        
       # print(n1+n2+n3)



medias_notas(10,8,9)
medias_notas(10,10,10)

def somar_notas(n1,n2,n3):
        notas_somadas= n1 + n2 + n3
        return notas_somadas

notas = somar_notas(23,33,21) 
print (notas)

def notas_mais_10(notas_somadas):
    porcentagem = notas_somadas+ 10
    return porcentagem
notas_somadas_mais_dez = notas_mais_10(notas)
print (notas_somadas_mais_dez)


