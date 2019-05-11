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
import matplotlib.pyplot as pp

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
lst_dividas = [] # cada item sera uma sublista com indices ID, ID do modelo alugado, data de aluguel, diaria em divida, possiveis multas
lst_suv = [] # formato nome,id_tipo, ano, placa, chaci, diaria, multa do modelo
lst_sedan = []
lst_hatch = []
lst_alugados = []
lst_estoque = [lst_suv, lst_sedan, lst_hatch]

# Funcoes e resto do codigo

def main():
    print('Iniciando sistema ...\n')
    print('Locadora de Carros Localiza, bem-vindo(a)!\n')
    
    inicia_sistema()

def inicia_sistema():
    x = 0
    while(tag):
        opcoes_iniciais(x)
        op = raw_input('Encerrar sistema?y para continuar\n')
        if op=='y':
            atualizar_banco()
            break
        x = x+1

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
        if(len(lst_add)==6):
            lst_dividas.append(lst_add)
            k=0
            lst_add = []
 
    #    print(lst_dividas)

    arq.close()
    
    # itens alugados
    
    arq = open('itensalugados_dados.txt', 'r')
    linha = arq.readlines()
    lst_add = []
    k=0

    for x in linha:
        if k==5 or k==6:
            lst_add.append((int(x)))
        else:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        
        k = k+1
        if(len(lst_add)==7):
            lst_alugados.append(lst_add)
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
        if k==5 or k==6:
            lst_add.append((int(x)))
        else:
            new = x.replace(x, x[:-1])
            lst_add.append(new)
        k = k+1
        if(len(lst_add)==7):
            if lst_add[1]=='001':
                lst_suv.append(lst_add)
            elif lst_add[1]=='002':
                lst_sedan.append(lst_add)
            elif lst_add[1]=='003':
                lst_hatch.append(lst_add)
            k=0
            lst_add = []
 
    #    print(lst_suv)

    arq.close()
    
    # perfis pendentes
    
    arq = open('perfispendentes_dados.txt', 'r')
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
        if(len(lst_add)==7):
            lst_perfispendentes.append(lst_add)
            k=0
            lst_add = []
    
    return

def fazer_login():
    tp_opcao = ('y','n')
    opcao = 'k'
    
    nome_usuario = raw_input("Digite o seu nome de usuario: ")
    senha_usuario = raw_input("Digite sua senha: ")
    print("\nVerificando sistema ...")
    
    chave = checa_login(nome_usuario,senha_usuario)
    
    if chave==1:
        verifica_perfil(nome_usuario)
    else:
        while(opcao not in tp_opcao):    
            opcao = raw_input("Algo deu errado. Deseja tentar logar novamente? y para continuar\n")
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
                
def verifica_perfil(username):    
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                gera_multa()
                log(username, 'Login iniciado')
                if y[7]=='gerente':                   
                    func_gerente(username)
                    return
                elif y[7]=='funcionario':
                    func_funcionario(username)
                    return
                elif y[7]=='cliente':
                    func_cliente(username)
                    return                

def func_gerente(username):
    opcao_ger = 0
    tp_libera = ('1','2','3','4', '5', '6', '7','8','9','10','11','12','13','14','15','16', '156')
    
    while(opcao_ger not in tp_libera):
        opcao_ger = raw_input('Gerente logado, o que deseja?\n[1] Cadastrar alguem \n[2] Ativar cadastro\n[3] Buscar usuario\n[4] Verificar estoque\n[5] Deletar usuario\n[6] Buscar item\n[7] Atualizar usuario\n[8]Quantidade de usuarios cadastrados\n[9]Alterar perfil de usuario\n[10]Cadastrar item\n[11]Deletar item\n[12]Ver graficos\n[13]Dados do sistema\n[14]Verificar operacoes de um dado usuario\n[15]Contabilizar divida paga ao sistema\n[16]Limpar lista de perfis pendentes\n[156] Deslogar\n')
    
    if opcao_ger=='1':
        log(username, 'Realizar cadastro')
        realizar_cadastro()
    elif opcao_ger=='2':
        log(username, 'Ativar cadastro')
        ativar_cadastro()
    elif opcao_ger=='3':
        log(username, 'Buscar usuario')
        buscar_usuario(username)
    elif opcao_ger=='4':
        log(username, 'Verificar estoque')
        verificar_estoque()
    elif opcao_ger=='5':
        log(username, 'Deletar usuario')
        deletar_usuario(username)
    elif opcao_ger=='6':
        log(username, 'Buscar item')
        buscar_item()
    elif opcao_ger=='7':
        log(username, 'Atualizar usuario')
        att_usuario(username)
    elif opcao_ger=='8':
        log(username, 'Verificar quantidade de usuarios')
        quant_usuarios()
    elif opcao_ger=='9':
        log(username, 'Alterar perfil de usuario')
        alterar_perfil(username)
    elif opcao_ger=='10':
        log(username, 'Cadastrar item')
        cadastrar_item()
    elif opcao_ger=='11':
        log(username, 'Deletar item')
        deletar_item()
    elif opcao_ger=='12':
        log(username, 'Verificar graficos')
        graficos()
    elif opcao_ger=='13':
        log(username, 'Ver dados do sistema')
        exibe('gerente')
    elif opcao_ger=='14':
        log(username, 'Ver operacoes de um dado usuario')
        ver_operacoes(username)
    elif opcao_ger=='15':
        log(username, 'Confirmar o pagamento de divida')
        fim_aluguel()
    elif opcao_ger=='16':
        log(username, 'Limpar perfis pendentes')
        limpar_perfispendentes()
    
    if opcao_ger!='156':
        func_gerente(username)
    
    log(username, 'Login encerrado')
    
    return

