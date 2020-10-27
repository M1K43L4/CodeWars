def divisors(integer):
    if integer <= 1:
        print("can only check for greater than 1")
        return -1
    my_list = list(x for x in range(integer) if x > 1 and integer % x == 0)

    if len(my_list) == 0:
        return str(integer) + ' is prime'
    return my_list


if __name__ == '__main__':
    print(divisors(13))
