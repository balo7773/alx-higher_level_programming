#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    n_list = []
    while index < list_length:
        result = 0
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(result)
            index += 1
    return n_list
