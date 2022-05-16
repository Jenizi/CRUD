def validateCPF(CPF):

    def validateDigit(cpf, start, finish, multiplier):
        summ = 0

        for n in cpf[start:finish]:
            summ += int(n) * multiplier
            multiplier -= 1

        summ = (summ * 10) % 11

        summ = 0 if summ > 9 else summ

        return str(summ)
    if len(CPF) != 11:
        return False
    try:
        d1 = validateDigit(CPF, 0, 9, 10)
        d2 = validateDigit(CPF, 0, 10, 11)
    except Exception:
        return False
    return d1 == CPF[9] and d2 == CPF[10]
