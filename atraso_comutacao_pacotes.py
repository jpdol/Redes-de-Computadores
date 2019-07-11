from random import randint

pacotes = []
fila = []
tam_fila = 20
velocidade = 1
num_pacotes = 100

def criar_pacotes(): #Pacote == (tamanho do pacote, tempo de processamento)
	pacote = dict()
	pacote['tam'] = randint(1,20)
	pacote['proc'] = randint(1,5)
	pacote['delta_proc'] = pacote['proc']
	pacote['atraso'] = 0
	return pacote

def armazena(pacote):
	atraso = atraso_fila()
	fila.append(pacote)
	pacote['atraso'] += pacote['tam']/velocidade
	pacote['atraso_armazenagem'] = pacote['tam']/velocidade
	pacote['atraso_fila']=atraso

def processa(pacote):
	pacote['delta_proc']-=1
	pacote['atraso']+=1
	try:
		pacote['atraso_proc']+=1
	except:
		pacote['atraso_proc']=1

def reenvia(pacote):
	pacote['atraso'] += pacote['tam']/velocidade
	pacote['atraso_reenvio'] = pacote['tam']/velocidade

def atraso_fila():
	atraso=0
	for i in fila:
		atraso+=i['proc']+i['tam']/velocidade
	return atraso

pacotes = []
for i in range(num_pacotes): # cria lista de pacotes a serem comutados
	pacotes.append(criar_pacotes())

i=1
while(len(pacotes)>0 or len(fila)>0):
	if len(pacotes)>0 and len(fila)<tam_fila:
		armazena(pacotes.pop())

	processa(fila[0])
	if fila[0]['delta_proc']<=0:
		reenvia(fila[0])
		del(fila[0]['delta_proc'])
		print()
		print(fila.pop(0))
		i+=1
