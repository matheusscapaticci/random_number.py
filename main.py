import random  # importa números aleatórios

print("Bem-vindo ao jogo!")  # mostra uma mensagem
print("Adivinhe um número entre 1 e 100.")  # explica o jogo

secret = random.randint(1, 100)  # sorteia um número
attempt = 0  # começa as tentativas em 0
limit = 5  # limite de tentativas

while attempt < limit:  # repete até chegar no limite

    user_guess = int(input("Digite um número: "))  # pede um número
    attempt += 1  # aumenta a tentativa

    if user_guess == secret:  # verifica se acertou
        print("Parabéns, você acertou!")  # mostra que acertou
        print("Tentativas:", attempt)  # mostra as tentativas
        break  # para o jogo

    elif user_guess > secret:  # verifica se é maior
        print("O número é menor.")  # avisa

    else:  # se não for maior nem igual, é menor
        print("O número é maior.")  # avisa

if attempt == limit and user_guess != secret:  # verifica se acabou as tentativas sem acertar
    print("Você perdeu!")  # mostra que perdeu
    print("O número era:", secret)  # mostra o número correto
