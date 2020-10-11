 
import math
import sys
a=input ("Digite o A:")
b=input ("Digite o B:")
c=input ("Digite o C:")
delta=((b^2)-4*a)*c
if delta<0 :

 print ("Delta negativo, nao possui raizes reais") 
 sys.exit()

else : print "Delta : %s." % d 
sqdelta=math.sqrt(delta)
x1=(-b+sqdelta)/(2*a)
x2=(-b-sqdelta)/(2*a)
print "X1: %s." % x1
print "X2: %s." % x2