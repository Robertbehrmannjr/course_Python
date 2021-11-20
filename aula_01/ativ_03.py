def calc_velocidade_media(distancia,tempo, medida = None):
    if (medida != None):
        if (medida.lower() == 'm/s'):
            return (distancia/tempo) * 3.6
    return distancia/tempo

# programa executando a função
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

d = float(input('Informe a distância percorrida em quilômetros:'))
t = int(input('informe o tempo percorrido em horas:'))
m = input('Informe a unidade de medida (Km/h ou m/s):')
# chamando a função
r = calc_velocidade_media(d,t,m)
print('\nA velocidade média foi de {:.2f}'.format(r))

print('\n----- FIM DA EXECUÇÃO: -----\n')
