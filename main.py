import basicos, arquivos, exibicao

data = basicos.recebeDATA()
dataF = data[6:10]+"_"+data[3:5]+"_"
ext = '.txt'

BD = ['log'+ext,
      'linhas'+ext,
      dataF + 'bancos' + ext,
      dataF + 'lancamentos' + ext
     ]

for x in range(0,len(BD)):
    arq = BD[x]
    arquivos.verificacaoARQUIVO(arq)

basicos.mensagem("Bem Vindo!")
exibicao.exibiMENUPRINCIPAL(BD)
