"""
Discipline: PROGRAMMING LANGUAGE APPLIED TO AUTOMATION. - LPAA
Teacher: João Fausto Lorenzato de Oliveira
Students: Guilherme Barros, Lukas Ponciano

Project of a system that performs registration, rent or sale to a car rental company in python.

initiation of the program...
"""
# imports

import random as rd 
import pandas as pd

from datetime import datetime
from time import sleep

# Tags

tag = True

# Variaveis globais

lst_ids_ativos = [1]
lst_clientes = []
lst_perfispendentes = []
lst_funcionarios = []
lst_gerentes = []
lst_usuarios = [lst_gerentes ,lst_clientes, lst_funcionarios]
lst_tarifasdiarias = [1,2,3]
lst_dividas = [] # cada item sera uma sublista com indices ID, ID do modelo alugado, data de aluguel, diaria em divida, possiveis multas
lst_estoque = []

# Funcoes e resto do codigo

def main():
    print('Iniciando sistema ...\n')
    print('Locadora de Vans Localiza, bem-vindo(a)!\n')
    
    inicia_sistema()

def inicia_sistema():
    x = 0 # variavel provisoria, apenas para nao estourar o while
    while(tag):
        opcoes_iniciais(x)
        x += 1
        if x==2:
            atualizar_banco()
            break

def opcoes_iniciais(x):
    entrada_inicial = 0
    tp_entrada = ('1','2','3')
    
    if(x==0):
        iniciar_banco_dados()
    
    while(entrada_inicial not in tp_entrada):
        entrada_inicial = raw_input('Opcoes do sistema.\n[1] Login \n[2] Realizar cadastro \n[3] EXIT\n')
    
    if entrada_inicial=='1':
        fazer_login()       
    elif entrada_inicial=='2':
         realizar_cadastro()
    elif entrada_inicial=='3':
        print('Finalizando...')
        sleep(2)
        print('Programa encerrado, Volte sempre!!!')  
    else:
        print ('Opção invalida!!')
        
    return 

