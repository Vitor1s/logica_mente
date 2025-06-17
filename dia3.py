# ==========================================
# Revisão: Operadores Aritméticos em Python
# ==========================================
# Operadores aritméticos são usados para realizar operações matemáticas básicas.

a = 10
b = 4

print("Soma (a + b):", a + b)            # Adição
print("Subtração (a - b):", a - b)       # Subtração
print("Multiplicação (a * b):", a * b)   # Multiplicação
print("Divisão (a / b):", a / b)         # Divisão (resultado float)
print("Exponenciação (a ** b):", a ** b) # Potência (a elevado a b)
print("Divisão inteira (a // b):", a // b) # Resultado inteiro da divisão
print("Resto da divisão (a % b):", a % b)  # Módulo (resto)

# ==========================================
# Operadores de Comparação
# ==========================================
# Usados para comparar valores e retornar True ou False.

print("a > 5:", a > 5)     # Maior que
print("a < 5:", a < 5)     # Menor que
print("a == 5:", a == 5)   # Igual a
print("a != 5:", a != 5)   # Diferente de
print("a >= 10:", a >= 10) # Maior ou igual a
print("a <= 10:", a <= 10) # Menor ou igual a

# ==========================================
# Operadores Lógicos: AND, OR, NOT
# ==========================================
# Permitem combinar condições para criar lógicas mais complexas.

# AND: True se todas as condições forem verdadeiras
idade = 20
carteira_dirigir = True
pode_dirigir = (idade >= 18) and carteira_dirigir
print("Pode dirigir (idade >= 18 e carteira):", pode_dirigir)

# OR: True se pelo menos uma condição for verdadeira
estudante = False
idade = 65
meia_entrada = estudante or idade >= 65
print("Tem direito à meia entrada (estudante ou idade >= 65):", meia_entrada)

# NOT: Inverte o valor booleano
chovendo = True
nao_chovendo = not chovendo
print("Chovendo:", chovendo)
print("Não está chovendo:", nao_chovendo)

# ==========================================
# Exemplos Práticos de Lógica de Programação
# ==========================================

# Exemplo 1: Verificar se pode passar de ano
# Regras: nota mínima 6 e frequência mínima 75%
nota = 8
frequencia = 60
passar_de_ano = (nota >= 6) and (frequencia >= 75)
print("Passou de ano? (nota >= 6 e frequência >= 75):", passar_de_ano)

# Exemplo 2: Verificação de senha
# Compara se a senha digitada é igual à senha cadastrada
senha = "123456"
confirma_senha = "teste123456"
senha_correta = senha == confirma_senha
print("A senha está correta?", senha_correta)

# Exemplo 3: Divisão de conta de restaurante
# Divide o valor total igualmente entre as pessoas
total = 123.85
pessoas = 3
valor_por_pessoa = total / pessoas
print("Cada um vai pagar:", valor_por_pessoa)

# ==========================================
# Dicas de Lógica de Programação
# ==========================================
# - Use operadores aritméticos para cálculos matemáticos.
# - Use operadores de comparação para tomar decisões.
# - Combine condições com operadores lógicos para criar regras mais complexas.
# - Sempre teste suas condições para entender o resultado (True/False).
# - Comentários ajudam a entender o que cada parte do código faz.

