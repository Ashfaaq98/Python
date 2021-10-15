def collatz(number):

    if number % 2 == 0:
        e = number // 2
        print(e)
        return e

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    print("Give me a number: ")
    n = int(input())
    while n != 1:
        n = collatz(n)
except ValueError:
    print('Value Error. Please enter integer')