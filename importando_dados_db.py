#Importando Dados Brutos das Tabelas

import sys

##....................................................
# Lendo arquivo de input
leitDados = lerArquivo(APP_DIR + '\\ifrn_servidores.csv')

##....................................................
# Caso dê algum erro na leitura sai do programa
if not leitDados[0]:
    print(leitDados[1])
    sys.exit()

## .................................................
# Tratando os dados lidos
print('\nTratando os Dados Lidos...')
dad_lidos = leitDados[1]

# Gerando SETS com os dados a serem inseridos nas tabelas 
# exceto na tabela ALUNOS
setCategoriaServidor             = set(map(lambda c: c['categoria_servidores'], dad_lidos.values()))
setSetorSiape                    = set(map(lambda c: c['setores_siape'], dad_lidos.values()))
setCampi                         = set(map(lambda c: c['campi'], dad_lidos.values()))
setSetorSuap                     = set(map(lambda c: c['setores_suap'], dad_lidos.values()))
setCargoServidor                 = set(map(lambda c: c['cargo_servidores'], dad_lidos.values()))
setDisciplinasIngresso           = set(map(lambda c: c['disciplina_ingresso'], dad_lidos.values()))

## .............................................................
# Estabelecendo conexão com Database Server
dbConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

# .....................................................
# Caso dê algum erro na conexão sai do programa
if not dbConexao[0]:
    print(dbConexao[1])
    sys.exit()

# Guarda o objeto da conexão 
connDB = dbConexao[1]

## .......................................................
# Inserindo os dados na tabela CATEGORIA_SERVIDORES
print('\nInserindo os dados na tabela CATEGORIA_SERVIDORES...')
dictCatServidor = dict()
for catServ in setCategoriaServidor:
    if not catServ: catServ = '-----'
    retorno = insereCategoria(catServ, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCatServidor[catServ] = retorno[1]

## ........................................................
# Inserindo os dados na tabela SETORES_SIAPE
print('\nInserindo os dados na tabela SETORES_SIAPE...')
dictSetSiape = dict()
for siape in setSetorSiape:
    if not siape: siape = '-----'
    retorno = insereSetorSiape(siape, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSetSiape[siape] = retorno[1]

## ........................................................
# Inserindo os dados na tabela CAMPI
print('\nInserindo os dados na tabela CAMPI...')
dictCampi = dict()
for campus in setCampi:
    if not campus: campus = '-----'
    retorno = insereCampus(campus, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCampi[campus] = retorno[1]

## ........................................................
# Inserindo os dados na tabela SETORES_SUAP
print('\nInserindo os dados na tabela SETORES_SUAP...')
dictSetSuap = dict()
for suap in setSetorSuap:
    if not suap: suap = '-----'
    retorno = insereSetorSuap(suap, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSetSuap[suap] = retorno[1]

## ..........................................................
# Inserindo os dados na tabela CARGO_SERVIDORES
print('\nInserindo os dados na tabela CARGO_SERVIDORES...')
dictCargServ = dict()
for cargo in setCargoServidor:
    if not cargo: cargo = '-----'
    retorno = insereCargo(cargo, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCargServ[cargo] = retorno[1]

## .......................................................
# Inserindo os dados na tabela DISCIPLINA_INGRESSO
print('\nInserindo os dados na tabela DISCIPLINA_INGRESSO...')
dictDiscIngresso = dict()
for disciplina in setDisciplinasIngresso:
    if not disciplina: disciplina = '-----'
    retorno = insereDisciplina(disciplina, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictDiscIngresso[disciplina] = retorno[1]

## .............................................

# Inserindo dados na tabela SERVIDORES
print('\nInserindo os dados na tabela SERVIDORES...')
tuplaCampos = tuple(['matricula'       ,'id_categoria_servidores','url_foto_75x100'         ,'id_setor_suap'             
                     'funcao'          ,'curriculo_lattes'       ,'id_cargo_servidores'     , 
                     'jornada_trabalho', 'campus'                , 'id_setor_siape', 
                     'telefones_institucionais' ,'nome'          , 'id_disciplina_ingresso',                 ])
for k,v in dad_lidos.items():
    if dad_lidos[k]['categoria_servidores']                 == '': dad_lidos[k]['categoria_servidores']         = '-----'
    if dad_lidos[k]['setores_siape']                        == '': dad_lidos[k]['setores_siape']                = '-----'
    if dad_lidos[k]['campi']                                == '': dad_lidos[k]['campi']                        = '-----'
    if dad_lidos[k]['setores_suap']                         == '': dad_lidos[k]['setores_suap']                 = '-----'
    if dad_lidos[k]['cargo_servidores']                     == '': dad_lidos[k]['cargo_servidores']             = '-----'
    if dad_lidos[k]['disciplina_ingresso']                  == '': dad_lidos[k]['situacao_sistemica']           = '-----'

## Falta alterar alguns campos e adicionar outros
    dad_lidos[k]['categoria_servidores']            = dictCatServido[dad_lidos[k]['categoria_servidores']]
    dad_lidos[k]['setores_siape']                   = dictSetSiape[dad_lidos[k]['setores_siape']]
    dad_lidos[k]['campi']                           = dictCampi[dad_lidos[k]['campi']]
    dad_lidos[k]['setores_suap']                    = dictSetSuap[dad_lidos[k]['setores_suapa']]
    dad_lidos[k]['cargo_servidores']                = dictCargServ[dad_lidos[k]['cargo_servidores']]
    dad_lidos[k]['disciplina_ingresso']             = dictDiscIngresso[dad_lidos[k]['disciplina_ingresso']]

    tuplaValores = tuple(v.values())

    retorno = insereAlunos(tuplaCampos, tuplaValores, connDB)

    if not retorno[0]: print(retorno[1])
# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()