# pip install psycopg2 --user
import psycopg2, sys

#Arquivo com Requisições ao Banco de Dados das questões  --- QUESTOES D,E,F

# ...............................................................
def conectaDB(server: str, database: str, dbuser: str, userpwd: str):
    conectado = False
    conexao   = None
    try:
        conexao = psycopg2.connect(f'dbname={database} user={dbuser} host={server} password={userpwd}')
    except:
        conexao = f'ERRO: {sys.exc_info()[0]}'
    else:
        conectado = True
    finally:
        return conectado, conexao

#Estrutura de Conexão
# ...............................................................
def estruturaDB(conexao):
    boolSucesso        = False
    dictEstrutura      = dict()    
    strSQLNomeTabelas  = 'SELECT tables.table_name, tables.table_schema '
    strSQLNomeTabelas += 'FROM information_schema.tables '
    strSQLNomeTabelas += 'WHERE table_schema NOT IN (\'pg_catalog\', \'information_schema\') ' 
    strSQLNomeTabelas += 'AND table_type = \'BASE TABLE\' ORDER BY table_name;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQLNomeTabelas)
    except:
        dictEstrutura = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstTabelas = cursorTable.fetchall()
        for tabela in lstTabelas:
            retornoFields = listaCampi(tabela[0], conexao)
            #retornoPKS    = listaPK(tabela[0], conexao)
            dictEstrutura[tabela[0]] = { 'schema'     : tabela[1],
                                         #'primary_key': retornoPKS[1],
                                         'campos'     : retornoFields[1],
                                         'tipos'      : retornoFields[2] }
    finally:
        return boolSucesso, dictEstrutura


# ...............................................................
# ........... CONSULTA CAMPI .............
def listaCampi(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomeCampi      = list()
    lstTipoCampi      = list()
    strSQLNomeCampus   = 'SELECT campi.campus AS sigla,categoria_servidores.categoria,servidores.matricula'
    strSQLNomeCampus  += 'COUNT(servidores.id_categoria_servidores) AS qtd_categoria_serv'
    strSQLNomeCampus  += 'FROM servidores'
    strSQLNomeCampus  += 'INNER JOIN categoria_servidores ON servidores.id_categoria_servidores = categoria_servidores.id_categoria_servidores'
    strSQLNomeCampus  += 'INNER JOIN servidores ON servidores.campus = campi.campus' 
    strSQLNomeCampus  += 'GROUP BY servidores.matricula,campi.campus,categoria_servidores.categoria;'
    try:
        cursorFields = conexao.cursor()
        cursorFields.execute(strSQLNomeCampus)
    except:
        lstNomeCampi = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstCampi   = cursorFields.fetchall()
        for campus in lstCampi:
            lstNomeCampi.append(campus[0])
            lstTipoCampi.append(campus[1])
    finally:
        return boolSucesso, lstNomeCampi, lstTipoCampi
# ................................................................
# ...... CONSULTA DOCENTES ..............
def listaDocente(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomeDocente      = list()
    lstTipoCampos      = list()
    strSQLNomeDocente   = 'SELECT  servidores.matricula,servidores.nome,categoria_servidores.categoria,disciplina_ingresso.disciplina,campi.campus'
    strSQLNomeDocente  += 'COUNT(disciplina_ingresso.id) AS qtd_disciplina'
    strSQLNomeDocente  += 'FROM servidores, categoria_servidores, disciplina_ingresso, campi'
    strSQLNomeDocente  += 'WHERE categoria_servidores.categoria = 'docente''
    strSQLNomeDocente  += 'INNER JOIN servidores ON servidores.id_disciplina_ingresso = disciplina_ingresso.id'
    strSQLNomeDocente  += 'GROUP BY servidores.matricula,categoria_servidores.categoria,disciplina_ingresso.disciplina;'
    try:
        cursorFields = conexao.cursor()
        cursorFields.execute(strSQLNomeDocente)
    except:
        lstNomeDocente = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstCampos   = cursorFields.fetchall()
        for campos in lstCampos:
            lstNomeDocente.append(campos[0])
            lstTipoCampos.append(campos[1])
    finally:
        return boolSucesso, lstNomeDocente, lstTipoCampos

# ...... CONSULTA DISCIPLINA POR CAMPUS ..............
def listaDisciplina(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomeDisciplina      = list()
    lstTipoDisciplina      = list()
    strSQLNomeDisciplina   = 'SELECT servidores.matriculaservidores.nome,categoria_servidores.categoria,disciplina_ingresso.disciplina,campi.campus'
    strSQLNomeDisciplina  += 'COUNT(disciplina_ingresso.id) AS qtd_disciplina'
    strSQLNomeDisciplina  += 'FROM disciplina_ingresso'
    strSQLNomeDisciplina  += 'INNER JOIN servidores ON servidores.id_disciplina_ingresso = disciplina_ingresso.id'
    strSQLNomeDisciplina  += 'INNER JOIN servidores ON servidores.campus = campi.campus'
    strSQLNomeDisciplina  += 'GROUP BY disciplina_ingresso.id,campi.campus;'
    try:
        cursorFields = conexao.cursor()
        cursorFields.execute(strSQLNomeDisciplina)
    except:
        lstNomeDisciplina = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstDisciplina   = cursorFields.fetchall()
        for campos in lstDisciplina:
            lstNomeDisciplina.append(campos[0])
            lstTipoDisciplina.append(campos[1])
    finally:
        return boolSucesso, lstNomeDisciplina, lstTipoDisciplina