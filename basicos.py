import time, exibicao

def menuPRINCIPAL(BD):
    mensagem("MENU PRINCIPAL!")
    mensagem("CREDITO")
    exibicao.exibirLINHAS('C', BD)
    mensagem("DEBITO")
    exibicao.exibirLINHAS('D', BD)

    mensagem("OQUE DESEJA FAZER")
    print("1 - EXIBIR BANCOS")
    print("2 - LANÇAMENTOS")
    print("3 - HISTORICO")
    print("4 - OPÇÕES")
    print("0 - SAIR")
    print("-"*30)


def menuOPCOES():
    mensagem("OPCÕES!")
    mensagem("OQUE DESEJA FAZER")
    print("1 - CADASTRAR BANCOS")
    print("2 - CADASTRAR LINHAS")
    print("0 - VOLTAR AO MENU PRINCIPAL")
    print("-"*30)


def mensagem(msg):
    print("-"*30)
    print(msg.center(30))
    print("-"*30)
    time.sleep(1)


def msgSIMPES(msg):
    print(msg.center(30))
    time.sleep(1)


def recebeDATA():
    from datetime import date
    data = date.today()
    dataD = data.strftime('%d/%m/%Y')
    return dataD