def func_funcionario(username):
    opcao_func = 0
    tp_libera = ('1','2','3','4','5','6','7','156')
    
    while(opcao_func not in tp_libera):
        opcao_func = raw_input('Funcionario logado. O que deseja?\n[1]Verificar estoque\n[2]Cadastrar_item\n[3]Deletar item\n[4]Buscar usuario\n[5]Fazer cadastro\n[6]Atualizar usuario\n[7]Confirmar pagamento de divida\n[156]Deslogar\n')
    
    if opcao_func=='1':
        log(username, 'Verificar estoque')
        verificar_estoque()
    elif opcao_func=='2':
        log(username, 'Cadastrar item')
        cadastrar_item()
    elif opcao_func=='3':
        log(username, 'Deletar item')
        deletar_item()
    elif opcao_func=='4':
        log(username, 'Buscar usuario')
        buscar_usuario(username)
    elif opcao_func=='5':
        log(username, 'Fazer cadastro')
        realizar_cadastro()
    elif opcao_func=='6':
        log(username, 'Atualizar usuario')
        att_usuario(username)
    elif opcao_func=='7':
        log(username, 'Confirmar o pagamento de divida')
        fim_aluguel()
        
    if opcao_func!='156':
        func_funcionario(username)
    
    log(username, 'Login encerrado')
    
    return

def func_cliente(username):
    opcao_cli = 0
    tp_libera = ('1','2','3')
    
    while(opcao_cli not in tp_libera):
        opcao_cli = raw_input('Cliente logado, o que deseja?\n[1] Alugar carro\n[2]Verificar meu status\n[3]Deslogar\n')
    
    if opcao_cli=='1':
        log(username, 'Alugar carro')
        alugar_carro(username)
    elif opcao_cli=='2':
        log(username, 'Verificar status')
        verifica_status(username)
    
    if opcao_cli!='3':
        func_cliente(username)
        
    log(username, 'Login encerrado')
    
    print('Saindo\n')
    
    return

def ativar_cadastro():
    ativar_quem = 0
    qual_perfil = 0
    tp_libera = range(1,len(lst_perfispendentes)+1)
    tp_libera2 = ('1','2','3')
    
    if len(lst_perfispendentes)==0:
        print('Nao ha perfis pendentes.\n')
        return
    
    print("Os usuarios com perfis pendentes sao: \n")
    
    for x in lst_perfispendentes:
        print(x)
        print('\n')
        
    conf = raw_input('Deseja realmente adicionar alguem ao sistema?y para continuar\n')
    
    if conf=='n':
        print('Operacao cancelada.\n')
        return
    
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
    lst_perguntas = ['ID','\nNome: ', '\nCPF, sem espacos, tracos ou pontos, 11 dig: ','\nData de nascimento: sequencia oito digitos numericos sem espacos entre si - diamesano: ', 'idade', '\nLogin desejado: ', '\nSenha escolhida: ']
    lst_dados = []
    x = 0
    
    print('\nEntrada de dados para cadastro. Responda conforme o que for pedido:')
    while(x<7):
        if x==0:
            entrada_dados = gera_id_user()
        elif x==4:
            entrada_dados = gera_idade(lst_dados[3])
        else:
            if x==3:
                ok = 0
                while ok!=1:
                    entrada_dados = raw_input('%s' %(lst_perguntas[x]))
                    ok = verif_data(entrada_dados)
            elif x==5:
                ok = 0
                while ok==0:
                    entrada_dados = raw_input('%s' %(lst_perguntas[x]))
                    ok = login_existe(entrada_dados)
            elif x==2:
                ok = 0
                while ok==0:
                    entrada_dados = raw_input('%s' %(lst_perguntas[x]))
                    ok = verif_cpf(entrada_dados)
            else:                   
                entrada_dados = raw_input('%s' %(lst_perguntas[x]))
        
        lst_dados.append(entrada_dados)
        x = x+1
        
    print('Fim do cadastro!\n')
    armazena(lst_dados, 1)
    
