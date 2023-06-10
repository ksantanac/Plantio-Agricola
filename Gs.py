import time

def cadastro():

    # Função criada para cadastrar o usuário com o nome e região em que está localizado.

    nome = input('Digite seu nome: ')
    print('')
    regioes = ['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste']

    for i, regiao in enumerate(regioes):
        print(f'{i + 1} - {regiao}')
    print('')
    regiao = int(input("Digite o número da região em que está localizado: "))

    while regiao <= 0 or regiao > 5:
        print("Região selecionada não existe, selecione uma região correta.")
        # time.sleep
        print('')
        print("",
              int('1'), '- Norte\n',
              int('2'), '- Nordeste\n',
              int('3'), '- Sul \n',
              int('4'), '- Sudeste\n',
              int('5'), '- Centro-Oeste\n'
              )

        regiao = int(input("Digite a região em que está localizado: "))

    norte(regiao, nome)
    nordeste(regiao, nome)
    sul(regiao, nome)
    sudeste(regiao, nome)
    centro(regiao, nome)

def deseja_continuar():
    # Função criada para caso o usuário queira entrar novamente no programa
    cadastro()
def norte(regiao, nome):
    # Função criada para região norte

    if regiao == 1:
        produtos = ['Açaí', 'Mandioca', 'Milho', 'Banana', 'Arroz', 'Feijão', 'Maracujá', 'Pimenta Preta', 'Abacaxi',
                    'Coco', 'Outro']

        for i, produto in enumerate(produtos):
            print(f'{i + 1} - {produto}')

        print('')
        produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        while produto_plantar < 1 or produto_plantar > 11:
            print('')
            print('Opção inválida, favor tente novamente.')
            print('')

            for i, produto in enumerate(produtos):
                print(f'{i + 1} - {produto}')

            print('')
            produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        match produto_plantar:
            case 1:

                time.sleep(1)
                print('')
                print('O açaí é uma cultura perene que pode ser plantada ao longo de todo o ano na região Norte. '
                      'No entanto, o período ideal para o plantio é durante a estação chuvosa, que ocorre entre '
                      'os meses de janeiro e junho.')
                print('É importante preparar o solo adequadamente, garantindo uma boa drenagem e fertilidade para '
                      'obter melhores resultados no cultivo do açaí.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 2:

                time.sleep(1)
                print('')
                print('A mandioca pode ser plantada durante todo o ano na região Norte, sendo mais comum realizar '
                      'o plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho.')
                print('O solo adequado para o cultivo da mandioca deve ser bem drenado e rico em nutrientes.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 3:

                time.sleep(1)
                print('')
                print('O milho pode ser plantado durante todo o ano na região Norte, com destaque para os meses de '
                      'setembro a março, que correspondem à estação chuvosa.')
                print('O solo ideal para o cultivo do milho deve ser fértil, bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 4:

                time.sleep(1)
                print('')
                print('A banana é uma cultura que pode ser plantada ao longo de todo o ano na região Norte. '
                      'No entanto, o período ideal para o plantio é durante a estação chuvosa, que ocorre entre '
                      'os meses de janeiro e junho.')
                print('O solo adequado para o cultivo de bananas deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 5:

                time.sleep(1)
                print('')
                print('O arroz é uma cultura que pode ser plantada durante todo o ano na região Norte, sendo mais '
                      'comum realizar o plantio no período da estação chuvosa, que ocorre entre os meses de janeiro '
                      'e junho.')
                print('O solo ideal para o cultivo de arroz deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 6:
                time.sleep(1)
                print('')
                print('O feijão pode ser plantado durante todo o ano na região Norte, com destaque para os meses de '
                      'janeiro a março e de agosto a outubro, que correspondem à estação chuvosa.')
                print('O solo adequado para o cultivo de feijão deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 7:

                time.sleep(1)
                print('')
                print('O maracujá é uma cultura que pode ser plantada ao longo de todo o ano na região Norte. '
                      'No entanto, o período ideal para o plantio é durante a estação chuvosa, que ocorre entre '
                      'os meses de janeiro e junho.')
                print('O solo adequado para o cultivo de maracujá deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 8:
                time.sleep(1)
                print('')
                print('A pimenta preta pode ser plantada durante todo o ano na região Norte, sendo mais comum realizar '
                      'o plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho.')
                print('O solo adequado para o cultivo de pimenta preta deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 9:

                time.sleep(1)
                print('')
                print('O abacaxi é uma cultura que pode ser plantada durante todo o ano na região Norte, sendo mais '
                      'comum realizar o plantio no período da estação chuvosa, que ocorre entre os meses de janeiro '
                      'e junho.')
                print('O solo adequado para o cultivo de abacaxi deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 10:

                time.sleep(1)
                print('')
                print('O coco é uma cultura perene que pode ser plantada ao longo de todo o ano na região Norte. '
                      'No entanto, o período ideal para o plantio é durante a estação chuvosa, que ocorre entre '
                      'os meses de janeiro e junho.')
                print('O solo adequado para o cultivo de coco deve ser bem drenado e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print(
                          'Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          )


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 11:
                time.sleep(1)
                print('')
                outro_produto = input('Digite o que gostaria de plantar: ')

                print(f'{nome}, ainda não temos {outro_produto} registrado no sistema. '
                      f'Iremos atualizar e retornaremos.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

def nordeste(regiao, nome):
    # Função criada para região nordeste.

    if regiao == 2:

        produtos = ['Cana de açúcar', 'Mandioca', 'Milho', 'Banana', 'Batata-doce', 'Feijão', 'Abóbora', 'Melancia',
                    'Quaibo', 'Fava', 'Outro']

        for i, produto in enumerate(produtos):
            print(f'{i + 1} - {produto}')

        print('')
        produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        while produto_plantar < 1 or produto_plantar > len(produtos):
            print('')
            print("Opção inválida, favor tente novamente.")
            print('')
            for i, produto in enumerate(produtos):
                print(f'{i + 1} - {produto}')

            print('')
            produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        match produto_plantar:

            case 1:
                time.sleep(1)
                print('')
                print(
                    'A cana de açúcar é uma cultura perene que pode ser plantada ao longo de todo o ano na região Nordeste. '
                    'No entanto, o período ideal para o plantio é durante a estação chuvosa, que ocorre entre os meses de '
                    'janeiro e junho.')
                print('É importante preparar o solo adequadamente, garantindo uma boa drenagem e fertilidade para obter '
                      'melhores resultados no cultivo da cana de açúcar.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 2:
                time.sleep(1)
                print('')
                print(
                    'A mandioca pode ser plantada durante todo o ano na região Nordeste, sendo mais comum realizar o plantio '
                    'no período da estação chuvosa, que ocorre entre os meses de janeiro e junho.')
                print('O solo adequado para o cultivo da mandioca deve ser bem drenado e rico em nutrientes.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 3:
                time.sleep(1)
                print('')
                print(
                    'O milho pode ser plantado durante todo o ano na região Nordeste. No entanto, recomenda-se realizar o '
                    'plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho, para aproveitar '
                    'melhor a umidade do solo.')
                print(
                    'O solo ideal para o cultivo de milho é aquele que possui boa fertilidade e capacidade de retenção de água.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 4:
                time.sleep(1)
                print('')
                print(
                    'A banana pode ser plantada durante todo o ano na região Nordeste, desde que haja um manejo adequado do '
                    'irrigação. É importante garantir uma boa drenagem do solo para evitar o acúmulo de água nas raízes das '
                    'plantas.')
                print('O cultivo de banana requer uma boa quantidade de luz solar e solo fértil.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 5:
                time.sleep(1)
                print('')
                print(
                    'A batata-doce pode ser plantada durante todo o ano na região Nordeste. No entanto, recomenda-se realizar '
                    'o plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho, para aproveitar '
                    'melhor a umidade do solo.')
                print(
                    'O solo ideal para o cultivo de batata-doce deve ser bem drenado, leve, fértil e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 6:
                time.sleep(1)
                print('')
                print(
                    'O feijão pode ser plantado durante todo o ano na região Nordeste, sendo mais comum realizar o plantio no '
                    'período da estação chuvosa, que ocorre entre os meses de janeiro e junho.')
                print('O cultivo de feijão requer um solo bem drenado, rico em matéria orgânica e com boa fertilidade.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 7:
                time.sleep(1)
                print('')
                print(
                    'A abóbora pode ser plantada durante todo o ano na região Nordeste, sendo mais comum realizar o plantio '
                    'no período da estação chuvosa, que ocorre entre os meses de janeiro e junho.')
                print('O solo ideal para o cultivo de abóbora deve ser bem drenado, fértil e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 8:
                time.sleep(1)
                print('')
                print(
                    'A melancia pode ser plantada durante todo o ano na região Nordeste, desde que haja um manejo adequado '
                    'do irrigação. É importante garantir uma boa drenagem do solo para evitar o acúmulo de água nas raízes '
                    'das plantas.')
                print('O cultivo de melancia requer uma boa quantidade de luz solar e solo fértil.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 9:
                time.sleep(1)
                print('')
                print(
                    'O quaibo pode ser plantado durante todo o ano na região Nordeste. No entanto, recomenda-se realizar o '
                    'plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho, para aproveitar '
                    'melhor a umidade do solo.')
                print('O solo ideal para o cultivo de quaibo deve ser bem drenado, fértil e rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 10:
                time.sleep(1)
                print('')
                print('A fava pode ser plantada durante todo o ano na região Nordeste. No entanto, recomenda-se realizar o '
                      'plantio no período da estação chuvosa, que ocorre entre os meses de janeiro e junho, para aproveitar '
                      'melhor a umidade do solo.')
                print('O cultivo de fava requer um solo bem drenado, fértil e com boa capacidade de retenção de água.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 11:
                time.sleep(1)
                print('')
                outro_produto = input('Digite o que gostaria de plantar: ')

                print(f'{nome}, ainda não temos {outro_produto} registrado no sistema. '
                      f'Iremos atualizar e retornaremos.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

def sul(regiao,nome):
    # Função criada para região Sul.

    if regiao == 3:

        produtos = ['Cenoura', 'Couve-flor', 'Tomate', 'Maçã', 'Uva', 'Morango', 'Erva-mate',
                    'Mel', 'Repolho', 'Brócolis', 'Outro']

        for i, produto in enumerate(produtos):
            print(f'{i + 1} - {produto}')

        print('')
        produto_plantar = int(input(f"{nome}, Escolha o que gostaria de plantar: "))

        while produto_plantar < 1 or produto_plantar >len(produtos):
            print('')
            print('Opção inválida, favor tente novamente.')
            print('')

            for i, produto in enumerate(produtos):
                print(f'{i + 1} - {produto}')

            print('')
            produto_plantar = int(input(f"{nome}, Escolha o que gostaria de plantar: "))

        match produto_plantar:

            case 1:

                time.sleep(1)
                print('')
                print('O plantio da cenoura na região sul pode ser realizado ao longo de todo o ano, com exceção '
                      'dos meses mais frios do inverno.')
                print('O solo ideal para a cenoura é aquele bem drenado, fértil e com boa quantidade de matéria '
                      'orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 2:

                time.sleep(1)
                print('')
                print('O plantio da couve-flor na região sul pode ser realizado durante o outono e a primavera, '
                      'evitando os períodos mais quentes e frios do ano.')
                print('O solo ideal para a couve-flor é aquele com boa drenagem, rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')


                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 3:

                time.sleep(1)
                print('')
                print('O tomate pode ser plantado na região sul durante a primavera e o verão, evitando as épocas '
                      'de geadas.')
                print('O solo ideal para o tomate é aquele com boa drenagem, rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")


            case 4:

                time.sleep(1)
                print('')
                print('A melhor época para plantio de maçã na região sul é no início do outono, entre março e abril.')
                print('É importante escolher variedades de maçã adequadas para o clima da região sul, que apresentam boa '
                      'resistência ao frio e um bom sabor.')
                print('O solo ideal para o cultivo de maçã na região sul é aquele com boa drenagem e rico em matéria '
                      'orgânica.')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print('')
                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 5:

                time.sleep(1)
                print('')
                print('A uva pode ser plantada na região sul durante a primavera e o verão, evitando as épocas '
                      'de geadas.')
                print('O solo ideal para a uva é aquele bem drenado, fértil, com boa quantidade de matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 6:

                time.sleep(1)
                print('')
                print('O morango pode ser plantado na região sul durante a primavera e o verão, evitando as épocas '
                      'de geadas.')
                print('O solo ideal para o morango é aquele bem drenado, fértil, rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")


            case 7:

                time.sleep(1)
                print('')
                print('A erva-mate pode ser cultivada na região sul durante todo o ano, desde que a temperatura '
                      'não fique abaixo de 10°C.')
                print('A erva-mate se adapta a diversos tipos de solos, porém, o ideal é um solo bem drenado e fértil')
                print('')

                solo_drenado = input('Você sabe o que é um solo bem drenado? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")


            case 8:

                time.sleep(1)
                print('')
                print('O mel pode ser produzido na região sul ao longo de todo o ano, aproveitando a floração das '
                      'plantas da região.')
                print('O mel não depende diretamente do tipo de solo, mas sim das plantas visitadas pelas abelhas. '
                      'As abelhas da região sul visitam uma grande variedade de plantas, o que contribui para a '
                      'diversidade do mel produzido.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 9:

                time.sleep(1)
                print('')
                print('O repolho pode ser plantado na região sul durante o outono e a primavera, evitando os períodos '
                      'mais quentes e frios do ano.')
                print('O solo ideal para o repolho é aquele com boa drenagem, rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")


            case 10:

                time.sleep(1)
                print('')
                print('O brócolis pode ser plantado na região sul durante o outono e a primavera, evitando os períodos '
                      'mais quentes e frios do ano.')
                print('O solo ideal para o brócolis é aquele com boa drenagem, rico em matéria orgânica.')
                print('')

                solo_drenado = input('Você sabe o que é um solo com boa drenagem? Digite Sim ou Não: ').lower()

                if solo_drenado.lower() == 'não' or solo_drenado.lower() == 'nao':
                    print('')
                    print('Um solo bem drenado é aquele que permite que a água seja facilmente absorvida e '
                          'escoada, evitando o acúmulo excessivo de umidade nas raízes das plantas. Isso é '
                          'importante para evitar problemas como apodrecimento das raízes e o desenvolvimento '
                          'de doenças.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 11:
                print('')
                outro_produto = input('Digite o que gostaria de plantar: ')

                print(f'{nome}, ainda não temos {outro_produto} registrado no sistema. '
                      f'Iremos atualizar e retornaremos.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

def sudeste(regiao, nome):
    # Função criada para região sudeste.

    if regiao == 4:
        produtos = ['Café', 'Cana-de-Açúcar', 'Milho', 'Feijão', 'Alface', 'Mandioca', 'Cenoura',
                    'Laranja', 'Limão', 'Batata Doce', 'Outro']

        for i, produto in enumerate(produtos):
            print(f'{i + 1} - {produto}')

        print('')
        produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        while produto_plantar < 1 or produto_plantar > len(produtos):
            print('')
            print('Opção inválida, favor tente novamente.')
            print('')

            for i, produto in enumerate(produtos):
                print(f'{i + 1} - {produto}')

            print('')
            produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        match produto_plantar:

            case 1:

                time.sleep(1)
                print('')
                print(
                'O café é um produto amplamente cultivado na região Sudeste do Brasil, sendo uma cultura perene. '
                'O plantio pode ser realizado em diferentes épocas do ano,\nporém, é importante levar em consideração '
                'as condições climáticas e a disponibilidade de água. A colheita ocorre geralmente após cerca de 3 a 4 '
                'anos\ndo plantio. É necessário adotar práticas adequadas de manejo e adubação para obter bons resultados'
                ' no cultivo do café.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 2:

                time.sleep(1)
                print('')
                print(
                'A cana-de-açúcar é uma cultura amplamente cultivada na região Sudeste do Brasil, sendo uma planta perene. '
                'O plantio pode ser realizado em diferentes épocas\ndo ano, mas é comum realizar o plantio na primavera ou '
                'verão. A colheita da cana-de-açúcar geralmente ocorre cerca de 12 a 18 meses após o plantio. É\nimportante '
                'manter a planta irrigada e adotar boas práticas de manejo para obter uma boa produtividade e qualidade na '
                'produção de açúcar ou etanol\na partir da cana-de-açúcar.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 3:

                time.sleep(1)
                print('')
                print(
                'O milho é uma cultura bastante cultivada na região Sudeste do Brasil, sendo uma planta anual. O plantio do '
                'milho pode ser realizado em diferentes épocas\ndo ano, dependendo do tipo de cultivar escolhido. É importante '
                'fazer um bom preparo do solo, fornecer a quantidade adequada de água e adubar corretamente\npara obter bons '
                'resultados no cultivo do milho. A colheita do milho ocorre geralmente após cerca de 90 a 120 dias do plantio, '
                'quando as espigas estão maduras.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 4:

                time.sleep(1)
                print('')
                print(
                'O feijão é uma cultura bastante comum na região Sudeste do Brasil, sendo uma planta anual. O plantio do '
                'feijão pode ser realizado em diferentes épocas\ndo ano, mas é importante evitar períodos de frio intenso '
                'ou de grande incidência de chuvas. É necessário preparar o solo adequadamente, garantir uma boa\nirrigação '
                'e adubar corretamente para obter bons resultados no cultivo do feijão. A colheita do feijão ocorre geralmente '
                'após cerca de 70 a 100 dias\ndo plantio, quando as vagens estão maduras.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 5:

                time.sleep(1)
                print('')
                print(
                'A alface é uma cultura de ciclo curto e pode ser cultivada ao longo do ano na região Sudeste do Brasil. '
                'O plantio da alface requer temperaturas amenas\ne é importante evitar o plantio durante períodos de calor '
                'intenso. É necessário preparar o solo adequadamente, fornecer a quantidade adequada de água\ne adubar '
                'corretamente para obter uma boa produção de alfaces saudáveis. A colheita da alface ocorre geralmente após '
                'cerca de 40 a 60 dias do plantio,\nquando as folhas estão maduras.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 6:

                time.sleep(1)
                print('')
                print(
                'A mandioca é uma cultura amplamente cultivada na região Sudeste do Brasil. O plantio da mandioca pode ser '
                'realizado em diferentes épocas do ano, mas\né importante evitar períodos de grande incidência de chuvas. A '
                'colheita da mandioca geralmente ocorre após cerca de 8 a 12 meses do plantio, quando as\nraízes atingem a '
                'maturidade. É importante realizar um bom preparo do solo, fornecer a quantidade adequada de água e adubar '
                'corretamente para obter uma\nboa produtividade e qualidade nas raízes de mandioca.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 7:

                time.sleep(1)
                print('')
                print(
                'A cenoura é uma cultura de ciclo curto e pode ser cultivada ao longo do ano na região Sudeste do Brasil. '
                'O plantio da cenoura requer temperaturas amenas\ne é importante evitar o plantio durante períodos de calor '
                'intenso. É necessário preparar o solo adequadamente, fornecer a quantidade adequada de água e\nadubar '
                'corretamente para obter uma boa produção de cenouras de qualidade. A colheita da cenoura ocorre geralmente '
                'após cerca de 90 a 120 dias do plantio,\nquando as raízes estão maduras.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 8:

                time.sleep(1)
                print('')
                print(
                'A laranja é uma cultura amplamente cultivada na região Sudeste do Brasil, sendo uma árvore perene. O '
                'plantio da laranja pode ser realizado ao longo do ano,\nmas é importante evitar períodos de frio intenso. '
                'A colheita das laranjas ocorre geralmente após cerca de 1 a 2 anos do plantio, dependendo da variedade\n'
                'cultivada. É necessário fornecer a quantidade adequada de água, adubar corretamente e realizar práticas de '
                'controle de pragas e doenças para obter uma boa\nprodutividade e qualidade nas laranjas.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 9:

                time.sleep(1)
                print('')
                print(
                'O limão é uma cultura amplamente cultivada na região Sudeste do Brasil, sendo uma árvore perene. O plantio '
                'do limão pode ser realizado ao longo do ano,\nmas é importante evitar períodos de frio intenso. A colheita '
                'dos limões ocorre geralmente após cerca de 1 a 2 anos do plantio, dependendo da variedade\ncultivada. É '
                'necessário fornecer a quantidade adequada de água, adubar corretamente e realizar práticas de controle de '
                'pragas e doenças para obter uma\nboa produtividade e qualidade nos limões.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 10:

                time.sleep(1)
                print('')
                print(
                'A batata doce é uma cultura de ciclo curto e pode ser cultivada ao longo do ano na região Sudeste do Brasil. '
                'O plantio da batata doce requer temperaturas\namenas e é importante evitar o plantio durante períodos de '
                'calor intenso. É necessário preparar o solo adequadamente, fornecer a quantidade adequada de água\ne adubar '
                'corretamente para obter uma boa produção de batatas doces saudáveis. A colheita da batata doce ocorre '
                'geralmente após cerca de 90 a 120 dias\ndo plantio, quando as raízes estão maduras.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 11:

                print('')
                outro_produto = input('Digite o que gostaria de plantar: ')

                print(f'{nome}, ainda não temos {outro_produto} registrado no sistema. '
                      f'Iremos atualizar e retornaremos.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

def centro(regiao, nome):
    # Função criada região centro-oeste

    if regiao == 5:
        produtos = ['Soja', 'Tomate', 'Milho', 'Feijão', 'Cebola', 'Mandioca', 'Arroz',
                    'Sorgo', 'Amendoim', 'Batata', 'Outro']

        for i, produto in enumerate(produtos):
            print(f'{i + 1} - {produto}')

        print('')
        produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        while produto_plantar < 1 or produto_plantar > len(produtos):
            print('')
            print('Opção inválida, favor tente novamente.')
            print('')

            for i, produto in enumerate(produtos):
                print(f'{i + 1} - {produto}')

            print('')
            produto_plantar = int(input(f"{nome}, escolha o que gostaria de plantar: "))

        match produto_plantar:

            case 1:

                time.sleep(1)
                print('')
                print(
                    'A soja é uma cultura de grande importância na região Centro-Oeste. O plantio é geralmente realizado '
                    'entre os meses de setembro e janeiro, aproveitando\na época das chuvas e evitando o período de seca.'
                    ' É necessário realizar um planejamento adequado e seguir as boas práticas agrícolas para obter bons\n'
                    'resultados no cultivo da soja.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 2:

                time.sleep(1)
                print('')
                print(
                    'O tomate é uma cultura que pode ser plantada ao longo do ano na região Centro-Oeste, mas é importante '
                    'levar em consideração as condições climáticas\ne as variações de temperatura. O plantio pode ser '
                    'realizado em diferentes épocas, dependendo do tipo de tomate e do sistema de cultivo adotado.'
                    '\nO manejo adequado, incluindo o controle de pragas e doenças, é fundamental para obter uma boa '
                    'produção de tomates.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 3:

                time.sleep(1)
                print('')
                print(
                    'O milho é uma cultura bastante cultivada na região Centro-Oeste. O plantio pode ser realizado em '
                    'diferentes épocas, dependendo das variedades e das\ncondições climáticas locais. Recomenda-se plantar o'
                    ' milho durante o período chuvoso para garantir um bom desenvolvimento das plantas.\nÉ importante '
                    'realizar um manejo adequado do solo e adotar práticas de controle de pragas e doenças para obter uma '
                    'boa produtividade de milho.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 4:

                time.sleep(1)
                print('')
                print(
                    'O feijão é uma cultura comum na região Centro-Oeste e pode ser plantado em diferentes épocas do ano, '
                    'principalmente durante a estação chuvosa.\nRecomenda-se fazer uma análise do solo e adotar práticas de'
                    ' manejo adequadas, como a rotação de culturas, para obter melhores resultados no plantio\nde feijão. '
                    'Além disso, é importante monitorar e controlar pragas e doenças que possam afetar a cultura.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 5:

                time.sleep(1)
                print('')
                print(
                    'A cebola é uma cultura que pode ser plantada ao longo do ano na região Centro-Oeste. O plantio deve ser'
                    ' realizado em solo bem drenado e enriquecido\ncom matéria orgânica. Recomenda-se fazer o plantio no '
                    'período de outono-inverno. A cebola requer cuidados com o manejo das plantas, controle de pragas\n'
                    'e doenças, além de uma irrigação adequada para obter uma boa produção.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 6:

                time.sleep(1)
                print('')
                print(
                'A mandioca é uma cultura que se adapta bem ao clima da região Centro-Oeste. O plantio pode ser feito '
                'durante o ano todo, mas recomenda-se evitar períodos\nde seca prolongada. É importante preparar o solo'
                ' adequadamente, realizar a escolha de variedades adequadas e fazer o controle de pragas e doenças para\n'
                'obter uma boa produtividade de mandioca.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 7:

                time.sleep(1)
                print('')
                print(
                'O arroz é uma cultura que se desenvolve bem na região Centro-Oeste, especialmente em áreas com boa '
                'disponibilidade de água. O plantio pode ser realizado\nem diferentes épocas, mas é importante considerar a'
                ' disponibilidade de água e as condições climáticas para obter um bom rendimento. Além disso,\né necessário'
                ' realizar o manejo adequado do solo, controle de plantas daninhas e pragas para obter uma boa colheita de '
                'arroz.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 8:

                time.sleep(1)
                print('')
                print(
                'O sorgo é uma cultura que se adapta bem ao clima da região Centro-Oeste. O plantio pode ser feito em '
                'diferentes épocas, mas recomenda-se evitar períodos\nde seca prolongada. É importante realizar uma boa'
                ' preparação do solo, realizar a adubação adequada e controlar pragas e doenças para obter bons resultados\n'
                'no cultivo do sorgo.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 9:

                time.sleep(1)
                print('')
                print(
                'O amendoim é uma cultura que se desenvolve bem na região Centro-Oeste, especialmente em solos bem drenados.'
                ' O plantio pode ser realizado em diferentes\népocas, mas é importante considerar as condições climáticas '
                'e a disponibilidade de água. É necessário realizar uma boa preparação do solo, adubação\nadequada e controle'
                ' de pragas e doenças para obter uma boa produção de amendoim.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 10:

                time.sleep(1)
                print('')
                print(
                'A batata é uma cultura que se adapta bem ao clima da região Centro-Oeste. O plantio pode ser realizado em '
                'diferentes épocas, dependendo das variedades e\ndas condições climáticas locais. Recomenda-se fazer a escol'
                'ha de variedades adaptadas à região e realizar o manejo adequado do solo, controle de pragas e\ndoenças para'
                ' obter uma boa produtividade de batata.')
                print('')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")

            case 11:

                print('')
                outro_produto = input('Digite o que gostaria de plantar: ')

                print(f'{nome}, ainda não temos {outro_produto} registrado no sistema. '
                      f'Iremos atualizar e retornaremos.')

                print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                print('')
                realizar_outro_plantio = int(input('Digite uma opção: '))

                while realizar_outro_plantio < 1 or realizar_outro_plantio > 2:
                    print('Opção inválida, favor tente novamente.')
                    print(f'{nome}, deseja realizar outro plantio:\n\n', int('1'), '- Sim\n', int('2'), '- Não')
                    print('')
                    realizar_outro_plantio = int(input('Digite uma opção: '))

                if realizar_outro_plantio == 1:
                    print('')
                    deseja_continuar()
                else:
                    print('')
                    print("Obrigado por usar nosso programa!")


cadastro()