def iniciar_banco_dados(): #essa funcao tambem devera atualizar estoques, situacao de alugueis e etc
    # gerente
    arq = open('gerente_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        if k==0:
            lst_add.append((int(x)))
            lst_ids_ativos.append((int(x)))
        elif k==4:
            lst_add.append((int(x)))
        else:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        k = k+1
        if(len(lst_add)==8):
            lst_gerentes.append(lst_add)
            k=0
            lst_add = []
 
    #    print(lst_gerentes)

    arq.close()
    
    # funcionarios
    
    arq = open('funcionarios_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        if k==0:
            lst_add.append((int(x)))
            lst_ids_ativos.append((int(x)))
        elif k==4:
            lst_add.append((int(x)))
        else:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        k = k+1
        if(len(lst_add)==8):
            lst_funcionarios.append(lst_add)
            k=0
            lst_add = []
 
    #    print(lst_funcionarios)

    arq.close()

     # clientes
        
    arq = open('cliente_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        if k==0:
            lst_add.append((int(x)))
            lst_ids_ativos.append((int(x)))
        elif k==4:
            lst_add.append((int(x)))
        else:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        k = k+1
        if(len(lst_add)==8):
            lst_clientes.append(lst_add)
            k=0
            lst_add = []
 
    #    print(lst_clientes)

    arq.close()
    
    # alugueis
    
    arq = open('alugueis_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        if k==1:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        else:
            lst_add.append((int(x)))
            
        k = k+1
        if(len(lst_add)==5):
            lst_dividas.append(lst_add)
            k=0
            lst_add = []

 
    #    print(lst_dividas)

    arq.close()
    
    # estoque
    
    arq = open('estoque_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        lst_estoque.append((int(x)))
        k = k+1
 
    #    print(lst_estoque)

    arq.close()
    
    return

def fazer_login():
    tp_opcao = ('y','n')
    opcao = 'k'
    
    nome_usuario = raw_input("Digite o seu nome de usuario: ")
    senha_usuario = raw_input("Digite sua senha: ")
    print("\nVerificando sistema ...")
    
    chave = checa_login(nome_usuario,senha_usuario)
    
    if chave==1:
        verifica_perfil()
    else:
        while(opcao not in tp_opcao):    
            opcao = raw_input("Algo deu errado. Deseja tentar logar novamente? y ou n")
        if opcao=='y':
            fazer_login()
    return   

def checa_login(username, password):
    
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                if y[6]==password:
                    return 1
                else:
                    return 2
                
def verifica_perfil():
    
    for x in lst_usuarios:
        for y in x:
            if y[7]=='gerente':
                func_gerente()
                return
            elif y[7]=='funcionario':
                func_funcionario()
                return
            elif y[7]=='cliente':
                func_cliente()
                return               

def func_gerente():
    opcao_ger = 0
    tp_libera = ('1','2','3','4', '5', '6', '7','8','9','10','156')
    
    while(opcao_ger not in tp_libera):
        opcao_ger = raw_input('Gerente logado, o que deseja?\n[1] Cadastrar alguem \n[2] Ativar cadastro\n[3] Buscar usuario\n[4] Verificar estoque\n[5] Deletar usuario\n[6] Buscar item\n[7] Atualizar usuario\n[8]Quantidade de usuarios cadastrados\n[9]Alterar perfil de usuario\n[10]Cadastrar item\n[11]Deletar item\n[156] Deslogar\n')
    
    if opcao_ger=='1':
        realizar_cadastro()
    elif opcao_ger=='2':
        ativar_cadastro()
    elif opcao_ger=='3':
        buscar_usuario()
    elif opcao_ger=='4':
        verificar_estoque()
    elif opcao_ger=='5':
        deletar_usuario()
    elif opcao_ger=='6':
        buscar_item()
    elif opcao_ger=='7':
        att_usuario()
    elif opcao_ger=='8':
        quant_usuarios()
    elif opcao_ger=='9':
        alterar_perfil()
    elif opcao_ger=='10':
        cadastrar_item()
    elif opcao_ger=='11':
        deletar_item()
    
    if opcao_ger!='156':
        func_gerente()
    
    return

def func_funcionario():
    return

def func_cliente():
    return

def ativar_cadastro():
    ativar_quem = 0
    qual_perfil = 0
    tp_libera = range(1,len(lst_perfispendentes)+1)
    tp_libera2 = ('1','2','3')
    print("Os usuarios com perfis pendentes sao: \n")
    
    for x in lst_perfispendentes:
        print(x)
        print('\n')
    
    while((int(ativar_quem)) not in tp_libera):
        ativar_quem = raw_input("Quem deseja adicionar? Cada opcao eh um inteiro que vai de 1 ate o maximo disponivel\n")
    
    while(qual_perfil not in tp_libera2):
        print("\nVoce escolheu adicionar o usuario", lst_perfispendentes[(int(ativar_quem))-1])        
        qual_perfil = raw_input("A qual perfil ele pertence?\n[1]Gerente \n[2]Funcionario \n[3]Cliente\n")
        
    if qual_perfil=='1':
        perfil = 'gerente'
    elif qual_perfil=='2':
        perfil = 'funcionario'
    elif qual_perfil=='3':
        perfil = 'cliente'
    
    for x in lst_perfispendentes:
        if x==lst_perfispendentes[(int(ativar_quem))-1]:
            x.append(perfil)
            if perfil=='gerente':
                armazena(x, 2)
            elif perfil=='funcionario':
                armazena(x,3)
            elif perfil=='cliente':
                armazena(x,4)
#            lst_ids_ativos.append(x[0]) 'tirando duvidas quanto a essa linha'
            lst_perfispendentes.remove(x)  
                      
    print('olha os pendentes', lst_perfispendentes)
    print("\nSistema atualizado!\n")
        
    return

def realizar_cadastro():
    lst_perguntas = ['ID','\nNome: ', '\nCPF: ','\nData de nascimento: ', 'idade', '\nLogin desejado: ', '\nSenha escolhida: ']
    lst_dados = []
    x = 0
    
    print('\nEntrada de dados para cadastro. Responda conforme o que for pedido:')
    while(x<7):
        if x==0:
            entrada_dados = gera_id_user()
        elif x==4:
            entrada_dados = gera_idade(lst_dados[3])
        else:
            entrada_dados = raw_input('%s' %(lst_perguntas[x]))
        lst_dados.append(entrada_dados)
        x = x+1
        
    print('Fim do cadastro!\n')
    armazena(lst_dados, 1)
    
#    print(lst_dados)
    
    return

def buscar_usuario():
    exibe()
    ok = 0
    id_user = raw_input("\nDigite o id do usuario que deseja localizar: \n")
    
    for x in lst_usuarios:
        for y in x:
            if y[0]==(int(id_user)):
                print("\nUsuario '%d' encontrado " %(int(id_user)), y)
                ok = 1
                for z in lst_dividas:
                    if (int(id_user==z[0])):
                        print('\nO usuario possui dividas coma empresa: ')
                        print('Usuario: ', z[0], '\nDiarias: ', z[3], '\nMultas: ', z[4])
                    else:
                        print("\nO usuario nao possui dividas com a empresa.\n")
                        
    if ok==0:
        print("\nDesculpe, mas o usuario '%d' nao consta no sistema!\n" %((int(id_user))))
    
    return

def verificar_estoque():
    print("\nEstoque atualizado: ")
    print("\n\tModelos SUV [ID 001]: ", lst_estoque[0])
    print("\n\tModelos Sedan [ID 002]: ", lst_estoque[1])
    print("\n\tModelos Hatch [ID 003]: ", lst_estoque[2])
        
    return

def deletar_usuario():
    exibe()
   
    quem_del = '0'
    
    while((int(quem_del)) not in lst_ids_ativos):
        quem_del = raw_input('\nDigite o id do usuario que deseja apagar do sistema: ')
        
    for x in lst_dividas:
        if x[0]==(int(quem_del)):
            print('O usuario escolhido possui dividas com a empresa. Nao eh possivel apaga-lo\n')
            print(x)
            return         
            
    print('Usuario encontrado. Nao possui dividas pendentes. Apagando ...\n')
    index = 0
    for z in lst_usuarios:
        for w in z:
            if w[0]==(int(quem_del)):
                print lst_clientes
                print w
                lst_ids_ativos.remove(w[0])
                if index==0:
                    lst_gerentes.remove(w)
                elif index==1:
                    lst_clientes.remove(w)
                elif index==2:
                    lst_funcionarios.remove(w)
        index = index + 1                                        
    
        return                                  

def buscar_item():
    tp_id = ('001', '002', '003')
    iden = '0'
    alugados = []
    
    while(iden not in tp_id):
        iden = raw_input('\nDigite o id do modelo que deseja verficar: \n[001] SUV\n[002] Sedan\n[003] Hatch\n ')
    
    for x in lst_dividas:
        for y in x:
            if x==iden:
                alugados.append(x)
    
    print('Modelos %s em estoque: %d' %(iden, (lst_estoque[int(iden)])))
    print('Modelos %s com aluguel ativo: ' %(iden), alugados)
    
    return

def att_usuario():  
    print('Logins dos usuarios cadastrados no sistema: \n')
    dados_novos = []
    exibe()
    
    quem_att = raw_input('\nDigite o id de quem deseja atualizar: ')
    
    if (int(quem_att)) not in lst_ids_ativos:
        print('Usuario nao disponivel\n')
        return   
    
    for x in lst_dividas:
        if x[0]==(int(quem_att)):
            print('O usuario possui dividas com a empresa; atualizacao de perfil indisponivel\n')
            print(x)
            return
    
    att_nome = raw_input('Nome: \n')
    dados_novos.append(att_nome)
    att_cpf = raw_input('CPF: \n')
    dados_novos.append(att_cpf)
    att_datanasc = raw_input('Data de nascimento: \n')
    dados_novos.append(att_datanasc)
    att_idade = gera_idade(att_datanasc)
    dados_novos.append(att_idade)
    att_login = raw_input('Login: \n')
    dados_novos.append(att_login)
    att_senha = raw_input('Senha: \n')
    dados_novos.append(att_senha)
    
    aux = []
    
    
    for x in lst_usuarios:
        for y in x:
            if y[0]==(int(quem_att)):
                aux.append(y[0])
                for z in range(0,6):
                    aux.append(dados_novos[z])
                aux.append(y[7])               
                if y[7]=='gerente':
                    lst_gerentes.remove(y)
                    lst_gerentes.append(aux)
                if y[7]=='cliente':
                    lst_clientes.remove(y)
                    lst_clientes.append(aux)
                if y[7]=='funcionario':
                    lst_funcionarios.remove(y)
                    lst_funcionarios.append(aux)    
        
    return           

def quant_usuarios():
    quant = 0
    for x in lst_usuarios:
        quant = quant + len(x)
    
    print('Contagem atual do sistema: ')    
    print('\n1. Quantidade total de usuarios cadastrados no sistema: %d' %(quant))
    print('2. Quantidade de gerentes: %d' %(len(lst_gerentes)))
    print('3. Quantidade de clientes: %d' %(len(lst_clientes)))
    print('4. Quantidade de funcionarios: %d' %(len(lst_funcionarios)))
    print('5. Quantidade de perfis pendentes de atualziacao: %d' %(len(lst_perfispendentes)))
    
    return

def alterar_perfil():
    exibe()
    quem_alterar = '0'
    tp_perfil = ('gerente', 'funcionario', 'cliente')
    novo_perfil = 'aleat'
    
    quem_alterar = raw_input('\nDigite o ID de quem deseja alterar o perfil: ')
        
    if (int(quem_alterar)) not in lst_ids_ativos:
        print('Usuario nao encontrado.\n')
        return
        
    for x in lst_dividas:
        if x[0]==(int(quem_alterar)):
            print('Usuario pendente na lista de dividas. Impossivel alterar perfil agora', x)
            return
    
    k = 0
    i = 0
    aux = []
    aux2 = []
    
    for x in lst_usuarios:
        for y in x:
            if y[0]==(int(quem_alterar)):
                aux = y
                aux2 = y
                k = i
        i = i+1
    
    while(novo_perfil not in tp_perfil):
        novo_perfil = raw_input('Digite o novo perfil para o seu usuario: ')
    
    aux[7] = novo_perfil
        
    if k==0:
        lst_gerentes.remove(aux2)
    elif k==1:
        lst_clientes.remove(aux2)
    elif k==2:
        lst_funcionarios.remove(aux2)
        
    if novo_perfil=='gerente':
        lst_gerentes.append(aux)
    elif novo_perfil=='cliente':
        lst_clientes.append(aux)
    elif novo_perfil=='funcionario':
        lst_funcionarios.append(aux)
           
    return

def cadastrar_item():
    tp_idcarros = ('001','002','003')
    idcarros = '0'
    
    while(idcarros not in tp_idcarros):
        print(tp_idcarros)
        idcarros = raw_input('Digite o ID que voce deseja cadastrar um novo item: [001]SUV [002] Sedan [003]Hatch\n ')
        
    if idcarros=='001':
        lst_estoque[0] = lst_estoque[0] + 1
    elif idcarros=='002':
        lst_estoque[1] = lst_estoque[1] + 1
    elif idcarros=='003':
        lst_estoque[2] = lst_estoque[2] + 1    
    
    verificar_estoque()
    
    return

def deletar_item():
    tp_idcarros = ('001','002','003')
    idcarros = '0'
    
    while(idcarros not in tp_idcarros):
        idcarros = raw_input('Digite o ID de qual veiculo deseja adicionar um novo item: [001]SUV [002]Sedan [003]Hatch\n')
    
    if idcarros=='001':
        if lst_estoque[0]==0:
            print('Estoque desse modelo esta esgotado. Impossivel deletar.\n')
            return
        lst_estoque[0] = lst_estoque[0] - 1
    elif idcarros=='002':
        if lst_estoque[1]==0:
            print('Estoque desse modelo esta esgotado. Impossivel deletar.\n')
            return
        lst_estoque[1] = lst_estoque[1] - 1
    elif idcarros=='003':
        if lst_estoque[2]==0:
            print('Estoque desse modelo esta esgotado. Impossivel deletar.\n')
            return
        lst_estoque[2] = lst_estoque[2] - 1    
    
    verificar_estoque()
    
    return

def armazena(info, x):
    if x==1:
        lst_perfispendentes.append(info)
        print(lst_perfispendentes)
    elif x==2:
        lst_gerentes.append(info)
        print('\n', lst_gerentes)
    elif x==3:
        lst_funcionarios.append(info)
        print('\n', lst_funcionarios)
    elif x==4:
        lst_funcionarios.append(info)
        print('\n', lst_clientes)
    
    atualizar_banco()
        
    return

def gera_id_user():
    while(1):
        id_user = rd.randint(2,10)
        if not id_user in lst_ids_ativos:
            break

    lst_ids_ativos.append(id_user)

    return id_user

def gera_idade(data_nasc):
    
    dia_nasc = int(data_nasc[0:2])
    mes_nasc = int(data_nasc[2:4])
    ano_nasc = int(data_nasc[4::])
#    print('dia', dia_nasc)
#    print('mes', mes_nasc)
#    print('ano', ano_nasc)
    
    if ano_nasc > (datetime.now().year+100):
        print ('Voce nasceu no futuro?')
    elif ano_nasc < 1900:
        print ('Nao e possivel calcular para antes de 1900, você não pode ser tão old')
    else:
        idade = datetime.now().year - ano_nasc
        if datetime.now().month < mes_nasc:
            idade = idade - 1
        elif datetime.now().month == mes_nasc:
            if datetime.now().day > dia_nasc:
                idade = idade - 1
                
    return idade

def exibe():
    dict_sistema = {}
    lst_exibe = []
    lst_infos_tab = ['ID', 'Nome', 'CPF', 'Data de nasc', 'Idade', 'Login', 'Senha', 'Perfil']
    tag = True
    k=0

    while(tag):
        for x in lst_usuarios:       
            for y in x:
                lst_exibe.append(y[k])
                print lst_exibe
                
                dict_sistema[lst_infos_tab[k]] = lst_exibe
                print lst_infos_tab[k]
    
        if k==len(lst_infos_tab)-1:
            tag = False
        k+=1
        lst_exibe = []

    frame = pd.DataFrame(dict_sistema)
    print frame  

def atualizar_banco():
    
    # gerente
    
    arq = open('gerente_dados.txt', 'w')

    for x in lst_gerentes:
        for y in x:
            arq.writelines((str(y))+'\n')    

    arq.close()
    
    arq = open('funcionarios_dados.txt', 'w')

    for x in lst_funcionarios:
        for y in x:
            arq.writelines((str(y))+'\n')    

    arq.close()
    
    # cliente
    
    arq = open('cliente_dados.txt', 'w')

    for x in lst_clientes:
        for y in x:
            arq.writelines((str(y))+'\n')    

    arq.close()
    
    # alugueis
    
    arq = open('alugueis_dados.txt', 'w')

    for x in lst_dividas:
        for y in x:
            arq.writelines((str(y))+'\n')    

    arq.close()
    
    # estoque
    
    arq = open('estoque_dados.txt', 'w')
    
    for x in lst_estoque:
        arq.writelines((str(x))+'\n')
        
    arq.close()
    
    return
        
main()
