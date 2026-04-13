print("AND ou OR")

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

and_result = num1 & num2 
or_result = num1 | num2 

print("")

print(f"Resultado da operação AND: {and_result}")
print(f"Resultado em binário: {bin(and_result)}")

print("")

print(f"Resultado da operação OR: {or_result}")
print(f"Resultado em binário: {bin(or_result)}")

