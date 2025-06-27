# Funções em Python: blocos de código que podem ser reutilizados
# Este código mostra como criar e usar funções, explicando cada passo de forma simples

# Aqui criamos uma função chamada 'saudacao' que mostra uma mensagem na tela
# Função é como uma receita: só acontece quando você pede (chama ela)
def saudacao():
    # Mostra uma mensagem explicando o que é uma função
    print("Ola, entendendo o conceito de função, onde para seu uso precisa ser chamado, se nao nada acontece")

# Aqui estamos chamando (usando) a função 'saudacao' para mostrar a mensagem
saudacao()

# Agora vamos criar uma função que recebe um nome para personalizar a mensagem
# 'nome' é um parâmetro: um valor que a função precisa para funcionar
def sauda_personalizada(nome):
    # Mostra uma mensagem usando o nome que foi passado para a função
    print(f"ola {nome}, entendeu o conceito de função, onde para seu uso precisa ser chamado, se nao nada acontece, pois quando ele e colocado dentro da função serve como uma variável")

# Chamando a função e passando o nome 'Vitor'
sauda_personalizada("Vitor")
# Chamando a função e passando o nome 'Maria'
sauda_personalizada("Maria")

# Função com vários parâmetros: nome, idade e profissão
def pessoa(nome, idade, profissao):
    # Mostra as informações da pessoa usando os valores recebidos
    print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}")

# Chamando a função e passando os valores para cada parâmetro
pessoa("Vitor", 25, "Desenvolvedor")

# Função que faz uma conta e devolve o resultado usando 'return'
def soma(a, b):
    # Soma os dois valores recebidos e guarda em 'resultado'
    resultado = a + b
    # Devolve o resultado para quem chamou a função
    return resultado

# Aqui chamamos a função, mas não guardamos o resultado em lugar nenhum
soma(5, 10)

# Criamos uma variável 'x' com valor 15
x = 15 # Chama a função e retorna o resultado

# Chamamos a função soma(5, 10), pega o resultado (15) e soma com x (15), ficando 30
soma_x = x + soma(5, 10)

# Mostra o valor de soma_x (30)
print(soma_x)

# Guardamos o resultado da soma(1, 99) na variável 'resultado_soma'
resultado_soma = soma(1, 99)

# Somamos 10 com o resultado da soma anterior (100 + 10 = 110)
soma_y = 10 + resultado_soma

# Mostra o valor de soma_y (110)
print(soma_y)

# O valor retornado pela função pode ser usado em qualquer lugar do código

# Função que converte Fahrenheit para Celsius
def fahrenheit_p_celsius(f):
    # Faz a conta para converter e devolve o resultado
    return (f - 32) * 5 / 9

# Criamos uma variável 'f' com valor 45 (graus Fahrenheit)
f = 45
# Chamamos a função para converter 45°F para Celsius e guardamos em 'c'
c = fahrenheit_p_celsius(f)
# Mostra o resultado da conversão
print(f"{f}°F é igual a {c}°C")

# DICAS PARA APRENDER FUNÇÕES EM PYTHON
# 1. Função é como uma receita: só acontece quando você chama ela.
# 2. Você pode dar informações para a função usando parâmetros (como ingredientes).
# 3. O que está dentro da função só funciona quando ela é chamada.
# 4. Use 'return' para devolver um resultado da função e usar em outros lugares.
# 5. Você pode chamar a mesma função várias vezes, mudando os valores enviados.
# 6. Funções ajudam a deixar o código mais organizado e fácil de entender.
# 7. Se errar, não desista! Teste, mude e aprenda com cada tentativa.
# 8. Comente seu código para lembrar o que cada parte faz.
# 9. Pratique criando funções para coisas do dia a dia (ex: somar, converter, mostrar mensagens).
# 10. Divirta-se programando! Quanto mais você pratica, melhor fica.