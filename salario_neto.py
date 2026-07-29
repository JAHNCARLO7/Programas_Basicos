salariob= float(input("Ingresa tu salario bruto: "))
por= float(input("Ingresa el porcentaje de impuestos: "))
dedu= float(input("Ingresa las deducciones: "))

impuestos= salariob*(por/100)
neto= salariob-impuestos-dedu

print ("Tu salario neto es: ", neto)