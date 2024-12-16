def loop_Pergunta(titulo, pergunta, lista_de_opcoes, mensagem_erro):
    while True:
        print('=' * 50)
        print(titulo.upper().center(50))
        print('=' * 50)
        print(pergunta)
        print()
        n_options = 0

        for i in lista_de_opcoes:
            n_options += 1
            print(f'{n_options} - {i}')
        print()
        resposta = int(input('-> '))

        if resposta >=1 and resposta <= n_options:
            return resposta

        else:
            print(f'\033[31m{mensagem_erro}\033[m\n')



