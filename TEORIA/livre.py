numero = 22

centenas_str = dezenas_str = unidades_str = ''
partes_numericas = 0

centenas_int = numero // 100
if centenas_int == 1:
    centenas_str = ('1 Centena')
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = (f'{centenas_int} Centenas')
    partes_numericas += 1

dezenas_int = (numero % 100) // 10
if dezenas_int == 1:
    dezenas_str = ('1 Dezena')
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = (f'{dezenas_int} Dezenas')
    partes_numericas += 1

unidades_int = ((numero % 100) % 10)
if unidades_int == 1:
    unidades_str = ('1 Unidade')
    partes_numericas += 1
elif unidades_int > 1:
    unidades_str = (f'{unidades_int} Unidades')
    partes_numericas += 1


if partes_numericas == 0:
    print('Não possui centenas, dezenas ou unidades.')
elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidades_str)
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidades_str
        print(f'{centenas_str} e {segunda_parte}')
    else:
        print(f'{dezenas_str} e {unidades_str}')
