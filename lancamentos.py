import basicos,exibicao

def lancamento(BD):
    basicos.mensagem("LANÇAMENTO DE REGISTRO")

    cd = str(input("Credito ou Debito [C/D]: ")).upper()
    op = verificacaoOPCOES(BD,cd)
    basicos.msgSIMPES("Tipos de Lançamentos:")
    for x in range(0,len(op)):
        print("{:<20} {:<20}".format(x, op[x]))
    nt = int(input("Informe o tipo: "))
    tipo = op[nt]
    valor = float(input("Informe o valor: "))
    op2 = verificacaoBANCOS(BD)
    basicos.msgSIMPES("Seus bancos:")
    for x in range(0, len(op2)):
        print("{:<20} {:<20}".format(x, op2[x]))
    banco = int(input("Informe o banco: "))

    escreveLANCAMENTO(BD,cd,tipo,valor,banco)


def escreveLANCAMENTO(BD,cd,tipo,valor,banco):
    try:
        a = open(BD[3], 'at')
    except:
        basicos.mensagem("Erro ao abrir o arquivo")
    else:
        try:
            id = recebeID(BD[0])
            data = basicos.recebeDATA()
            a.write("{};{};{};{};{};{};\n".format(id,cd,tipo,valor,banco,data))
        except:
            basicos.mensagem("Erro ao efetuar lançamento")
        else:
            basicos.mensagem("Registro adicionado em {}".format(a))
    finally:
        a.close()
        exibicao.exibiMENUPRINCIPAL(BD)


def verificacaoOPCOES(BD,cd):
    try:
        a = open(BD[1], 'rt')
    except:
        basicos.mensagem("Erro ao abrir o arquivo")
    else:
        try:
            opcoes = list()
            for linha in a:
                dado = linha.split(';')
                if dado[0] == cd:
                    opcoes.append(dado[1])
            return opcoes
        except:
            basicos.mensagem("Erro ao escrever no arquivo")
        else:
            basicos.mensagem("Registro adicionado")


def verificacaoBANCOS(BD):
    try:
        a = open(BD[2], 'rt')
    except:
        basicos.mensagem("Erro ao abrir o arquivo")
    else:
        try:
            opcoes = list()
            for linha in a:
                dado = linha.split(';')
                if dado[0] not in opcoes:
                    opcoes.append(dado[1])
            return opcoes
        except:
            basicos.mensagem("Erro ao escrever no arquivo")
        else:
            basicos.mensagem("Registro adicionado")
    finally:
        a.close()


def recebeID(arq):
    try:
        a = open(arq, 'rt')
    except:
        print("Erro ao abrir o arquivo")
    else:
        try:
            id = int()
            for linhas in a:
                id = id + 1
        except:
            print("Erro ao calcular id")
        else:
            return id
    finally:
        a.close()


def insereBANCO(BD):
    try:
        a = open(BD[2], 'at')
    except:
        basicos.mensagem("Erro ao abrir o arquivo")
    else:
        try:
            id = recebeID(BD[2])
            nome = str(input("Informe o nome do banco: "))
            saldo = float(input("Informe o saldo inicial: "))
            a.write("{};{};{};\n".format(id,nome,saldo))
        except:
            basicos.mensagem("Erro ao efetuar lançamento")
        else:
            basicos.mensagem("Registro adicionado")
    finally:
        a.close()
        exibicao.exibiMENUPRINCIPAL(BD)


def insereLINHAS(BD):
    try:
        a = open(BD[1], 'at')
    except:
        basicos.mensagem("Erro ao inserir linhas")
    else:
        try:
            tipo = str(input("Informe o tipo de linha[C/D]: ")).upper()
            nome = str(input("Informe o nome: ")).upper()
            a.write("{};{};\n".format(tipo,nome))
        except:
            basicos.mensagem("Erro ao efetuar lançamento")
        else:
            basicos.mensagem("Registro adicionado")
    finally:
        a.close()