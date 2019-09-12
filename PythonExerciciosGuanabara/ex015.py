km = float(input("Quantos km foram rodados ? km:"))
dias = int(input("Por qauntos dias foi alugado ? Dias:"))

print("O valor do aluguel do carro corresponde R${:.2f}".format((km * 0.15) + (dias * 60)))


