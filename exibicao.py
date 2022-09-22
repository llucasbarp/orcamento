import os, basicos, lancamentos

def exibiMENUPRINCIPAL(BD):
    basicos.menuPRINCIPAL(BD)

    while True:
        try:
            op = int(input("PROCEDIMENTO DESEJADO: "))
        except(ValueError, TypeError):
            print("ERRO! Informe um inteiro:")
        else:
            if op == 1:
                exibirBANCOS(BD)
            elif op == 2:
                lancamentos.lancamento(BD)
            elif op == 3:
                exibirHISTORICO(BD)
            elif op == 4:
                exibirMENUOPCOES(BD)
            elif op == 0:
                basicos.mensagem("SAINDO")
                break
            else:
                basicos.mensagem("PROCEDIMENTO INVALIDO")
        finally:
            break


def exibirMENUOPCOES(BD):
    basicos.menuOPCOES()

    while True:
        try:
            op = int(input("OPÇÃO DESEJADA: "))
        except(ValueError, TypeError):
            print("ERRO! Informe um inteiro:")
        else:
            if op == 1:
                basicos.mensagem("CADASTRO BANCOS")
                lancamentos.insereBANCO(BD)
            elif op == 2:
                basicos.mensagem("CADASTRO LINHAS")
                lancamentos.insereLINHAS(BD)
            elif op == 0:
                basicos.mensagem("VOLTAR AO MENU PRINCIPAL")
                exibiMENUPRINCIPAL(BD)
            else:
                basicos.mensagem("PROCEDIMENTO INVALIDO")
        finally:
            break


def exibirLINHAS(op,BD):
    try:
        arqLancamento = open(BD[3], 'rt')
        arqLinha = open(BD[1], 'rt')
    except:
        basicos.mensagem("Erro ao carregar dados.")
    else:

        opcoes = list()
        valor = list()

        for linhas in arqLinha:
            dado = linhas.split(';')
            if dado[0] == op:
                if dado[1] not in opcoes:
                    opcoes.append(dado[1])
                    valor.append(0)

        for linha in arqLancamento:
            dado = linha.split(';')
            if dado[1] == op:
                if dado[2] in opcoes:
                    valor[int(opcoes.index(dado[2]))] = valor[int(opcoes.index(dado[2]))]+float(dado[3])

        for x in range(0,len(opcoes)):
            print("{:<25} {:<25}".format(opcoes[x], valor[x]))

        print("TOTAL: {}".format(sum(valor)).center(30))
        print("-" * 30)
    finally:
        arqLancamento.close
        arqLinha.close


def exibirBANCOS(BD):
    basicos.mensagem("BANCOS")
    try:
        arq_BD_Banco = open(BD[2], 'rt')
        arq_BD_Lanca = open(BD[3], 'rt')
    except:
        basicos.mensagem("Erro ao carregar dados.")
    else:
        bancos = list()
        bancosNome = list()
        valorMes = list()
        creditos = list()
        debitos = list()
        validacao = False

        for linhas in arq_BD_Banco:
            dado = linhas.split(';')
            if dado[0] not in bancos:
                valorMes.append(dado[2])
                bancos.append(dado[0])
                bancosNome.append(dado[1])
                creditos.append(0)
                debitos.append(0)

        if os.stat(BD[3]).st_size != 0:
            for linha in arq_BD_Lanca:
                dado = linha.split(';')
                if dado[4] in bancos:
                    if dado[1] == 'C':
                        creditos[int(dado[4])] = creditos[int(dado[4])] + float(dado[3])
                    else:
                        debitos[int(dado[4])] = debitos[int(dado[4])] + float(dado[3])
                validacao = True

        for x in range(0,len(bancos)):
            if validacao == True:
                basicos.mensagem(bancosNome[x])
                print('MÊS ANTERIOR: {}'.format(valorMes[x]))
                print('CREDITOS: {}'.format(creditos[x]))
                print('DEBITOS: {}'.format(debitos[x]))
                print('TOTAL: {}'.format(float(valorMes[x])+float(creditos[x])-float(debitos[x])))
            else:
                basicos.mensagem(bancosNome[x])
                print('MÊS ANTERIOR: {}'.format(valorMes[x]))
                print('CREDITOS: {}'.format(0))
                print('DEBITOS: {}'.format(0))
                print('TOTAL: {}'.format(float(0) + float(0) - float(0)))

        print("-" * 30)

    finally:
        arq_BD_Banco.close
        arq_BD_Lanca.close

        op = int(input("Deseja voltar ao menu principal [0-sim/1-nao]?"))
        if op == 0:
            exibiMENUPRINCIPAL(BD)


def exibirHISTORICO(BD):
    mes = input("Informe o mês desejado: ")
    ano = input("Informe o ano desejado: ")
    date = ano+'_'+mes+'_'
    exibirBANCOShistorico(BD, date)


def exibirBANCOShistorico(BD, date):
    basicos.mensagem("BANCOS")
    try:
        arq_BD_Banco = open(date+"bancos.txt", 'rt')
        arq_BD_Lanca = open(date+"lancamentos.txt", 'rt')
    except:
        basicos.mensagem("Erro ao carregar dados.")
    else:
        bancos = list()
        bancosNome = list()
        valorMes = list()
        creditos = list()
        debitos = list()

        for linhas in arq_BD_Banco:
            dado = linhas.split(';')
            if dado[0] not in bancos:
                valorMes.append(dado[2])
                bancos.append(dado[0])
                bancosNome.append(dado[1])
                creditos.append(0)
                debitos.append(0)

        for linha in arq_BD_Lanca:
            dado = linha.split(';')
            if dado[4] in bancos:
                if dado[1] == 'C':
                    creditos[int(dado[4])] = creditos[int(dado[4])] + float(dado[3])
                else:
                    debitos[int(dado[4])] = debitos[int(dado[4])] + float(dado[3])

        for x in range(0,len(bancos)):
            basicos.mensagem(bancosNome[x])
            print('MÊS ANTERIOR: {}'.format(valorMes[x]))
            print('CREDITOS: {}'.format(creditos[x]))
            print('DEBITOS: {}'.format(debitos[x]))
            print('TOTAL: {}'.format(float(valorMes[x])+float(creditos[x])-float(debitos[x])))

        print("-" * 30)

    finally:
        arq_BD_Banco.close
        arq_BD_Lanca.close

        op = int(input("Deseja voltar ao menu principal [0-sim/1-nao]?"))
        if op == 0:
            exibiMENUPRINCIPAL(BD)