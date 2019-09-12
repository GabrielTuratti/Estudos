from math import hypot

co = float(input(" comprimeto do cateto oposto"))
ca = float(input(" comprimento do cateto adiacente"))

hi = hypot(co , ca)
print(" a hipotenusa é igual a : {:.2f}".format(hi))