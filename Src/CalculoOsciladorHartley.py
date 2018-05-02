## Oscilador Hartley
import math

#Bobinas del circuito tanque
# Bobina de salida, conectada al Colector del transistor
l1 = 680e-6
# Bobina de realimentacion, conectada a la Base del transistor
l2 =  680e-6
# Bobina equivalente del circuito tanque, bobinas en serie.
lEqHartley = l1 + l2

#Condensador del circuito tanque.
##CHartley = 100e-12
CHartley = 4.7e-12


##Calculamos la frecuencia de oscilacion del circuito tanque.
foHartley = 	1/(2*math.pi*math.sqrt(lEqHartley*CHartley)) # Frecuencia de oscilacion
print "la frecOscHartley es:", foHartley
# Sacamos el periodo de una onda con el inverso de la frecuencias
periodoHartley = 1/foHartley
print "el periodoHartley es:", periodoHartley


##Para que el circuito oscile correctamente, las reactancias deben de ser iguales
## tanto para el serie de las bobinas como para el condensador utilizado sobrel el circuito tanque. 
#reactancia inductiva total es = wL donde w es la velocidad angular a la frecuencia de oscilacion. 
Xl = 2*math.pi*foHartley*lEqHartley
print "Reactancia Inductiva total: ", Xl, "Ohm"
#Reactancia Inductiva
##Calculamos la reactancia para cada bobina
## La bobina se puede ver como una sola el cual ha sido dividida en la mitad. para este ejemplot seria
# el total de 1360uH, 
Xl1 = 2*math.pi*foHartley*l1
print "Reactancia inductiva para l1: ", Xl1, "Ohm"
Xl2 = 2*math.pi*foHartley*l2
print "Reactancia inductiva para l2: ", Xl2, "Ohm"
Xlto = Xl1 + Xl2
print "Reactancia Inductiva Total: ", Xlto, "Ohm"

# La ganancia en reactancias sobre las bobinas
AXl2Xl1 = Xl2/Xl1 
print "Ganancia expresada por la reactancia L2/l1s", AXl2Xl1
	
# Reactancia Capacitiva generada por el condensador del circuito tanques
Xc = 1/(2*math.pi*foHartley*CHartley)
print "Reactancia Capacitiva para Condensador: ", Xc, "Ohm"


difReactancias = abs(Xl-Xc)
print "Diferencia entre reactancias", difReactancias
if  difReactancias < 0.0001:
	print "Las reactancias Son casi iguales podria Resonar!"
else:
	print "Las reactancias No son iguales"



# Calculo de los valores para el diseno del transistor para el colpits
# para el 2n222 con un beta hfe=75
## Ganancia del transistor medida 
##Av = hfe = 200

## Ganancia del transistor debida a los condensadores, tambien conocida como atenuacion o factor 
## de retroalimentacion.
beta=Al1Sobrel2 = l1/l2
print "Ganancia en Bobinas:",Al1Sobrel2
print "Ganancia en Reactancias  :",AXl2Xl1



##Para el diseno del circuito.
#en Volts 
Vcc = 12.0

## r1 y r2 son las resistencias del divisor de voltage en la entrada de la base
## para este ejemplo usaremos 10k
r1 = 22e3
r2 = 4.7e3





# en ohm
# Resistencia de emisor
re = 560
# Resistencia del colector
rc = 1.2e3

# Resitencia de Carga
rl = 100e3


## hayamos voltage thevenin
Vb = vth = ((r2*Vcc)/(r1+r2))
print "vth:" , vth

rth = (r1*r2)/(r1+r2)
print "rth:", rth

# Beta medido del transistor
b = 350
Vbe = 0.7

## Corriente de base
Ib = (vth - Vbe)/(rth + b*re)
print "Ib: %E" % Ib

Ic = b * Ib
print "Ic: %E" % Ic

## para hayar corrientes decimos Ie=Ic aproximadamente...
#iE = Ve/re
Ie = Ic
print "Ie = Ic : %E" % Ie

# Hayamos voltaje de Colector y de emisor
Vc = rc * Ic
print "Vc: ", Vc
Ve = re * Ie
print "Ve: ", Ve

# Hayamos VOltaje Colector Emisor
Vce = Vcc - Vc -Ve
print "Vce: ", Vce

#Analisis en alterna
# Hayamos impedancias de entrada y salida 

Zin = rth
print "Zin: %E" % Zin
Zou = (rc * rl)/ (rc + rl)
print "Zou: %E" % Zou

rPrimae = 26e-3/Ie 
print "r'e: ", rPrimae

#Ganancia del transistor
Av = (Zou)/(rPrimae + re)
print "Av:", Av

# Hayamos los condensadores de entrada y de salida
cIn = (-1)/((Zin/10)*2 * math.pi * foHartley)
print "Cin: ", cIn
cOut = (-1)/((Zou/10)*2 * math.pi * foHartley)
print "Cout: ", cOut 

#hayamos el condensador para el colector
Ce = (-1)/((re/10)*2 * math.pi * foHartley)
print "Ce: ", Ce 

##Ganancia por conductancia  O ganancia de CorrIente
gm = Ie / 26e-3
print "Gm:", gm

# Ganacia con filtro en Emisor
AvC = Zou / rPrimae
print "AvC:", AvC

## Ganancia de Voltage del Amplificador
Av = gm * rc
print "Ganancia del amplificador utilizado", Av 


##Condiciones de arranque para la oscilacion
## Se debe de proponer un valor de RC para que el circuito resuene.
# Debe de ser Rc * Gm * hfe  > 1
# donde Rc = Resistencia de Colector, Gm ganancia por conductancia, hfe el beta del transistor

GananciaTotal = rc * gm * Al1Sobrel2
print "GananciaTotal  es: ", GananciaTotal 
print "Es valido el valor de RC para resonar?", GananciaTotal >= 1
#print "es hfe mayor a  c1/c2?", beta > (Ac1SobreC2)
print "Av*Ai>1?", gm*Av > 1
