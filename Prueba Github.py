def menorC_aux(num, result):
    if num == 0:
        return result
    elif num % 10 < result:
        return menorC_aux(num // 10, num % 10)
    else:
        return menorC_aux(num // 10, result)