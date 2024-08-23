def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        flag = True
        for i in range(2, result):
            if result%i == 0:
                flag = False
        if flag:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)
    

result = sum_three(2, 3, 6)
print(result)