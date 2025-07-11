#Exercício de peguntas e respostas usando dicionário

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',

    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '50', '100', '5'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['10', '5', '20', '40'],
        'Resposta': '5'
    }
]

pontos = 0 

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i}) {opcoes}')

    try:
        escolha = int(input('escolha a opção: '))
        if pergunta['Opções'][escolha] == pergunta["Resposta"]:
            pontos += 1
            print('Resposta correta!\n')
        else:
            print('Resposta errada!!!\n')
    except (ValueError, IndexError):
        print("Entrada inválida! VOcê perdeu essa pergunta\n")

    print(f'Você acertou {pontos} de {len(perguntas)} perguntas.')