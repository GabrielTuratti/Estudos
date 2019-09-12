valor = int(input('Entre com um número para saber a tabuada: '))  
n = 0

print('Tabuada do {}'.format(valor))

while(n <= 10):
  print('{0} X {1} = {2}'.format(n, valor, (n * valor)))
  n = n + 1