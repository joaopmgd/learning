import time

def fib_iterative(pos):
    fibonacci = [0, 1]
    i = len(fibonacci)
    while len(fibonacci) <= pos:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        i += 1
    return fibonacci[pos]


def fib_recursive(pos):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fib_recursive(pos -1) + fib_recursive(pos - 2)


if __name__ == '__main__':
    start_time = time.time()
    print(fib_recursive(35))
    print("--- Fibonacci Recursive Took %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(fib_iterative(35))
    print("--- Fibonacci Iterative Took %s seconds ---" % (time.time() - start_time))