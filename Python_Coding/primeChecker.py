def isPrime(num):
    prime_list = [2, 3]
    for i in range(4, num + 1):
        is_prime = True
        for j in prime_list:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    return num in prime_list
             
num = 2169

isPrime(num)