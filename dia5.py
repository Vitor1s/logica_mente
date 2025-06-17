# =======================================================
# ESTRUTURAS DE REPETIÇÃO EM PYTHON (for, while)
# =======================================================

# ---------------------------------------------
# 1. LOOP FOR COM LISTAS
# ---------------------------------------------
# O loop 'for' percorre cada item de uma lista automaticamente

frutas = ["maçã", "banana", "laranja", "uva"]  # Lista com 4 frutas

# Sintaxe: for variavel in lista:
# A variável 'fruta' recebe cada item da lista, um por vez
for fruta in frutas:
    print("Fruta:", fruta)
# Resultado: imprime cada fruta separadamente

print()  # Linha em branco para separar

# ---------------------------------------------  
# 2. LOOP FOR COM RANGE()
# ---------------------------------------------
# range(n) cria uma sequência de números de 0 até n-1

for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
    print("Repetição número:", i)
# Executa 5 vezes: i = 0, depois i = 1, i = 2, i = 3, i = 4

print()

# ---------------------------------------------
# 3. LOOP WHILE (ENQUANTO)
# ---------------------------------------------
# O 'while' repete ENQUANTO uma condição for verdadeira
# CUIDADO: se a condição nunca ficar falsa = loop infinito!

contador = 0  # Variável de controle

while contador < 5:  # Enquanto contador for menor que 5
    print("Contador:", contador)
    contador += 1  # IMPORTANTE: incrementar para não criar loop infinito
# contador += 1 é o mesmo que: contador = contador + 1

print()

# ---------------------------------------------
# 4. COMANDO BREAK (PARAR O LOOP)
# ---------------------------------------------
# 'break' interrompe completamente o loop

print("Demonstração do BREAK:")
for i in range(10):  # Iria de 0 a 9
    if i == 5:  # Quando i for igual a 5
        print("Parando o loop no número 5")
        break  # SAI do loop imediatamente
    print("Número:", i)
# Resultado: imprime 0, 1, 2, 3, 4 e para

print()


# ---------------------------------------------
# 5. COMANDO CONTINUE (PULAR ITERAÇÃO)
# ---------------------------------------------
# 'continue' pula para a próxima iteração do loop

print("Demonstração do CONTINUE:")
for i in range(5):  # De 0 a 4
    if i == 2:  # Quando i for igual a 2
        continue  # PULA esta iteração e vai para a próxima
    print("Número:", i)
# Resultado: imprime 0, 1, 3, 4 (pula o 2)

print()


# ---------------------------------------------
# 6. EXERCÍCIO: TABUADA DE UM NÚMERO
# ---------------------------------------------
# Vamos calcular a tabuada de um número escolhido pelo usuário

print("=== CALCULADORA DE TABUADA ===")
N = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {N}:")
for i in range(1, 11):  # De 1 até 10 (range(1, 11))
    resultado = N * i  # Multiplica N por cada número de 1 a 10
    print(f"{N} x {i} = {resultado}")

print()

# ---------------------------------------------
# 7. EXERCÍCIO: CONTAR NÚMEROS PARES E ÍMPARES
# ---------------------------------------------
# Vamos contar quantos números são pares e ímpares em um intervalo

print("=== CONTADOR DE PARES E ÍMPARES ===")
pares = 0     # Contador de números pares (inicia em 0)
impares = 0   # Contador de números ímpares (inicia em 0)

# Vamos verificar números de 1 a 10
for i in range(1, 11):  # De 1 até 10
    if i % 2 == 0:  # Se o resto da divisão por 2 for 0 = par
        pares += 1  # pares = pares + 1
        print(f"{i} é PAR")
    else:  # Se o resto da divisão por 2 for 1 = ímpar
        impares += 1  # impares = impares + 1  
        print(f"{i} é ÍMPAR")

print(f"\nResumo final:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")

# =======================================================
# RESUMO DOS CONCEITOS APRENDIDOS:
# =======================================================
# 1. for com listas: percorre cada item automaticamente
# 2. for com range(): cria sequências numéricas
# 3. while: repete enquanto condição for verdadeira
# 4. break: para o loop completamente
# 5. continue: pula para próxima iteração
# 6. Operador %: resto da divisão (usado para par/ímpar)
# 7. Contadores: variáveis que aumentam a cada iteração
# 8. input() com int(): entrada de números do usuário
# =======================================================