#    print(lst_dados)
    
    return

def buscar_usuario(username):
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                perfil = y[7]
                exibe(perfil)
    ok = 0
    div = 0
    id_user = raw_input("\nDigite o id do usuario que deseja localizar: \n")
    
    if perfil=='funcionario':
        for x in lst_gerentes:
            if int(x[0])==int(id_user):
                print('Esse perfil pertence a um gerente, voce nao possui acesso!\n')
                return
    
    for x in lst_usuarios:
        for y in x:
            if y[0]==(int(id_user)):
                print("\nUsuario '%d' encontrado " %(int(id_user)))
                ok = 1
                for z in lst_dividas:
                    if (int(id_user) == z[0]):
                        print('\nO usuario possui dividas com a empresa: ')
                        print('Usuario: ID ' + str(z[0]) + '\nNumero de chassi do carro: ' + z[1] + '\nDiarias R$: ' +  str(z[3]) + '\nMultas: R$ ' + str(z[4]))
                        div = div + 1
    if div==0:
        print("\nO usuario nao possui dividas com a empresa.\n")
                        
    if ok==0:
        print("\nDesculpe, mas o usuario '%d' nao consta no sistema!\n" %((int(id_user))))
    
    return

def verificar_estoque():
    print("\nEstoque atualizado: ")
    print("\n\tModelos SUV [ID 001]: " + str(len(lst_suv)) + " em estoque")
    for x in lst_suv:
        print('Nome: ' + x[0] + '\n' + 'ID do modelo: ' + x[1] + '\n' + 'Ano: ' + x[2] + '\n' + 'Placa: ' + x[3] + '\n' + 'Chassi: ' + x[4] + '\n' + 'Diaria: R$ ' + str(x[5]) + '\n' + 'Multa (por dia): R$ ' + str(x[6]) + '\n')
        print('\n')
    print("\n\tModelos Sedan [ID 002]: " + str(len(lst_sedan)) + " em estoque")
    for x in lst_sedan:
        print('Nome: ' + x[0] + '\n' + 'ID do modelo: ' + x[1] + '\n' + 'Ano: ' + x[2] + '\n' + 'Placa: ' + x[3] + '\n' + 'Chassi: ' + x[4] + '\n' + 'Diaria: R$ ' + str(x[5]) + '\n' + 'Multa (por dia): R$ ' + str(x[6]) + '\n')
        print('\n')
    print("\n\tModelos Hatch [ID 003]: " + str(len(lst_hatch)) + " em estoque")
    for x in lst_hatch:
        print('Nome: ' + x[0] + '\n' + 'ID do modelo: ' + x[1] + '\n' + 'Ano: ' + x[2] + '\n' + 'Placa: ' + x[3] + '\n' + 'Chassi: ' + x[4] + '\n' + 'Diaria: R$ ' + str(x[5]) + '\n' + 'Multa (por dia): R$ ' + str(x[6]) + '\n')
        print('\n')
        
    return

