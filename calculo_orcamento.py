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

escolha_do_usuario = input('(n)ovo gasto / (s)aldo ')
if escolha_do_usuario == 'n':
	valor_saldo_atual = saldo_atual()
	valor_do_debito = float(input('Qual o valor gasto: '))
	salvar_saldo(valor_saldo_atual, valor_do_debito)
	print('novo saldo %.2f' % saldo_atual())
elif escolha_do_usuario == 's':
	print('saldo atual: %.2f' % saldo_atual())
	print('seu ticket médio é: %.2f' % ticket_medio())
elif escolha_do_usuario == 'd':
	print('deposito')
else:
	print('sorry, try again: s, n ' )




# monthrange(2017, 5)[1] - datetime.now().day

# Open the file for reading
# read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
# write_file = open("text.txt", "w")
# Write to the file
# # write_file.write("Not closing files is VERY BAD.")

# # Try to read from the file
# print read_file.read()
# write_file.close()
# read_file.close()
