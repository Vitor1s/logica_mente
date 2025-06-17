# ---------------------------------------------
# Variáveis e Tipos de Dados em Python
# ---------------------------------------------

idade = 24  # inteiro (int)
nome = "Vitor"  # string (texto)
altura = 1.6  # float (número decimal)
cidade = 'São José'  # string
esta_logado = True  # booleano (bool)

# Em Python, o tipo de uma variável pode mudar dinamicamente:
nome = 2  # Agora 'nome' é um inteiro (int)

# Verificando o tipo das variáveis:
print(type(nome))        # <class 'int'>
print(type(esta_logado)) # <class 'bool'>
print(type(cidade))      # <class 'str'>
print(type(altura))      # <class 'float'>

# ---------------------------------------------
# Operações com Strings (Concatenação)
# ---------------------------------------------
nomeUsuario = "VITOR, "
frase = "Me chamo " + nomeUsuario + "qual seu nome?"
print(frase)

# ---------------------------------------------
# Operadores de Comparação
# ---------------------------------------------
maior = 15 > 12  # True
print(maior)
menor = 5 < 12   # True
print(menor)
menor2 = 5 < 2   # False
print(menor2)

# Comparando valores diretamente:
print(5 == 5)                # True
print("teste" == "teste")    # True
print("matheus" == "Matheus") # False (case sensitive)
print(15 != 15)              # False (15 não é diferente de 15)

# ---------------------------------------------
# Atribuição e Referência de Variáveis
# ---------------------------------------------
num = 10
num2 = num  # num2 recebe o valor de num
print(num2)
num = 12    # mudando o valor de num
print(num)
print("Numero:", num)

# ---------------------------------------------
# Operações Matemáticas
# ---------------------------------------------
operaçãoMt = num + 12
print(operaçãoMt)

# Operadores de comparação também retornam booleanos:
volume = 15 > 6
print(volume)

# É possível isolar operações matemáticas usando parênteses:
print((14 + 2) * 4)

# ---------------------------------------------
# Operações com Variáveis
# ---------------------------------------------
num3 = 15
num4 = num3 * num2  # Multiplicação entre variáveis
print(num4)

# ---------------------------------------------
# Operadores de Divisão e Módulo
# ---------------------------------------------
print(15.2 % 5)  # Módulo: retorna o resto da divisão (15.2 dividido por 5)
print(15.2 / 5)  # Divisão real: retorna o resultado da divisão

# ---------------------------------------------
# Fim do resumo do dia 2
# ---------------------------------------------