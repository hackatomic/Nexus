# -*- coding: utf-8 -*-
#-------------------------------------------------------------#
#Código para verificação da velocidade da comunicação serial  #  
#Autor: Rodrigo Trindade                                      #
#Data: 29/04/2015                                             #
#-------------------------------------------------------------#

import serial #Importa a biblioteca de comunicação seria
import time   #Importa a biblioteca de manipulação de tempo

#Função que define paramentros para a instancia ser.
#De forma resumida, configura a comunicação serial.
def init_serial():
    COMNUM = 1
    global ser #Cria uma variável globar para se usar fora da função
    ser = serial.Serial('/dev/ttyUSB0')  #Define a leitura na porta entre ''
    ser.baudrate = 9600   #Configura a comunicação pra 9600 bits/s
    port = '/dev/ttyUSB0'

    ser.timeout = 10

    #Verifica se a porta serial esta aberta
    if ser.isOpen():
        print 'Open: ' + port

#fim da função init_serial

init_serial() #Cria a instancia ser


time.sleep(1) #Espera um segundo

#Executa um loop infinito
while 1:
    leitura = ser.readline() #Ler o que esta sendo recebido pela porta serial

    t0 = time.time()    #Registra o tempo a partir do mo mento que se fez a leitura

    leitura = int(leitura)
    leitura = leitura**2+2
    leitura = str(leitura)
    ser.write(leitura)
    
    t = time.time() #Registra o tempo pós envio de dados
    
    print "Recebido: " + leitura
    print "Tempo: ", t-t0
    
