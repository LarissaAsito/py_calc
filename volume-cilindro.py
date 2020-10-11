#Calcula o volume de um cilindro circular reto

raio = float(input("\nInsira o valor do raio da base: "))
altura = float(input("\n Insira o valor da altura do cilindro: "))

def area_da_base(R):
	R = raio
	area = 3.14 * R * R
	return area

volume = area_da_base(raio) * altura
print(volume)