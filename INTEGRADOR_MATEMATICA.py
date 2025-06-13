# TRABAJO INTEGRADOR 2: MATEMÁTICA Y PROGRAMACIÓN
# Grupo 3: Sergio Massazza, Natalia Gutierrez, Marcos Manzanelli





def es_bisiesto(año):
    
    # Función para verificar si un año es bisiesto - si el año es divisible por 4, 
    # pero no por 100, excepto si es divisible por 400
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
def main():
    print("*" * 60)
    print("TRABAJO INTEGRADOR MATEMÁTICA Y PROGRAMACIÓN")
    print("*" * 60)
    
    # Datos: DNI Y FECHAS DE NACIMIENTO
    print("\nDATOS INTEGRANTES DEL GRUPO:")

    print("Sergio Massazza: DNI 17709420, Nacimiento: 19/04/1966")
    print("Natalia Gutierrez: DNI 26232440, Nacimiento: 04/11/1977") 
    print("Marcos Manzanelli: DNI 44347337, Nacimiento: 07/05/2001")
    
    # OPERACIONES CON DNIs
    print("\n" + "*"*50)
    print("A: OPERACIONES CON DNI")
    print("*"*50)
    
    #Ingreso de los DNIs 
    print("\n1. INGRESO DE DNI:")
    
    # Creamos listas para guardar los datos
    nombres = ["Sergio Massazza", "Natalia Gutierrez", "Marcos Manzanelli"]
    dnis = [17709420, 26232440, 44347337]
    
    # Mostrar los DNIs
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {dnis[i]}")
    print("Presione Enter para continuar...")
    input() 
    # 2. Generación automática de los conjuntos de dígitos únicos
    print("\n2. GENERACIÓN AUTOMÁTICA DE CONJUNTOS DE DÍGITOS ÚNICOS:")
    
    # Crear los conjuntos de dígitos únicos para cada DNI
    conjuntos = []  # Lista para guardar los conjuntos
    
    for i in range(len(dnis)):
        # Convertir el DNI a string para poder recorrer cada dígito
        dni_texto = str(dnis[i])
        
        # Crear un conjunto vacío para este DNI
        conjunto_digitos = set()
        
        # Recorrer cada dígito del DNI y agregarlo al conjunto
        for digito in dni_texto:
            conjunto_digitos.add(int(digito))
        
        # Guardar el conjunto en la lista
        conjuntos.append(conjunto_digitos)
        
        # Mostrar el conjunto (ordenado para que se vea mejor)
        print(f"Conjunto {chr(65+i)} ({nombres[i]}): {sorted(conjunto_digitos)}")

    print("Presione Enter para continuar...")
    input()

    # 3. Cálculo y visualización de operaciones entre conjuntos
    print("\n3. OPERACIONES ENTRE CONJUNTOS:")
    
    # UNIÓN entre pares de conjuntos
    print("\nUNIÓN entre pares de conjuntos:")
    for i in range(len(conjuntos)):
        for j in range(i+1, len(conjuntos)):  # Evitamos repetir pares
            # Calcular la unión de dos conjuntos
            union = conjuntos[i].union(conjuntos[j])
            print(f"Conjunto {chr(65+i)} ∪ Conjunto {chr(65+j)}: {sorted(union)}")
    
    # INTERSECCIÓN entre pares de conjuntos
    print("\nINTERSECCIÓN entre pares de conjuntos:")
    for i in range(len(conjuntos)):
        for j in range(i+1, len(conjuntos)):  # Evitamos repetir pares
            # Calcular la intersección de dos conjuntos
            interseccion = conjuntos[i].intersection(conjuntos[j])
            print(f"Conjunto {chr(65+i)} ∩ Conjunto {chr(65+j)}: {sorted(interseccion)}")
    
    # DIFERENCIA entre pares de conjuntos
    print("\nDIFERENCIA entre pares de conjuntos:")
    for i in range(len(conjuntos)):
        for j in range(i+1, len(conjuntos)):
            # Calcular A - B (elementos que están en A pero no en B)
            diferencia_ab = conjuntos[i] - conjuntos[j]
            # Calcular B - A (elementos que están en B pero no en A)
            diferencia_ba = conjuntos[j] - conjuntos[i]
            
            print(f"Conjunto {chr(65+i)} - Conjunto {chr(65+j)}: {sorted(diferencia_ab)}")
            print(f"Conjunto {chr(65+j)} - Conjunto {chr(65+i)}: {sorted(diferencia_ba)}")
    
    # DIFERENCIA SIMÉTRICA entre pares de conjuntos
    print("\nDIFERENCIA SIMÉTRICA entre pares de conjuntos:")
    for i in range(len(conjuntos)):
        for j in range(i+1, len(conjuntos)):
            # La diferencia simétrica son los elementos que están en uno u otro, pero no en ambos
            diferencia_simetrica = conjuntos[i].symmetric_difference(conjuntos[j])
            print(f"Conjunto {chr(65+i)} ∆ Conjunto {chr(65+j)}: {sorted(diferencia_simetrica)}")
    
    print("Presione Enter para continuar...")
    input()

    # 4. Conteo de frecuencia de cada dígito en cada DNI
    print("\n4. CONTEO DE FRECUENCIA DE CADA DÍGITO:")
    
    # Para cada DNI, contar cuántas veces aparece cada dígito
    for i in range(len(dnis)):
        print(f"\nFrecuencias en DNI de {nombres[i]} ({dnis[i]}):")
        
        # Convertir DNI a texto para recorrer dígito por dígito
        dni_texto = str(dnis[i])
        
        # Crear un diccionario para contar frecuencias
        frecuencias = {}
        
        # Recorrer cada dígito del DNI usando un bucle for
        for digito in dni_texto:
            # Si el dígito ya está en el diccionario, sumar 1
            if digito in frecuencias:
                frecuencias[digito] = frecuencias[digito] + 1
            else:
                # Si es la primera vez que aparece, inicializar en 1
                frecuencias[digito] = 1
        
        # Mostrar las frecuencias ordenadas
        for digito in sorted(frecuencias.keys()):
            print(f"  Dígito {digito}: {frecuencias[digito]} veces")

    print("Presione Enter para continuar...")
    input()
    
    
    # 5. Suma total de los dígitos de cada DNI
    print("\n5. SUMA TOTAL DE LOS DÍGITOS DE CADA DNI:")
    
    # Para cada DNI, sumar todos sus dígitos
    for i in range(len(dnis)):
        dni_texto = str(dnis[i])
        suma_total = 0
        
        # Recorrer cada dígito y sumarlo usando un bucle for
        for digito in dni_texto:
            suma_total = suma_total + int(digito)
        
        print(f"{nombres[i]} (DNI: {dnis[i]}): Suma de dígitos = {suma_total}")

    print("Presione Enter para continuar...")
    input()

 
    # 6. Evaluación de la expresión lógica elegida
    print("\n6. EVALUACIÓN DE EXPRESIÓN LÓGICA:")
    
    print("Expresión lógica implementada:")
    print("'Si más de la mitad de los conjuntos contienen dígitos primos, entonces el grupo tiene predominancia de números primos'")
    print()
    
    # Definir qué números son primos (solo dígitos del 0 al 9)
    digitos_primos = {2, 3, 5, 7}  # Los únicos dígitos primos son 2, 3, 5 y 7
    
    print(f"Dígitos primos considerados: {sorted(digitos_primos)}")
    print()
    # Contar cuántos conjuntos contienen al menos un dígito primo
    conjuntos_con_primos = 0
    # Verificar cada conjunto
    for i in range(len(conjuntos)):
        # Verificar si el conjunto actual tiene intersección con los dígitos primos
        tiene_primos = len(conjuntos[i].intersection(digitos_primos)) > 0
        
        if tiene_primos:
            # Mostrar qué dígitos primos tiene este conjunto
            primos_en_conjunto = conjuntos[i].intersection(digitos_primos)
            print(f"{nombres[i]} contiene dígitos primos: {sorted(primos_en_conjunto)}")
            conjuntos_con_primos = conjuntos_con_primos + 1
        else:
            print(f"{nombres[i]} NO contiene dígitos primos")
    
    print()
    print(f"Total de conjuntos: {len(conjuntos)} | Conjuntos con primos: {conjuntos_con_primos}")
    
    # Evaluar la condición
    if conjuntos_con_primos > len(conjuntos) // 2:
        print(f"CONCLUSIÓN: El grupo TIENE predominancia de números primos")
    else:
        print(f"CONCLUSIÓN: El grupo NO tiene predominancia de números primos")
    
  
    print("Presione Enter para continuar...")
    input()

    # PARTE B: OPERACIONES CON AÑOS DE NACIMIENTO
    print("\n" + "*"*50)
    print("PARTE B: OPERACIONES CON AÑOS DE NACIMIENTO")
    print("*"*50)
    
    # Extraer los años de nacimiento de las fechas
    fechas_nacimiento = ["19/04/1966", "04/11/1977", "07/05/2001"]
    años_nacimiento = []
    
    # Extraer solo el año de cada fecha (está al final, después del último /)
    for fecha in fechas_nacimiento:
        # Dividir la fecha por / y tomar el último elemento (el año)
        partes = fecha.split("/")
        año = int(partes[2])  # El año está en la posición 2 (tercera posición)
        años_nacimiento.append(año)
    
    print("Años de nacimiento:")
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {años_nacimiento[i]}")
    
    # Contar cuántos nacieron en años pares e impares
    print("\nConteo de años pares e impares:")
    años_pares = 0
    años_impares = 0
    
    # Usar un bucle para contar
    for año in años_nacimiento:
        if año % 2 == 0:  # Si el residuo de dividir por 2 es 0, es par
            años_pares = años_pares + 1
        else:
            años_impares = años_impares + 1
    
    print(f"Años pares: {años_pares}")
    print(f"Años impares: {años_impares}")
    
    # Verificar si todos nacieron después del 2000
    todos_despues_2000 = True
    for año in años_nacimiento:
        if año <= 2000:
            todos_despues_2000 = False
            break  # Salir del bucle si encontramos uno que no cumple
    
    if todos_despues_2000:
        print("Grupo Z: Todos nacieron después del 2000")
    else:
        print("No todos nacieron después del 2000")
    
    # Verificar si alguno nació en año bisiesto
    print("\nVerificación de años bisiestos:")
    hay_bisiesto = False
    años_bisiestos_encontrados = []
    
    for año in años_nacimiento:
        if es_bisiesto(año):  # Usamos la función que creamos arriba
            hay_bisiesto = True
            años_bisiestos_encontrados.append(año)
    
    if hay_bisiesto:
        print(f"Tenemos un año especial: {años_bisiestos_encontrados}")
    else:
        print("Nadie del grupo nació en año bisiesto")
    
    # Calcular edades actuales (asumiendo que estamos en 2024)
    año_actual = 2024
    edades_actuales = []
    
    print(f"\nEdades actuales (año {año_actual}):")
    for i in range(len(años_nacimiento)):
        edad = año_actual - años_nacimiento[i]
        edades_actuales.append(edad)
        print(f"{nombres[i]}: {edad} años")
    
    # Calcular producto cartesiano entre años y edades
    print(f"\nProducto cartesiano entre años de nacimiento y edades:")
    
    # Convertir a conjuntos para eliminar duplicados
    conjunto_años = set(años_nacimiento)
    conjunto_edades = set(edades_actuales)

    print(f"Conjunto de años: {sorted(conjunto_años)}")
    print(f"Conjunto de edades: {sorted(conjunto_edades)}")
    
    # Calcular el producto cartesiano
    producto_cartesiano = []
    for año in sorted(conjunto_años):
        for edad in sorted(conjunto_edades):
            producto_cartesiano.append((año, edad))
    
    print(f"Producto cartesiano: {producto_cartesiano}")
    print(f"Total de elementos: {len(producto_cartesiano)}")
    
    print("\n" + "*"*60)
    print("PROGRAMA COMPLETADO")
    print("*"*60)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
