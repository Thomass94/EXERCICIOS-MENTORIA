def entrega_mais_total(total):
    entrega = 20
    return(total + entrega)

def calcula_desconto(total):
    desconto = total /10
    return(total - desconto)
    
def calcula_total_pedido(itens):
    total = 0
    for pedido in itens:
        pedido = pedido
        total= total + pedido 
    return total


def calcula_total():
    sanduba = 11.10 
    coca = 4.20
    batata = 5.0
    itens_pedido = [sanduba,coca,batata]
    total_do_pedido = calcula_total_pedido(itens_pedido)

    valor_com_desconto = calcula_desconto(total_do_pedido) 
    total_com_entrega = entrega_mais_total(valor_com_desconto)


    print total_com_entrega

calcula_total()












  