def deletar_usuario(username):
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                exibe(y[7])
   
    quem_del = '0'
    
    while((int(quem_del)) not in lst_ids_ativos):
        quem_del = raw_input('\nDigite o id do usuario que deseja apagar do sistema: ')
        
    for x in lst_dividas:
        if x[0]==(int(quem_del)):
            print('O usuario escolhido possui dividas com a empresa. Nao eh possivel apaga-lo\n')
            print('ID do usuario: ' + str(x[0]) + '\n' + 'Numero de chassi do modelo alugado: ' + str(x[1]) + '\n' + 'Data do aluguel (DDMMAAAA): ' + str(x[2]) + '\n' + 'Dias de aluguel: ' + str(x[5]) + '\n' + 'Valor do aluguel: R$ ' + str(x[3]) + '\n' + 'Multa (se existente): R$ ' + str(x[4]))
            return         
            
    print('Usuario encontrado. Nao possui dividas pendentes. Apagando ...\n')
    
    arq = open('historicotransacoes_dados.txt', 'r')
    linha = arq.readlines()
    aux = []
    aux2 = []
    for x in linha:
        aux.append(x)
        if len(aux)==6:
            aux2.append(aux)
            if int(quem_del)==int(aux[0]):
                aux2.remove(aux)
            aux = []
    arq.close()
    arq = open('historicotransacoes_dados.txt', 'w')
    for x in aux2:
        for y in x:
            arq.writelines((str(y)))
    arq.close()
    
    for z in lst_usuarios:
        for w in z:
            if int(w[0])==(int(quem_del)):
                lst_ids_ativos.remove(w[0])
                if w[7]=='gerente':
                    lst_gerentes.remove(w)
                elif w[7]=='cliente':
                    lst_clientes.remove(w)
                elif w[7]=='funcionario':
                    lst_funcionarios.remove(w)
    
    return                                  

def buscar_item():
    chassis_cadastrados()
    
    iden = '0'
    
    iden = raw_input('\nDigite o numero de chassi do modelo que deseja verificar:\n')
    
    for x in lst_estoque:
        for y in x:
            if iden==y[4]:
                print('Modelo encontrado, atualmente no estoque.\n')
                print('Nome: ' + x[0] + '\n' + 'ID do modelo: ' + x[1] + '\n' + 'Ano: ' + x[2] + '\n' + 'Placa: ' + x[3] + '\n' + 'Chaci: ' + x[4] + '\n' + 'Diaria: ' + str(x[5]) + '\n' + 'Multa: ' + str(x[6]) + '\n')
                return
    
    for x in lst_dividas:
        if x[1]==iden:
            print('Modelo encontrado, atualmente encontra-se alugado.\n')
            for y in lst_alugados: # alterar quando criar lista e funcao de aluugados
                if iden==y[4]:
                    print('Nome: ' + y[0] + '\n' + 'ID do modelo: ' + y[1] + '\n' + 'Ano: ' + y[2] + '\n' + 'Placa: ' + y[3] + '\n' + 'Chaci: ' + y[4] + '\n' + 'Diaria: ' + str(y[5]) + '\n' + 'Multa: ' + str(y[6]) + '\n')
                    print('ID de usuario que alugou: ' + str(x[0]) + '\n' + 'Data do aluguel | MMDDAAAA: ' + str(x[2]) + '\n' + 'Diaria de contrato: ' + str(x[3]) + '\n' + 'Dias de contrato: ' + str(x[5]) + '\nDivida em aberto (multa): ' + str(x[4]) + ' reais\n')
                    return
    
    print('Esse chassi nao existe no sistema.\n')
    
    return

def chassis_cadastrados():
    chassis_num = []
    
    for x in lst_estoque:
        for y in x:
            chassis_num.append(x[4])
            
    for x in lst_dividas:
        chassis_num.append(x[1])
    
    print('Numeros de chassis cadastrados no sistema: ')
    for x in chassis_num:
        print(x)
        
    return

def att_usuario(username):  
    print('Logins dos usuarios cadastrados no sistema: \n')
    dados_novos = []
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                perfil = y[7]
                exibe(perfil)
    
    quem_att = raw_input('\nDigite o id de quem deseja atualizar: ')
    
    if perfil=='funcionario':
        for x in lst_gerentes:
            if int(x[0])==int(quem_att):
                print('Esse perfil pertence a um gerente, voce nao tem acesso!\n')
                return
    
    if (int(quem_att)) not in lst_ids_ativos:
        print('Usuario nao disponivel\n')
        return   
    
    for x in lst_dividas:
        if x[0]==(int(quem_att)):
            print('O usuario possui dividas com a empresa; atualizacao de perfil indisponivel\n')
            return
    
    att_nome = raw_input('Nome: \n')
    dados_novos.append(att_nome)
    ok = 0
    while(ok==0):
        att_cpf = raw_input('CPF, 11 dig, sem tracos, espacos ou pontos: \n')
        ok = verif_cpf(att_cpf)
    dados_novos.append(att_cpf)
    att_datanasc = '98'
    ok = 0
    while ok!=1:
        att_datanasc = raw_input('Data de nascimento: \n')
        ok = verif_data(att_datanasc)
    dados_novos.append(att_datanasc)
    att_idade = gera_idade(att_datanasc)
    dados_novos.append(att_idade)
    ok = 0
    while ok==0:
        att_login = raw_input('Login: \n')
        ok = login_existe(att_login)
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

