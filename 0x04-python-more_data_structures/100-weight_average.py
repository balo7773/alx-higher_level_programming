def weight_average(my_list=[]):
    """
        calculate the weighted average of all integers tuple
        (<score>, <weight>)

    Args:
        my_list: list containing all the tuples

    Return:
        The weighted average = \
        (score1 * weight1) + ... + (scoreN * weightN)/weight1 + ... + weightN
    """
    if my_list == []:
        return 0
    mult = 0 
    weight = 0
    for x in my_list:
        mult += (x[0] * x[1])
        weight += x[1]
    return mult / weight