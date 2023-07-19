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


# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()