def calcula_desconto(total):
    valor_desconto = 10
    valor_com_desconto = total - valor_desconto
    return  valor_com_desconto
    
def calcula_total_pedido(itens):
    total = 0
    for pedido in itens:
        #pedido = pedido - 2
        total= total + pedido
    return total


def calcula_total():
    sanduba = 11.10 
    coca = 4.20
    batata = 5.0
    itens_pedido = [sanduba,coca,batata]
    total_do_pedido = calcula_total_pedido(itens_pedido)

    valor_com_desconto = calcula_desconto(total_do_pedido)

    print valor_com_desconto

calcula_total()












  



