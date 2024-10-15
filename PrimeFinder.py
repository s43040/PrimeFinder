array = [2]
num = 3
while num < 100:
    for prime in array:
        if num % prime == 0:
            break
        if num <= (prime * prime):
            array.append(num)
            print(num)
            break
    num+=2