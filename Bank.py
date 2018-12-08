def bank (a, years):
    a = int(input("Введите размер вклада:"))
    years = int(input("Введите срок:"))
    for i in years:
        a = a*1.1
    print ("Сумма вашего счёта составит: ", a, " рублей.")
    return(a)

bank(a, years)
