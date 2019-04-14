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

logadm = ['admin']
keyadm = ['54321']

lst_ids_ativos = [1]
lst_clientes = []
lst_perfispendentes = []
lst_funcionarios = []
lst_gerentes = [[1, 'Carlos Muniz', '86541235509', '29071980', 38, 'carlos_ger', 'iokA12', 'gerente']]
lst_usuarios = [lst_gerentes ,lst_clientes, lst_funcionarios]
lst_tarifasdiarias = [1,2,3]

# Funcoes e resto do codigo

def main():
    print('Iniciando sistema ...\n')
    print('Locadora de Vans Localiza, bem-vindo(a)!\n')
    
    inicia_sistema()

def inicia_sistema():
    x = 0 # variavel provisoria, apenas para nao estourar o while
    while(tag):
        opcoes_iniciais()
        x += 1
        if x==2:
            break

def opcoes_iniciais():
    entrada_inicial = 0
    tp_entrada = ('1','2','3','4')
    
    iniciar_banco_dados()
    
    while(entrada_inicial not in tp_entrada):
        entrada_inicial = raw_input('Opcoes do sistema.\n[1] Login \n[2] Realizar cadastro \n[3] Teste admin \n[4] EXIT\n')
    
    if entrada_inicial=='1':
        fazer_login()       
    elif entrada_inicial=='2':
         realizar_cadastro()
    elif entrada_inicial=='3':
            admin()
            #problema de range...
    elif entrada_inicial=='4':
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
            elif y[7]=='funcionario':
                func_funcionario()
            elif y[7]=='cliente':
                func_cliente()   
    return                

def func_gerente():
    opcao_ger = 0
    tp_libera = ('1','2')
    
    while(opcao_ger not in tp_libera):
        opcao_ger = raw_input('Gerente logando, o que deseja?\n[1] Cadastrar alguem \n[2] Ativar cadastro\n')
    
    if opcao_ger=='1':
        realizar_cadastro()
    if opcao_ger=='2':
        ativar_cadastro()
    
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
            delete = x
            x.append(perfil)
            if perfil=='gerente':
                armazena(x, 2)
            elif perfil=='funcionario':
                armazena(x,3)
            elif perfil=='cliente':
                armazena(x,4)
                
    lst_ids_ativos.remove(delete[0])
            
    lst_perfispendentes.remove(delete)      
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
    lst_infos_tab = ['ID', 'Nome', 'CPF', 'Data de nasc', 'Idade', 'Login', 'Senha', 'Perfil', 'Dívida']
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

def admin():
    
    user = input('Usuário: ')
    while not user in logadm:
        user = input ('Usuário não existe: ')
    
    key = input ('Senha: ')
    while not key in keyadm:
        key = input ('Senha incorreta: ')
        
    return
##    lst_perfispendente.append(lst_dados) aparentemente só funciona com a lista passando como parâmetro
        
main()
