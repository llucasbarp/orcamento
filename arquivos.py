import basicos,os

def verificacaoARQUIVO(arq):
    if os.path.exists(arq):
        basicos.mensagem('Base: '+arq+' | Carregada com Sucesso')
    else:
        basicos.mensagem('Base ' + arq + ' não encontrada')
        criacaoARQUIVO(arq)


def criacaoARQUIVO(arq):
    basicos.mensagem("Criando arquivo: " + arq)
    try:
        arquivo = open(arq, 'a')
        arquivo.close(arq)
    except:
        if os.path.exists(arq):
            basicos.mensagem("Arquivo "+arq+ " Criado")
        else:
            basicos.mensagem("Erro ao criar o arquivo")
    finally:
        if arq[8:14] == 'bancos':
            registro(arq)


def registro(arq):
    basicos.mensagem('REGISTROS ACESSADO')
    try:
        registro = open('log.txt', 'r')
        registro.close()
    except:
        basicos.mensagem('ERRO ao abrir os REGISTROS')
    else:
        import os
        if os.stat('log.txt').st_size == 0:
            registro = open('log.txt', 'wt')
            nome = str(input("Infome o seu nome: "))
            registro.write("{};{};".format(nome, 1))
        else:
            registro = open('log.txt', 'r+')
            for linhas in registro:
                dado = linhas.split(';')
            registro.close()
            registro = open('log.txt', 'w+')
            registro.write("{};{};".format(dado[0], int(dado[1]) + 1))
            copiaBANCOS(arq)
    finally:
        registro.close()


def copiaBANCOS(arq):
    basicos.mensagem("INICIANDO COPIA DE BANCOS")
    meses = ['12','01','02','03','04','05','06','07','08','09','10','11','12']
    try:
        ind = arq[5:7]
        nome_antigo = arq.replace(str(ind), str(meses[int(ind) - 1]))
        dadosVALOR = valorBANCOS(nome_antigo)
        novo = open(arq, 'at')
        antigo = open(nome_antigo, 'rt')

    except:
        basicos.mensagem("Erro ao copiar")

    else:
        cont = 0
        for linhas in antigo:
            dado = linhas.split(';')
            novo.write("{};{};{};\n".format(dado[0],dado[1],dadosVALOR[cont]))
            cont = cont+1

    finally:
        antigo.close()
        novo.close()


def valorBANCOS(banco):
    try:
        arq_BD_Banco = open(banco, 'rt')
        lancamento = banco.replace('bancos','lancamentos')
        arq_BD_Lanca = open(lancamento, 'rt')

    except:
        basicos.mensagem("Erro ao carregar dados.")

    else:
        bancos = list()
        bancosNome = list()
        valorMes = list()
        creditos = list()
        debitos = list()
        totBANCOS = list()

        for linhas in arq_BD_Banco:
            dado = linhas.split(';')
            if dado[0] not in bancos:
                valorMes.append(dado[2])
                bancos.append(dado[0])
                bancosNome.append(dado[1])
                creditos.append(0)
                debitos.append(0)
                totBANCOS.append(0)

        for linha in arq_BD_Lanca:
            dado = linha.split(';')
            if dado[4] in bancos:
                if dado[1] == 'C':
                    creditos[int(dado[4])] = creditos[int(dado[4])] + float(dado[3])
                else:
                    debitos[int(dado[4])] = debitos[int(dado[4])] + float(dado[3])

        for x in range(0,len(bancosNome)):
            val = float(valorMes[x])+float(creditos[x])-float(debitos[x])
            print(val)
            totBANCOS[x]=float(val)

    finally:
        arq_BD_Banco.close()
        arq_BD_Lanca.close()

        return totBANCOS