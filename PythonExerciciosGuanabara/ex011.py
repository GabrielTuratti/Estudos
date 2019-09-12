l = float(input("Qual é a largura da parede?:"))
a = float(input("Qual é a altura da parede?:"))
area = l * a

print(" Sua parede tem {} metros quadrados e será necessário {} litros de tinta pra pintar.".format(area, (area/2)))
