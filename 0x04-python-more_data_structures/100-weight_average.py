#/usr/bin/python3
def weight_average(my_list=[]):

    if my_list == []:
        return 0
    mult = 0 
    weight = 0
    for x in my_list:
        mult += (x[0] * x[1])
        weight += x[1]
    return mult / weight