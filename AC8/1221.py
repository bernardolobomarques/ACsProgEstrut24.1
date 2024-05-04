import math
import time

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    N = int(input())  
    for _ in range(N):
        X = int(input())  
        start_time = time.time()  
        result = "Prime" if is_prime(X) else "Not Prime"  
        print(result)  
        elapsed_time = time.time() - start_time  
        if elapsed_time > 1:  
            print("Tempo de execução excedeu 1 segundo.")
            break

if __name__ == "__main__":
    main()
