senhaCorreta = 1234
tentativas = 3
for i in range(3):
    print(f'digite a senha({tentativas - i} tentativas restantes: ', end='')
    senhaDigitada = float(input('digite a senha: '))
    if senhaDigitada == senhaCorreta:
      print('acesso permitido.')
      break
    elif i == tentativas - 1:
        print('numero de tentativas esgotadas')
        break
    else: print ('acesso negado')
    