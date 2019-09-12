valor = float(input("Qual é o preço do produto ? :"))
novo = valor - (valor * 5 / 100)

print("O valor total do produto é R$ {:.2f} com o desconto fica R$ {:.2f}.".format(valor, novo))