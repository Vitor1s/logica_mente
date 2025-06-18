# ===================================================================
# DIA 6 - LISTAS E MÉTODOS DE LISTAS
# ===================================================================
# Conceitos aprendidos:
# - Como criar listas (arrays)
# - Como acessar elementos por índice
# - Como adicionar elementos (append)
# - Como modificar elementos existentes
# - Como remover elementos (remove)
# - Como verificar tamanho da lista (len)
# - Como verificar se um elemento existe na lista (in)
# ===================================================================

print("=== CRIANDO UMA LISTA ===")
# Lista é uma coleção ordenada de itens que PODE ser modificada
# Os índices começam em 0: [0, 1, 2, 3]
carros = ["Fusca", "Civic", "Onix", "HB20"]
print(f"Lista inicial: {carros}")
print(f"Total de carros: {len(carros)}")

print("\n=== ACESSANDO ELEMENTOS POR ÍNDICE ===")
# Para acessar um elemento, use lista[índice]
print(f"Primeiro carro (índice 0): {carros[0]}")
print(f"Terceiro carro (índice 2): {carros[2]}")

print("\n=== ADICIONANDO NOVOS ELEMENTOS ===")
# O método .append() adiciona um item no FINAL da lista
carros.append("Corolla quebrado")
print(f"Após adicionar Corolla: {carros}")
print(f"Novo carro no índice 4: {carros[4]}")

# EXEMPLO comentado de como pedir input do usuário:
# carros.append(input("Digite o nome do novo carro: "))

print("\n=== MODIFICANDO ELEMENTOS EXISTENTES ===")
# Para modificar, use lista[índice] = novo_valor
carros[0] = "Fusca 1970"
print(f"Primeiro carro modificado: {carros[0]}")
print(f"Lista após modificação: {carros}")

print("\n=== REMOVENDO ELEMENTOS ===")
# O método .remove() remove a PRIMEIRA ocorrência do valor especificado
carros.remove("Civic")
print(f"Após remover Civic: {carros}")
print(f"Nova quantidade de carros: {len(carros)}")

print("\n=== VERIFICANDO SE UM ELEMENTO EXISTE ===")
# O operador 'in' verifica se um valor está presente na lista
if "Corolla quebrado" in carros:
    print("✓ O Corolla quebrado está na lista")
else:
    print("✗ O Corolla quebrado NÃO está na lista")

print(f"\nLista final: {carros}")

# ===================================================================
# MÉTODOS IMPORTANTES DE LISTAS:
# - append(item): adiciona item no final
# - remove(item): remove primeira ocorrência do item
# - pop(): remove último item (ou item em índice específico)
# - sort(): ordena a lista
# - reverse(): inverte a ordem dos elementos
# - len(lista): retorna quantidade de elementos
# - item in lista: verifica se item existe na lista
# ===================================================================

