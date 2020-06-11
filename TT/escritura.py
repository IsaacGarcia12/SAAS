Hola_1 = 'Hola este un texto de prueba'
Hola_2 = 'Hola texto de prueba 2'
with open('escritura.txt', 'w') as output:
	output.write(Hola_1 + '\n' +Hola_2)