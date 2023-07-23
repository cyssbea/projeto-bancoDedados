# pip install psycopg2 --user
import psycopg2, sys

# ------------------------------------------------------------
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

# ------------------------------------------------------------
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
            retornoPKS    = listaPK(tabela[0], conexao)
            retornoFields = listaCampos(tabela[0], conexao)
            dictEstrutura[tabela[0]] = { 'schema'     : tabela[1],
                                         'primary_key': retornoPKS[1],
                                         'campos'     : retornoFields[1],
                                         'tipos'      : retornoFields[2] }
    finally:
        return boolSucesso, dictEstrutura


# ------------------------------------------------------------
def listaPK(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomePrimaryKey  = list()
    strSQLPrimaryKeys  = 'SELECT key_column_usage.column_name '
    strSQLPrimaryKeys += 'FROM information_schema.table_constraints '
    strSQLPrimaryKeys += 'JOIN information_schema.key_column_usage '
    strSQLPrimaryKeys += 'ON table_constraints.constraint_name = key_column_usage.constraint_name '
    strSQLPrimaryKeys += 'WHERE	table_constraints.constraint_type = \'PRIMARY KEY\' ' 
    strSQLPrimaryKeys += 'AND table_constraints.table_schema NOT IN '
    strSQLPrimaryKeys += '(\'pg_catalog\', \'information_schema\') '
    strSQLPrimaryKeys += f'AND table_constraints.table_name = \'{nomeTabela}\';'
    try:
        cursorPK = conexao.cursor()
        cursorPK.execute(strSQLPrimaryKeys)
    except:
        lstNomePrimaryKey = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstPrimaryKeys = cursorPK.fetchall()
        for pks in lstPrimaryKeys:
            for pk in pks:
                lstNomePrimaryKey.append(pk)
    finally:
        return boolSucesso, lstNomePrimaryKey


# ------------------------------------------------------------
def listaCampos(nomeTabela: str, conexao):
    boolSucesso        = False
    lstNomeCampos      = list()
    lstTipoCampos      = list()
    strSQLNomeCampos   = 'SELECT columns.column_name, columns.data_type '
    strSQLNomeCampos  += 'FROM information_schema.columns '
    strSQLNomeCampos  += 'WHERE table_schema NOT IN (\'pg_catalog\', \'information_schema\') '
    strSQLNomeCampos  += f'AND table_name = \'{nomeTabela}\' '
    strSQLNomeCampos  += 'ORDER BY table_name, ordinal_position;'
    try:
        cursorFields = conexao.cursor()
        cursorFields.execute(strSQLNomeCampos)
    except:
        lstNomeCampos = f'{sys.exc_info()}'
    else:
        boolSucesso = True
        lstCampos   = cursorFields.fetchall()
        for campos in lstCampos:
            lstNomeCampos.append(campos[0])
            lstTipoCampos.append(campos[1])
    finally:
        return boolSucesso, lstNomeCampos, lstTipoCampos
        