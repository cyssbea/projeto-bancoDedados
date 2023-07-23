# pip install psycopg2 --user
import psycopg2, sys


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

## Atualizar estrutura de conexão
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
def listaCampi(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomeCampi      = list()
    lstNomeCampi      = list()
    strSQLNomeCampus   = 'SELECT campi.* AS sigla, categoria_servidores.categoria, servidores.matricula'
    strSQLNomeCampus  += 'COUNT(servidores.id_categoria_servidores) AS qtd_categoria_serv'
    strSQLNomeCampus  += 'FROM servidores.servidores'
    strSQLNomeCampus  += f'INNER JOIN servidores.campus ON servidores.campus = campi.campus  '
    strSQLNomeCampus  += 'GROUP BY servidores.campus, campi.campus'
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
        