def verif_data(dados):
    try:
        int(dados)
    except ValueError:
        print('Voce usou caracteres nao-numericos, data invalida!\n')
        return 0
        
    if len(dados)!=8:
        print('Voce nao disponibilizou a data no formato de oito digitos inteiros sem espacos, data invalida.\n')
        return 0
    
    return 1
                     
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

def alterar_perfil(username):
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                exibe(y[7])
    quem_alterar = '0'
    tp_perfil = ('gerente', 'funcionario', 'cliente')
    novo_perfil = 'aleat'
    
    quem_alterar = raw_input('\nDigite o ID de quem deseja alterar o perfil: ')
        
    if (int(quem_alterar)) not in lst_ids_ativos:
        print('Usuario nao encontrado.\n')
        return
        
    for x in lst_dividas:
        if x[0]==(int(quem_alterar)):
            print('Usuario pendente na lista de dividas. Impossivel alterar perfil agora')
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
    novo_item = []
    chassi_car = 'ias2'
    
    while(idcarros not in tp_idcarros):
        idcarros = raw_input('Digite o ID que voce deseja cadastrar um novo item: [001]SUV [002] Sedan [003]Hatch\n ')
        
    nome_car = raw_input('Nome do modelo: ')
    novo_item.append(nome_car)
    novo_item.append(idcarros)
    ano_car = raw_input('Ano: ')
    novo_item.append(ano_car)
    placa_car = raw_input('Placa do carro: ')
    novo_item.append(placa_car)
    while(len(chassi_car)!=17):
        chassi_car = raw_input('Numero de chassi(17 digitos): ')
    novo_item.append(chassi_car)
    diaria_car = raw_input('Valor da diaria do carro: ')
    novo_item.append(int(diaria_car))
    multa_car = raw_input('Valor da multa diaria: ')
    novo_item.append(int(multa_car))
    
    if novo_item[1]=='001':
        lst_suv.append(novo_item)
    elif novo_item[1]=='002':
        lst_sedan.append(novo_item)
    elif novo_item[1]=='003':
        lst_hatch.append(novo_item)
    
    verificar_estoque()
    
    return

def deletar_item():
    verificar_estoque()
    
    chassi_car = raw_input('Digite o numero de chassi que deseja apagar: ')
    
    for x in lst_estoque:
        for y in x: 
            if y[4]==chassi_car:
                print('Nome: ' + y[0] + '\n' + 'ID do modelo: ' + y[1] + '\n' + 'Ano: ' + y[2] + '\n' + 'Placa: ' + y[3] + '\n' + 'Chaci: ' + y[4] + '\n' + 'Diaria: ' + str(y[5]) + '\n' + 'Multa: ' + str(y[6]) + '\n')
                conf = raw_input('Modelo encontrado, deseja realmente apaga-lo do estoque?y para continuar\n')
                if conf=='y':
                    print('Operacao cancelada.\n')
                    return
                delet = y
                if y[1]=='001':
                    lst_suv.remove(delet)
                elif y[1]=='002':
                    lst_sedan.remove(delet)
                elif y[1]=='003':
                    lst_hatch.remove(delet)
                verificar_estoque()
                return                                    
    
    return

