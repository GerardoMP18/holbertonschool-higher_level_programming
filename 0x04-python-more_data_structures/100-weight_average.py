def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        summ = 0
        divv = 0
        for i in my_list:
            summ += i[0] * i[1]
            divv += i[-1]
        return summ/divv
