#Calcula o volume de um cilindro circular reto

raio = float(input("\nPor favor, insira o valor do raio da base: "))
altura = float(input("\nAgora, insira o valor da altura do cilindro: "))

def area_da_base(R):
	R = raio
	area = 3.14 * R * R
	return area

volume = area_da_base(raio) * altura
print(volume)
