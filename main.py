num1 = int(input())
num2 = int(input())

print(num1+num2)

def calculo(num1,num2,num3,operador):
    match operador:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: No se puede dividir entre cero"
        case "%":
            if num1%num2 == 0:
                return num1%num2
            else:
                return "Error"
        case _:
                print("Operador inexistente")  
#resultado = calculo(10, 3, "%")

print("Puedes escoger lo siguiente: ")
print("a. Elegir que operador (+, -, *, /, %) usarás en 2 números ")
print("b. Realizar ejercicios con 3 números ")
print("c. Indica si vas a mezclar los operadores (ej. 2 + 4 - 3, 4 * 5 + 1 / 3) con 3 o + números")

opcion = input("Elige una opción: ")

match opcion:
        case "a":
            operador = input("Elige el operador: \n")
            if operador in ["+", "-", "*", "/", "%"]:
                #operador = input("Elige el operador: \n")
                num1 = int(input("Indica un número: "))
                num2 = int(input("Indica otro número: "))
                resultado = calculo(num1, num2, operador)
                print("Resultado:", resultado)
            else:
                print("El operador no existe")
        case "b":
            operador = print("--Se añaden los 3 números ingresados-- \n")
            num_guardado = 0
            for i in range(3):
                    num_de_usuario = int(input("Indica un número: "))
                    num_guardado = num_guardado + num_de_usuario
            print("Los números suman: ", num_guardado)   
        
        case "c":
            num_guardado = 0
            repeticiones = int(input("Indique la cantidad de números por resolver: "))
            if repeticiones > 3:
                acumulado = int(input("Indica el numero 1: "))
                for i in range(repeticiones - 1):
                    operador = input("Elige el operador (+, -, *, /, %): ")
            
                    if operador in ["+", "-", "*", "/", "%"]:
                        siguiente_num = int(input(f"Indica el numero {i + 2}: "))
                        match operador:
                            case "+":
                                acumulado = acumulado + siguiente_num
                            case "-":
                                acumulado = acumulado - siguiente_num
                            case "*":
                                acumulado = acumulado * siguiente_num
                            case "/":
                                if siguiente_num != 0:
                                    acumulado = acumulado / siguiente_num
                                else:
                                    print("Error: No se puede dividir entre cero")
                                    break
                            case "%":
                                if siguiente_num != 0:
                                    acumulado = acumulado % siguiente_num
                                else:
                                    print("Error: No se puede sacar modulo con cero")       
                                    break
                print("Resultado: ",acumulado)                    
            elif(repeticiones==3):
                acumulado = int(input("Indica el numero 1: "))
                for i in range(repeticiones - 1):
                    operador = input("Elige el operador (+, -, *, /, %): ")
                            
                    if operador in ["+", "-", "*", "/", "%"]:
                        siguiente_num = int(input(f"Indica el numero {i + 2}: "))
                        match operador:
                            case "+":
                                acumulado = acumulado + siguiente_num
                            case "-":
                                acumulado = acumulado - siguiente_num
                            case "*":
                                acumulado = acumulado * siguiente_num
                            case "/":
                                if siguiente_num != 0:
                                    acumulado = acumulado / siguiente_num
                                else:
                                    print("Error: No se puede dividir entre cero")
                                    break
                            case "%":
                                    if siguiente_num != 0:
                                        acumulado = acumulado % siguiente_num
                                    else:
                                        print("Error: No se puede sacar modulo con cero")       
                                        break
                print("Resultado: ",acumulado)            
            else:
                print("Error: Ingresa un número mayor o igual a 3 para la próxima")
