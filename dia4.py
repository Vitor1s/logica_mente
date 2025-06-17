# =================================================
# ESTRUTURAS CONDICIONAIS EM PYTHON (if, else, elif)
# =================================================

# ---------------------------------------------
# 1. ESTRUTURA BÁSICA: IF e ELSE
# ---------------------------------------------
# O 'if' executa um bloco de código apenas se a condição for VERDADEIRA
# O 'else' executa quando a condição do 'if' for FALSA

idade = 18

if idade >= 18:
    print("Você é maior de idade.") 
else:
    print("Você é menor de idade.")

# ---------------------------------------------
# 2. OPERADORES LÓGICOS (and, or, not)
# ---------------------------------------------
# 'or' = OU (pelo menos uma condição deve ser verdadeira)
# 'and' = E (todas as condições devem ser verdadeiras)

aluno_escola_publica = False

# Exemplo com operador 'or': se for menor de 18 OU for estudante de escola pública
if idade < 18 or aluno_escola_publica:
    print("Você tem direito a meia entrada.")
else: 
    print("Você não tem direito a meia entrada.")


# ---------------------------------------------
# 3. ELIF - MÚLTIPLAS CONDIÇÕES
# ---------------------------------------------
# 'elif' permite testar várias condições em sequência
# Apenas a PRIMEIRA condição verdadeira será executada

# Sistema de notas: A (>9), B (>7), C (>5), ou "Estude mais"
nota = 8.5

if nota > 9:
    print("Sua nota é A - Excelente!")
elif nota > 7:
    print("Sua nota é B - Muito bom!")
elif nota > 5:
    print("Sua nota é C - Bom!")
else:  # Se nenhuma condição acima for verdadeira
    print("Estude mais um pouco - Nota insuficiente.")


# ---------------------------------------------
# 4. COMPARAÇÃO DE STRINGS
# ---------------------------------------------
# Podemos comparar textos usando == (igual) ou != (diferente)

clima = "nublado"

if clima == "ensolarado": 
    print("Hoje é um dia ensolarado, vamos à praia!")
elif clima == "chuvoso": 
    print("Hoje está chuvoso, melhor ficar em casa.")
elif clima == "nublado":
    print("Hoje está nublado, mas ainda podemos sair.")
else:
    print("Clima não reconhecido.")


# ---------------------------------------------
# 5. CÁLCULOS DENTRO DE CONDICIONAIS
# ---------------------------------------------
# Podemos fazer operações matemáticas dentro dos blocos condicionais

# Sistema de comissão de vendas:
# Venda > 1000: comissão de 0.5% (0.005)
# Venda > 500: comissão de 1% (0.01)  
# Demais casos: comissão de 2% (0.02)

venda = 250

if venda > 1000:
    comissao = venda * 0.005  # 0.5%
    print(f"Venda alta! Comissão de 0.5%: R$ {comissao:.2f}")
elif venda > 500:
    comissao = venda * 0.01   # 1%
    print(f"Venda média! Comissão de 1%: R$ {comissao:.2f}")
else: 
    comissao = venda * 0.02   # 2%
    print(f"Venda baixa! Comissão de 2%: R$ {comissao:.2f}")

# ---------------------------------------------
# 6. ENTRADA DE DADOS DO USUÁRIO
# ---------------------------------------------
# input() sempre retorna string, use float() ou int() para converter números

print("=== Verificador de Números ===")
numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é POSITIVO.")
elif numero < 0:
    print(f"O número {numero} é NEGATIVO.")
else:
    print(f"O número {numero} é ZERO.")

# =================================================
# RESUMO DOS CONCEITOS APRENDIDOS:
# =================================================
# 1. if/else: estrutura básica de decisão
# 2. elif: múltiplas condições em sequência  
# 3. Operadores: >, <, >=, <=, ==, != 
# 4. Operadores lógicos: and, or, not
# 5. Comparação de strings
# 6. Cálculos dentro de blocos condicionais
# 7. Entrada de dados com input()
# =================================================