def alugar_carro(username):
    print('ALUGUEL - para cada veiculo alugado, um novo processo de aluguel devera ser feito. Aluguel de no maximo 30 dias.\n')
    opcoes = []
    num_dias = '0'
    qual_alug = '0'
    divida = 0
    id_user = 0
    
    if (len(lst_suv) + len(lst_sedan) + len(lst_hatch)) == 0:
        print("Sem veiculos disponiveis em estoque.\n")
        return
    
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                id_user=y[0]
                
    for x in lst_dividas:
        if x[0]==id_user:
            if x[4]!=0:
                print('Voce esta com R$ %d de divida (multa) com a empresa; impossivel realizar novo aluguel\n')
                return
            
    print("ID's: 001 - SUV, 002-SEDAN, 003 - HATCH\n")        
    i = 1        
    for x in lst_estoque:
        for y in x:
            print('> OPCAO %d' %(i))
            print('Nome: ' + y[0] + '\n' + 'ID do modelo: ' + y[1] + '\n' + 'Ano: ' + y[2] + '\n' + 'Placa: ' + y[3] + '\n' + 'Chaci: ' + y[4] + '\n' + 'Diaria: ' + str(y[5]) + '\n' + 'Multa: ' + str(y[6]) + '\n')
            i = i+1
            opcoes.append(y)
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    
    tag = True
    
    while(tag):
        qual_alug = raw_input('Digite o inteiro correspondente a opcao do modelo que deseja alugar: ')
        if ((int(qual_alug))>0) and ((int(qual_alug)) <= len(opcoes)):
            tag = False
            
    i = (int(qual_alug))
    qual_alug = opcoes[i-1]
    
    tag = True
    while(tag):    
        num_dias = raw_input('Digite a quantidade de dias que deseja estar em posse do modelo | maximo 30: ')
        if (int(num_dias) > 0) and (int(num_dias)<31):
            tag = False
        
    divida = gera_divida(qual_alug,int(num_dias))
    
    new = []
    data = (str(datetime.now().day)) + ('0'+str(datetime.now().month)) + (str(datetime.now().year))
    
    new.append(id_user)
    new.append(qual_alug[4])
    new.append(int(data))
    new.append(divida)
    new.append(0)
    new.append(int(num_dias))
    
    print('Nome: ' + qual_alug[0] + '\n' + 'ID do modelo: ' + qual_alug[1] + '\n' + 'Ano: ' + qual_alug[2] + '\n' + 'Placa: ' + qual_alug[3] + '\n' + 'Chassi: ' + qual_alug[4] + '\n' + 'Diaria: ' + str(qual_alug[5]) + '\n' + 'Multa: ' + str(qual_alug[6]) + '\n')
    print('Dias: ' + str(new[5]) + '| ' + 'Diaria resultante: R$ ' + str(new[3]))
    conf = raw_input('CONFIRMACAO: Deseja realmente realizar esse aluguel?y para continuar\n')
    if conf=='n':
        print('Operacao cancelada.\n')
        return
    lst_alugados.append(qual_alug)
    armazena(new,5)
    
    if qual_alug in lst_suv:
        lst_suv.remove(qual_alug)
    elif qual_alug in lst_sedan:
        lst_sedan.remove(qual_alug)
        print('tirei')
    elif qual_alug in lst_hatch:
        lst_hatch.remove(qual_alug)
    
    arq = open('historicotransacoes_dados.txt', 'a')
    
    for x in new:
        arq.writelines((str(x))+'\n')
        
    arq.close()
    
    print('Aluguel finalizado.\n')
    
    return

def gera_divida(model,dias):
        
    valor = model[5]*dias
        
    return valor

def verifica_status(username):
    aux = []
    id_user = 0
    
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                id_user = y[0]
    
    for x in lst_dividas:
        if x[0]==id_user:
            aux.append(x)
            
    print('Suas dividas atuais com a empresa sao: \n')
    
    for x in aux:
        print('Chassi do modelo: ' + x[1] + '\n' + 'Data do aluguel (DDMMAAAA): ' + str(x[2]) + '\n' + 'Diaria de contrato: R$ ' + str(x[3]) + '\n' + 'Multa em aberto: R$ ' + str(x[4]) + '\n' + 'Dias validos do aluguel: ' + str(x[5]))
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        
    if len(aux)==0:
        print('Voce nao tem dividas ativas.\n')
    
    return

def limpar_perfispendentes():
    
    if len(lst_perfispendentes)==0:
        print('Nao ha perfis pendentes!\n')
        return
    
    print('LISTA DE PENDENTES:\n')
    
    for x in lst_perfispendentes:
        print('Nome: ' + str(x[1]) + '\nCPF: ' + str(x[2]))
        print('\n>>>PROXIMO:\n')
        
    op = raw_input('Deseja realmente apagar a lista?y para continuar: ')
    if op!='y':
        print('Operacao cancelada!\n')
        return
    
    for x in lst_perfispendentes:
        lst_perfispendentes.remove(x)
    
    print('Lista vazia!')
    
    return

