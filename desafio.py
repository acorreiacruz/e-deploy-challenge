def maior_lucro(lista):
    '''
        A função irá percorrer cada um dos valores, e irá calcular a diferença entre o valor do dia seguinte em relação ao atual, caso o valor seguinte seja maior do que o atual, logo após isso o valor da diferença será aramzeanda na lista. No final a lista será ordenada de form crescente, caso a lista seja vazia é retornado 0, caso contrário será retornado o último valor dela, o maior.
        dif_precos: lista que irá armazenar as diferenças de preços.

    '''
    dif_precos = []
    tamanho = len(lista)
    for i in range(tamanho - 1):
        for j in range(i + 1, tamanho):
            if lista[i] < lista[j]:
                dif_precos.append(lista[j] - lista[i])
    dif_precos.sort()
    return dif_precos[-1] if dif_precos else 0