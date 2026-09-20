# Contadores das respostas excelente e ruim
excelente = 0
ruim = 0

# Repete a pesquisa para 50 pessoas
for i in range(50):

    # Solicita o nome da pessoa
    nome = input("Digite o nome: ")

    # Solicita a idade e converte para número inteiro
    idade = int(input("Digite a idade: "))

    # Solicita a opinião sobre o atendimento
    opiniao = int(input("Digite sua opinião (1-Excelente, 2-Bom, 3-Ruim): "))

    # Verifica se a opinião foi excelente
    if opiniao == 1:
        excelente += 1

    # Verifica se a opinião foi ruim
    elif opiniao == 3:
        ruim += 1

# Mostra a quantidade de respostas excelente
print("Quantidade de respostas EXCELENTE:", excelente)

# Mostra a quantidade de respostas ruim
print("Quantidade de respostas RUIM:", ruim)