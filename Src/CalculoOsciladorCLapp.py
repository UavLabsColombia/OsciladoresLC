
## El siguiente script calcula los valores de condensadores y bobinas necesarias 
## para el montaje de 1 circuito basados en el oscilador con transistor BJT 2n3904
## 

## Oscilador para el 	Colpits 

import math
lClapp= 100e-6 # Expresado en Henrios
## Para el colpits, tenemos encuenta el criterio
#hfe> c1/c2
c1Clapp = 0.1e-9 # Expresado en Faradios
c2Clapp = 1e-9 # Expresado en Faradios
c3Clapp = 10e-9# Expresado en Faradios

cEqcolpist = 1/((1/c1Clapp)+(1/c2Clapp)+(1/c3Clapp)) # Condensador equivalente serie
print "Serie de condensadores para colpits", cEqcolpist

foClapp =  (1/(2*math.pi))*(math.sqrt((1/lClapp)*((1/c1Clapp)+(1/c2Clapp)+(1/c3Clapp))))# Frecuencia de oscilacion
print "la frecOscCOlpist es:", foClapp

periodo = 1 / foClapp
print "El periodo de la onda seno es:", periodo

##Para que el circuito oscile correctamente, las reactancias deben de ser iguales
## tanto para el serie de los condensadores como para la bobina utilizada. 
#reactancia inductiva
Xl = 2*math.pi*foClapp*lClapp
print "Reactancia Inductiva: ", Xl, "Ohm"

#Reactancia capacitiva
##Calculamos la reactancia para cada condensador
## El condensador mas pequeno, en este caso C1, tendra una reactancia mayor
## Ej. C1 = 4.7nF  C2 = 33nF, 
## al tener C1 la capacitancia menor, indica que la Reactancia de este sera la mayor
Xc1 = 1/(2*math.pi*foClapp*c1Clapp)
print "Reactancia Capacitiva para c1: ", Xc1, "Ohm"
Xc2 = 1/(2*math.pi*foClapp*c2Clapp)
print "Reactancia Capacitiva para c2: ", Xc2, "Ohm"
Xc3 = 1/(2*math.pi*foClapp*c3Clapp)
print "Reactancia Capacitiva para c3: ", Xc3, "Ohm"


Xc = Xc1 + Xc2  + Xc3

print "Reactancia Capacitiva Total: ", Xc, "Ohm"

AXc2Xc1 = Xc2/Xc1 
print "Ganancia en Condensadores por Reactancia", AXc2Xc1


difReactancias = abs(Xl-Xc)
print "Diferencia entre reactancias", difReactancias
if  difReactancias < 0.0001:
	print "Las reactancias Son casi iguales podria Resonar!"
else:
	print "Las reactancias No son iguales"



# Calculo de los valores para el diseno del transistor para el colpits
## Ganancia del transistor debida a los condensadores, tambien conocida como atenuacion o factor 
## de retroalimentacion.
beta=Ac1SobreC2 = c1Clapp/c2Clapp
print "Ganancia en condensadores:",Ac1SobreC2
print "Ganancia por Reactancias en condensador  :",AXc2Xc1



##Para el diseno del circuito.
#en Volts 
Vcc = 10.0

## r1 y r2 son las resistencias del divisor de voltage en la entrada de la base
## para este ejemplo usaremos 10k
r1 = 47e3
r2 = 10e3





# en ohm
# Resistencia de emisor
re = 1.2e3
# Resistencia del colector
rc = 4.7e3



## hayamos voltage thevenin
Vb = vth = ((r2*Vcc)/(r1+r2))
print "vth:" , vth

rth = (r1*r2)/(r1+r2)
print "rth:", rth

## Se calcula el voltaje de Emisor
Ve =  Vb - 0.7
print "Ve:", Ve

## para hayar corrientes decimos Ie=Ic aproximadamente...
iE = Ve/re
print "Ie = Ic :", iE

rPrimae = 26e-3/iE 
print "r'e: ", rPrimae

##Ganancia por conductancia  O ganancia de Corriente
gm = iE / 26e-3
print "Gm:", gm

## Ganancia de Voltage del Amplificador
Av = gm * rc
print "Ganancia del amplificador utilizado", Av 


##Condiciones de arranque para la oscilacion
## Se debe de proponer un valor de RC para que el circuito resuene.
# Debe de ser Rc * Gm * hfe  > 1
# donde Rc = Resistencia de Colector, Gm ganancia por conductancia, hfe el beta del transistor

GananciaTotal = rc * gm * Ac1SobreC2
print "GananciaTotal  es: ", GananciaTotal 
print "Es valido el valor de RC para resonar?", GananciaTotal >= 1
#print "es hfe mayor a  c1/c2?", beta > (Ac1SobreC2)
print "Av*Ai>1?", gm*Av > 1
