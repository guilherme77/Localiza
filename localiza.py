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
lst_gerentes = []
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
    
    while(entrada_inicial not in tp_entrada):
        entrada_inicial = raw_input('Opcoes do sistema.\n[1] Login \n[2] Realizar cadastro \n[3] Teste admin \n[4] EXIT\n')
    
    if entrada_inicial=='1':
        print('o sport ta na final')       
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

  return

def gera_idade(data_nasc):
    idade = 0
    while (idade < 0):
        if data_nasc > datetime.now().year:
            print ('Voce nasceu no futuro?')
            continue
        if data_nasc < 1900:
            print ('Nao e possivel calcular para antes de 1900, você não pode ser tão old')
            continue
        else:
            idade = datetime.now().year - data_nasc
            
    return idade

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
