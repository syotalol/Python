def bank (size: int, years: int) -> int:
    for i in range(years):
        size = int(size*1.1)
    print ("Сумма вашего счёта составит: {0} рублей.".format(size))
    return size, years
    
if __name__ == "__main__":
    bank (20000, 3)