def graficos():
    ano = raw_input('Digite o ano em que gostaria de observar as vendas: \n')
    
    arq = open('historicotransacoes_dados.txt','r')
    linha = arq.readlines()
    
    modelos = ['SUV','Sedan','Hatch']
    quant = [0,0,0]
    aux = []
    
    for x in linha:
        aux.append(x)
        if len(aux)==6:
            for y in lst_estoque:
                for z in y:
                    if (z[4]+'\n')==aux[1]: 
                        data = aux[2]
                        if (int(data[-5:]))==(int(ano)):
                            print('eae man kkk')
                            if int(z[1])==1:
                                quant[0] = quant[0]+1
                            elif int(z[1])==2:
                                quant[1] = quant[1] + 1
                            elif int(z[2])==3:
                                quant[2] = quant[2] + 1
                            aux = []            
    print quant
    arq.close()
    
    pp.bar(modelos, quant, color='red')
    pp.title('Numero de alugueis por modelo no ano %s' %(ano))
    pp.xlabel('Modelos')
    pp.ylabel('Quantidade de alugueis')

    pp.show()            
    
    faixa_etaria = ['18-25','26-35','36-45','46-55','55+']
    quant = []
    quant = [0,0,0,0,0]
    
    for x in lst_usuarios:
        for y in x:
            if y[4]>17 and y[4]<26:
                quant[0] = quant[0] + 1
            elif y[4]>25 and y[4]<36:
                quant[1] = quant[1]+1
            elif y[4]>35 and y[4]<46:
                quant[2] = quant[2]+1
            elif y[4]>45 and y[4]<56:
                quant[3] = quant[3]+1
            elif y[4]>55:
                quant[4] = quant[4]+1
                
    pp.bar(faixa_etaria, quant, color='blue')
    pp.title('Quantidade de usuarios cadastrados por faixa etaria')
    pp.xticks(faixa_etaria)
    pp.ylabel('Num de usuarios')
    pp.xlabel('Faixa etaria (anos)')
    
    pp.show()
    
    return

def login_existe(username):
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                print('Login ja existente. Tente outro!\n')
                return 0
    
    for x in lst_perfispendentes:
            if x[5]==username:
                print('Login ja existente. Tente outro!\n')
                return 0
    
    return 1

def ver_operacoes(username):
    for x in lst_usuarios:
        for y in x:
            if y[5]==username:
                exibe(y[7])
    
    id_user = raw_input('Digite o ID do usuario pelo qual deseja buscar operacoes: ')
    
    if (int(id_user)) not in lst_ids_ativos:
        print('O usuario nao esta ativo ou nao consta ou nunca realizou operacoes no sistema.')
        return

    arq = open('historicotransacoes_dados.txt', 'r')
    linha = arq.readlines()
    aux = []
    lst_historico = []
    
    for x in linha:
        aux.append(x)
        if len(aux)==6:
            if (int(aux[0]))==(int(id_user)):
                lst_historico.append(aux)
            aux = []
                
    print('Historico do usuario: ')
    
    for x in lst_historico:
        print('ID: ' +  str(x[0]))
        print('Modelo alugado: ' + str(x[1]))
        print('Data do aluguel: ' + str(x[2]))
        print('Valor pago: R$ ' + str(x[3]))
        print('Dias de aluguel: ' + str(x[5]))
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
          
    arq.close()    
        
    return
 
def fim_aluguel():
    i = 1
    
    if len(lst_dividas)==0:
        print('Nao ha dividas no sistema!\n')
        return

    print('Dividas ativas no sistema: ')
    for x in lst_dividas:
        print('=>DIVIDA %d' %(i))
        for y in lst_clientes:
            if y[0]==x[0]:
                print('Nome: ' + str(y[1]))
                print('CPF: ' + str(y[2]))
        print('ID do usuario: ' +  str(x[0]))
        print('Chassi do modelo alugado: ' + str(x[1]))
        for y in lst_alugados:
            if y[4]==x[1]:
                print('Modelo: ' + str(y[0]))
                print('Ano: ' + str(y[2]))
        print('Data do aluguel: ' + str(x[2]))
        print('Valor pago: R$ ' + str(x[3]))
        print('Valor pago adicionalmente(multa): R$ ' + str(x[4]))
        print('Dias de aluguel: ' + str(x[5]))
        i = i+1
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
      
    qual_div = raw_input('Qual divida deseja constar como paga? Digite o inteiro referente a ela: ')

    if (int(qual_div))>(len(lst_dividas)) or (int(qual_div))<1:
        print('Valor digitado nao aceito pelo sistema.')
        return

    conf = raw_input('Tem certeza? y para continuar\n')

    if conf!='y':
        print('Operacao cancelada.\n')
        return

    apag = lst_dividas[(int(qual_div))-1]
    
    for x in lst_alugados:
        if x[4]==apag[1]:
            if x[1]=='001':
                lst_suv.append(x)
            elif x[1]=='002':
                lst_sedan.append(x)
            elif x[1]=='003':
                lst_hatch.append(x)
            lst_alugados.remove(x)

    lst_dividas.remove(apag)

    print('Divida paga. Sistema atualizado!')
    
    return
 
