def is_even(num):
    if num % 2 == 0:
        return True

    else:
        return False

print(is_even(2))

def calc_total(list):
    sum = sum(list)
    for num in list:
        sum += num
    return sum
