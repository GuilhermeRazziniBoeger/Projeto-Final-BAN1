import psycopg2

# configuracoes do banco de dados -> preencher conforme desejado
host = 'localhost'
dbname = 'rede_fast_food_database'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

# string de conexao
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)

# funcao exibe o menu
def mostra_menu():
    print('\n -- Menu --\n')
    print('   1) Inserir nova tupla em tabela\n')
    print('   2) Exibir todas as tuplas de tabela\n')
    print('   3) Exibir os pedidos e seus dados\n')
    print('   4) Exibir os pedidos com avaliacao igual ou superior a 7\n')
    print('   5) Exibir preços mín. e máx. de pratos vendidos igual/acima de quantidade\n')
    print('   6) [Sair]\n')

    print('Selecione o item desejado do menu: ')

# Uma opção para inserir novas tuplas da primeira tabela
# Uma opção para inserir novas tuplas da segunda tabela
# funcao insere nova tupla numa tabela desejada
def insere_nova_tupla():
    print('\n - Inserir nova Tupla -\n')
    tabela_desejada = ''

    print('*Tabelas disponíveis: pedidos, pratos, bebidas, pedidos_pratos, pedidos_bebidas, vendas\n')
    tabela_desejada = input('Insira a tabela a receber a tupla: \n')

    if(tabela_desejada == 'pedidos'):
        print('\n*Tabela pedidos, informe:')
        valor1 = int(input('\nid:'))
        valor2 = int(input('\nid_venda:'))
        valor3 = input('\nobservacoes:')

        comando_sql = 'INSERT INTO pedidos (id, id_venda, observacoes) VALUES ({0}, {1}, {2})'.format(valor1, valor2, valor3)
        
    elif(tabela_desejada == 'pratos'):
        print('\n*Tabela pratos, informe:')
        valor1 = int(input('\nid:'))
        valor2 = input('\nnome:')
        valor3 = int(input('\npeso:'))
        valor4 = input('\npreco:')
        valor5 = input('\nid_cat_prato:')
        comando_sql = 'INSERT INTO pratos (id, nome, peso, preco, id_cat_prato) VALUES ( {0}, {1}, {2}, {3}, {4})'.format(valor1,valor2,valor3,valor4,valor5)
    
    elif(tabela_desejada == 'bebidas'):
        print('\n*Tabela bebidas, informe:')
        valor1 = int(input('\nid:'))
        valor2 = input('\nnome:')
        valor3 = int(input('\nconteudo:'))
        valor4 = input('\npreco:')
        valor5 = input('\nid_cat_bebida:')

        comando_sql = 'INSERT INTO bebidas (id, nome, conteudo, preco, id_cat_bebida) VALUES ({0},{1},{2},{3},{4})'.format(valor1,valor2,valor3,valor4,valor5)
    
    elif(tabela_desejada == 'pedidos_pratos'):
        print('\n*Tabela pedidos_pratos, informe:')
        valor1 = int(input('\nid_pedido:'))
        valor2 = int(input('\nid_prato:'))
        valor3 = int(input('\nquantidade:'))

        comando_sql = 'INSERT INTO pedidos_pratos (id_pedido, id_prato, quantidade) VALUES ({0},{1},{2})'.format(valor1, valor2, valor3)
    
    elif(tabela_desejada == 'pedidos_bebidas'):
        print('\n*Tabela pedidos_bebidas, informe:')
        valor1 = int(input('\nid_pedido:'))
        valor2 = int(input('\nid_bebida:'))
        valor3 = int(input('\nquantidade:'))

        comando_sql = 'INSERT INTO pedidos_bebidas (id_pedido, id_bebida, quantidade) VALUES ({0},{1},{2})'.format(valor1, valor2, valor3)
   
    elif(tabela_desejada == 'vendas'):
        print('\n*Tabela vendas, informe:')
        valor1 = int(input('\nid:'))
        valor2 = int(input('\nid_cliente:'))
        valor3 = int(input('\nid_funcionario:'))
        valor4 = input('\ndata_hora_venda:') # ex: '2022-1-1 14:00:00'
        valor5 = int(input('\navaliacao_cliente:'))

        comando_sql = 'INSERT INTO vendas (id, id_cliente, id_funcionario, data_hora_venda, avaliacao_cliente) VALUES ({0},{1},{2},{3},{4})'.format(valor1,valor2,valor3,valor4,valor5)
    elif(tabela_desejada == ''):
        print('\nTabela inexistente, nao foram feitas alteracoes')
    
    # se a tabela foi informada corretamente, conecta ao banco de dados
    if(tabela_desejada=='pedidos' or tabela_desejada=='pratos' or tabela_desejada=='bebidas' or tabela_desejada=='pedidos_pratos' or tabela_desejada=='pedidos_bebidas' or tabela_desejada=='vendas'):
        # print(comando_sql)

        # conectar ao banco de dados
        conn = psycopg2.connect(conn_string)
        
        # cursor permite executar comandos sql
        cursor = conn.cursor()
        cursor.execute(comando_sql)
        conn.commit()
        cursor.close()
        
        # desconecta do banco de dados
        conn.close()