def gera_multa():
    aux = 0
    aux2 = []
    d_aux1='k'
    d_aux2='k2'
    
    for x in lst_dividas:
        aux2 = x
        data = str(x[2])
        #print('data', data)
        aux = int(data[-4:])
        d_aux1 = str(aux)+'-'+str(data[-6:-4])+'-'+str(data[:-6])
        #print('daux_1', d_aux1)
        d_aux2 = str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)
        #print('daux_2', d_aux2)
        d1 = datetime.strptime(d_aux1, '%Y-%m-%d')
        d2 = datetime.strptime(d_aux2, '%Y-%m-%d')
        tempo_atraso = abs((d2 - d1).days)
        #print('tempoatraso', tempo_atraso)

        if tempo_atraso>x[5]:
            for y in lst_alugados:
                if y[4]==x[1]:
                    multa = 0
                    multa = tempo_atraso*y[6]
            aux2[4] = multa
            lst_dividas.remove(x)
            lst_dividas.append(aux2)
            
    return

def verif_cpf(dados):
    if len(dados)!=11:
        print('CPF no formato errado!\n')
        return 0
    
    try:
        int(dados)
    except ValueError:
        print('CPF invalido, fora do formato pedido.\n')
        return 0
    
    return 1 
          
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
        lst_clientes.append(info)
        print('\n', lst_clientes)
    elif x==5:
        lst_dividas.append(info)
    
    atualizar_banco()
        
    return

def gera_id_user():
    x = (len(lst_gerentes) + len(lst_funcionarios) + len(lst_clientes))*2
    while(1):
        id_user = rd.randint(2,x)
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

def exibe(perfil):
    dict_sistema = {}
    lst_exibe = []
    lst_infos_tab = ['ID', 'Nome', 'CPF', 'Data de nasc', 'Idade', 'Login', 'Senha', 'Perfil']
    tag = True
    k=0

    if perfil=='gerente':
        while(tag):
            for x in lst_usuarios:       
                for y in x:
                    lst_exibe.append(y[k])
                    #print lst_exibe
                
                    dict_sistema[lst_infos_tab[k]] = lst_exibe
                    #print lst_infos_tab[k]
    
            if k==len(lst_infos_tab)-1:
                tag = False
            k+=1
            lst_exibe = []
    elif perfil=='funcionario':
        while(tag):
            for x in lst_usuarios:
                for y in x:
                    if k!=6:
                        lst_exibe.append(y[k])
                        #print lst_exibe
                
                        dict_sistema[lst_infos_tab[k]] = lst_exibe
                        #print lst_infos_tab[k]
                    elif k==6:
                        lst_exibe.append('----')
                        dict_sistema[lst_infos_tab[k]] = lst_exibe
    
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
    
    # itens alugados
    
    arq = open('itensalugados_dados.txt', 'w')

    for x in lst_alugados:
        for y in x:
            arq.writelines((str(y))+'\n')    

    arq.close()
    
    # estoque
    
    arq = open('estoque_dados.txt', 'w')

    for x in lst_estoque:
        for y in x:
            for z in y:
                arq.writelines((str(z))+'\n')    

    arq.close()
    
    # perfis pendentes
    
    arq = open('perfispendentes_dados.txt', 'w')
    
    for x in lst_perfispendentes:
        for y in x:
            arq.writelines((str(y))+'\n') 
            
    arq.close()
    
    return

def log(username, str_acao):
    arq = open('log_localiza.txt', 'a')
    
    str_hora = 'Hora->' + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' + str(datetime.now().second)
    
    str_data = ' Data->' + str(datetime.now().day) + '/' + str(datetime.now().month) + '/' + str(datetime.now().year)   
    
    arq.writelines(str_hora +' | ' + str_data + ' | ' + ' | Usuario: ' + username + ' | Acao: ' + str_acao + '\n')
    
    arq.close()
    
    return
        
main()
