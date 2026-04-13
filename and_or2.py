print("AND ou OR")

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

print("")
print("Opções:")
print("1 para AND")
print("2 para OR")
print("")
escolha = int(input("insira a opção que deseja realizar: "))

match escolha:
    case 1:
        and_result = num1 & num2 
        print(f"Resultado da operação AND {and_result}")
        print(f"Resultado em binário {bin(and_result)}")
    case 2:
        or_result = num1 | num2 
        print(f"Resultado da operação OR {or_result}")
        print(f"Resultado em binário {bin(or_result)}")
    case _:
        print("Opção inválida")

