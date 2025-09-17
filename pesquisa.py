totalSim = 0
totalNao = 0
mulheresSim = 0
homensNao =  0
totalMulheres = 0
totalHomens = 0
for i in range(5):
    sexo = input('digite o sexo (H/M): ')
    resposta = input('digite a resposta (S/N): ')
    if resposta == 'S':
        totalSim += 1
        if sexo == 'M':
            mulheresSim += 1
    else:
        totalNao += 1
        if sexo == 'H':
            homensNao += 1
    if sexo == 'M':
        totalMulheres += 1
    else:
        totalHomens +=1
if totalMulheres > 0:
    porcMulheresSim = (mulheresSim / totalMulheres)*100
else:
    porcMulheresSim = 0

if totalHomens >0:
    porcHomensNao = (homensNao/totalHomens)*100
else:
    porcHomensNao = 0

print(f'Numero de pessoas que responderam Sim: {totalSim}')
print(f'numero de pessoas que responderam Nao: {totalNao}')
print(f'porcentagem de mulheres que responderam Sim: {porcMulheresSim:.2f}%')
print(f'porcentagem de Homens que responderam Nao: {porcHomensNao:.2f}%')

     
