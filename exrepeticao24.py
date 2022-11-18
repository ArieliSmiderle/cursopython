def clear():
    print("\n" * 40)


while True:
    print("---------- LOJA TABAJARA -----------")
    n = 1
    total = 0

    while True:
        preco = float(input("Digite o valor do produto {}: R$ ".format(n)))
        n += 1
        total += preco
        if preco == 0:
            break

    print("------------------------------------")

    print("O valor total da sua compra é: R$ {:.2f} ".format(total))
    dinheiro = float(input("Digite a quantidade que será dada em dinheiro: R$ "))
    print("O troco será: R$ {:.2f}".format(dinheiro - total))

    print("------------------------------------")

    reset = input("pressione 0 para reset, 1 para encerrar: ")
    if reset == "0":
        clear()
        continue
    else:
        clear()
        print("Encerrando caixa...")
        break