# # Tratamento de Erros

array = ["OR", "AND", 'XOR', 'NAND', 'NOR', 'MOR', 'S1', 'S2']
logical_numbers = ["1", "0"]
def verificar_erros(tamanho, S1, S2, logical_expression):
    if (tamanho > 1000):       return True 
    elif (tamanho != len(S1)): return True
    elif(tamanho !=len(S2)):   return True
    
    for palavra in logical_expression:
        if (palavra in array):
            pass
        else: 
            return True
    
    for i in range(tamanho):     # GAMBIARRA PRA VER SE FUNCIONA
        if (S1[i] in logical_numbers):
            pass
        else: 
            return True
    
    for i in range(tamanho):
        if (S2[i] in logical_numbers):
            pass
        else: 
            return True

    return False

# # Comparações

def to_compare():
    if(len(logical_expression) == 3):
        if(logical_expression[0] == 'S1' and logical_expression[2] == 'S2'):
            return comparisons(S1, S2, logical_expression[1])
        if(logical_expression[0] == 'S1' and logical_expression[2] == 'S1'):
            return comparisons(S1, S1, logical_expression[1])
        if(logical_expression[0] == 'S2' and logical_expression[2] == 'S1'):
            return comparisons(S2, S1, logical_expression[1])
        if(logical_expression[0] == 'S2' and logical_expression[2] == 'S2'):
            return comparisons(S2, S2, logical_expression[1])
    else:
        # PRIMEIRA PARTE
        if(logical_expression[0] == 'S1' and logical_expression[2] == 'S2'):
            partial_result = comparisons(S1, S2, logical_expression[1])
        if(logical_expression[0] == 'S1' and logical_expression[2] == 'S1'):
            partial_result = comparisons(S1, S1, logical_expression[1])
        if(logical_expression[0] == 'S2' and logical_expression[2] == 'S1'):
            partial_result = comparisons(S2, S1, logical_expression[1])
        if(logical_expression[0] == 'S2' and logical_expression[2] == 'S2'):
            partial_result = comparisons(S2, S2, logical_expression[1])

            # SEGUNDA PARTE
        if(logical_expression[-1] == 'S1'):
            return comparisons(partial_result, S1, logical_expression[-2])
        if(logical_expression[-1] == 'S2'):
            return comparisons(partial_result, S2, logical_expression[-2])       


# # Logical Bits Manager
# 

def comparisons(primeira, segunda, operacao):
    if(operacao == "OR"): return OR(primeira, segunda)
    if(operacao == "AND"): return AND(primeira, segunda)
    if(operacao == "XOR"): return XOR(primeira, segunda)
    if(operacao == "NAND"): return NAND(primeira, segunda)
    if(operacao == "NOR"): return NOR(primeira, segunda)
    if(operacao == "MOR"): return MOR(primeira, segunda)
        


# # Now the comparisons

def OR(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == '0' and segunda[i] == '0'):
            resultado += '0'
        else:
            resultado +='1'
    return resultado


def AND(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == '1' and segunda[i] == '1'):
            resultado += '1'
        else:
            resultado +='0'
    return resultado

def XOR(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == segunda[i]):
            resultado += '0'
        else:
            resultado +='1'
    return resultado

def NAND(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == '1' and segunda[i] == '1'):
            resultado += '0'
        else:
            resultado +='1'
    return resultado


def NOR(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == '0' and segunda[i] == '0'):
            resultado += '1'
        else:
            resultado +='0'
    return resultado


def MOR(primeira, segunda):
    resultado = ''
    for i in range(tamanho):
        if (primeira[i] == '1' and segunda[i] == '0'):
            resultado += '0'
        else:
            resultado +='1'
    return resultado


# tamanho = int(input())
# S1 = str(input()).replace("\n", "")
# S2 = str(input()).replace("\n", "")
# logical_expression = str(input()).split(" ")

tamanho = int(input())
S1 = str(input(""))
S2 = str(input(""))

S1  = str(S1.rstrip())
S2  = str(S2.rstrip())
logical_expression = str(input()).split(" ")




if(verificar_erros(tamanho, S1, S2, logical_expression) == True): 
    print("ERRO")
    exit()
else:
    print(to_compare())
