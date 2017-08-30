import sys
from calendar import monthrange
from datetime import datetime

def saldo_para_gastar(saldo_anterior, valor_debitado):
	dias_restantes = monthrange(datetime.now().year, datetime.now().month)[1] - datetime.now().day
	saldo_novo = saldo_anterior - valor_debitado
	quanto_ainda_posso_gastar = saldo_novo / dias_restantes
	return quanto_ainda_posso_gastar

def ticket_medio():
	dias_restantes = monthrange(datetime.now().year, datetime.now().month)[1] - datetime.now().day
	quanto_ainda_posso_gastar = saldo_atual() / dias_restantes
	return quanto_ainda_posso_gastar	

def saldo_atual():
	leitura_arquivo_saldo_atual = open("saldo_atual.txt", "r")
	saldo_atual = float(leitura_arquivo_saldo_atual.read().replace(',', '.'))
	leitura_arquivo_saldo_atual.close()
	return saldo_atual

def salvar_saldo(saldo_atual, valor):	
	calculo = saldo_para_gastar(saldo_atual, valor)
	escrita_arquivo_novo_saldo = open("saldo_atual.txt", "w")
	escrita_arquivo_novo_saldo.write(str(calculo))
	escrita_arquivo_novo_saldo.close()

def novo_deposito(deposito):
	novo_saldo = saldo_atual() + deposito
	escrita_arquivo_novo_saldo = open("saldo_atual.txt", "w")
	escrita_arquivo_novo_saldo.write(str(novo_saldo))
	escrita_arquivo_novo_saldo.close()

escolha_do_usuario = input('(n)ovo gasto / (s)aldo / (d)eposito ')
if escolha_do_usuario == 'n':
	valor_saldo_atual = saldo_atual()
	valor_do_debito = float(input('Qual o valor gasto? '))
	salvar_saldo(valor_saldo_atual, valor_do_debito)
	print('Novo saldo %.2f' % saldo_atual())
elif escolha_do_usuario == 's':
	print('Saldo atual: %.2f' % saldo_atual())
	print('Seu ticket médio é: %.2f' % ticket_medio())
elif escolha_do_usuario == 'd':
	depositado = float(input('Qual o valor depositado? '))
	novo_deposito(depositado)
	print('Seu novo saldo é: %.2f' % saldo_atual())
	print('Seu ticket médio agora é: %.2f' % ticket_medio())
else:
	print('sorry, try again: s, n ou d')