# Uma opção para listar todas as tuplas da primeira tabela
# Uma opção para listar todas as tuplas da segunda tabela
# funcao exibe todas as tuplas de uma dada tabela
def exibe_todas_as_tuplas():
    print('\n - Exibir Todas as Tuplas -\n')
    tabela_desejada = ''    

    print('*Tabelas disponíveis: pedidos, pratos, bebidas, pedidos_pratos, pedidos_bebidas, vendas\n')
    tabela_desejada = input('Insira qual tabela exibir todas as tuplas : \n')

    comando_sql = 'SELECT * FROM {0}'.format(tabela_desejada)
    retorno_tuplas = ''

    # se a tabela foi informada corretamente, conecta ao banco de dados
    if(tabela_desejada=='pedidos' or tabela_desejada=='pratos' or tabela_desejada=='bebidas' or tabela_desejada=='pedidos_pratos' or tabela_desejada=='pedidos_bebidas' or tabela_desejada=='vendas'):
        print(comando_sql)

        # conectar ao banco de dados
        conn = psycopg2.connect(conn_string)
        
        # cursor permite executar comandos sql
        cursor = conn.cursor()
        cursor.execute(comando_sql)
        retorno_tuplas = cursor.fetchall()        
        conn.commit()
        cursor.close()

        print('\nTuplas da tabela:',tabela_desejada)
        for i in range(len(retorno_tuplas)):
            print(retorno_tuplas[i])
        
        # desconecta do banco de dados
        conn.close()

# Uma opção para listar o resultado de uma consulta que envolva uma junção entre as duas tabelas
def exibe_dados_pedidos():
    print('\n - Exibir os Pedidos e Seus Dados -\n')

    # retorna o número do pedido, junto com as informacoes do prato e bebida deste
    comando_sql = 'SELECT p.id as numero_pedido,pp.id_prato,pp.quantidade as qtde_prato, pb.id_bebida, pb.quantidade as qtde_bebida FROM pedidos_pratos pp JOIN pedidos p ON pp.id_pedido=p.id JOIN pedidos_bebidas pb ON pb.id_pedido=p.id'
    retorno_tuplas = ''
    # conectar ao banco de dados
    conn = psycopg2.connect(conn_string)
    
    # cursor permite executar comandos sql
    cursor = conn.cursor()
    cursor.execute(comando_sql)
    retorno_tuplas = cursor.fetchall()        
    conn.commit()
    cursor.close()

    print('\nDados dos pedidos: ')
    for i in range(len(retorno_tuplas)):
        print(retorno_tuplas[i])
    
    # desconecta do banco de dados
    conn.close()

# Uma opção para listar o resultado de uma consulta que envolva uma junção entre as duas tabelas
def exibe_pedidos_avaliacao_positiva():
    print('\n - Exibir os Pedidos com avaliação maior que 7 -\n')

    # retorna o número do pedido, junto com as informacoes do prato e bebida deste
    comando_sql = 'SELECT p.id as numero_pedido, pp.id_prato, pp.quantidade as qtde_prato, pb.id_bebida, pb.quantidade as qtde_bebida FROM pedidos_pratos pp JOIN pedidos p ON pp.id_pedido=p.id JOIN pedidos_bebidas pb ON pb.id_pedido=p.id WHERE p.id IN (SELECT p.id FROM vendas v JOIN pedidos p ON v.id=p.id_venda WHERE v.avaliacao_cliente>=7)'
    retorno_tuplas = ''

    # conectar ao banco de dados
    conn = psycopg2.connect(conn_string)
    
    # cursor permite executar comandos sql
    cursor = conn.cursor()
    cursor.execute(comando_sql)
    retorno_tuplas = cursor.fetchall()        
    conn.commit()
    cursor.close()

    print('\nPedidos com avaliacao maior que 7: ')
    for i in range(len(retorno_tuplas)):
        print(retorno_tuplas[i])
    
    # desconecta do banco de dados
    conn.close()

# Uma opção para listar o resultado de uma consulta que envolva subconsulta(s) e uma ou mais funções de agregação.
# funcao exibe o preco mín. e máx. de pratos vendidos igual/acima de uma determinada quantidade
def exibe_min_max_pratos_vendidos_quantidade():
    print('\n - Exibir preços mín. e máx. de pratos vendidos igual/acima de quantidade -\n')

    valor = int(input('\nInforme a quantidade desejada:'))

    # retorna o número do pedido, junto com as informacoes do prato e bebida deste
    comando_sql = 'SELECT MIN(preco), MAX(preco) FROM pratos WHERE id IN (SELECT DISTINCT id_prato FROM pedidos_pratos WHERE quantidade>={0})'.format(valor)
    retorno_tuplas = ''

    # conectar ao banco de dados
    conn = psycopg2.connect(conn_string)
    
    # cursor permite executar comandos sql
    cursor = conn.cursor()
    cursor.execute(comando_sql)
    retorno_tuplas = cursor.fetchall()        
    conn.commit()
    cursor.close()

    print('\nPreços mín. e máx. de pratos vendidos igual/acima de '+str(valor)+' unidades: ')
    for i in range(len(retorno_tuplas)):
        print(retorno_tuplas[i])
    
    # desconecta do banco de dados
    conn.close()

if __name__ == '__main__':

    print('\n*** Bem vindo(a) a Aplicação Rede Fast-Food ***\n')

    item_menu = 0

    while(item_menu!=6):
        mostra_menu()
        item_menu = int(input())
        if(item_menu == 1):
            insere_nova_tupla()
        elif(item_menu == 2):
            exibe_todas_as_tuplas()
        elif(item_menu == 3):
            exibe_dados_pedidos()
        elif(item_menu == 4):
            exibe_pedidos_avaliacao_positiva()
        elif(item_menu == 5):
            exibe_min_max_pratos_vendidos_quantidade()
        elif(item_menu == 6):
            print('\n -- Encerrando execução da aplicação --')
        else:
            print('\n*Item inexistente, informe outro')
