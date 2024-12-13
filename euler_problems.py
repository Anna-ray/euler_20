def problem1():
    user_input = int(input("Enter a number: "))
    total = sum(x for x in range(user_input) if x % 3 == 0 or x % 5 == 0)
    print(total)

def problem2():
    user_input = int(input("Enter the maximum value: "))
    a, b = 1, 2
    total = 0
    while b <= user_input:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    print(total)

def problem3():
    user_input = int(input("Enter a number: "))
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = max(i for i in range(2, user_input + 1) if user_input % i == 0 and is_prime(i))
    print(largest_prime)

def problem4():
    n = int(input("Enter the number of digits "))
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    largest_palindrome = max(i * j 
                             for i in range(10**(n-1), 10**n) 
                             for j in range(10**(n-1), 10**n) 
                             if is_palindrome(i * j))
    print(largest_palindrome)

def problem5():
    import math
    user_input = int(input("Enter a number: "))
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    multiple = 1
    for i in range(1, user_input + 1):
        multiple = lcm(multiple, i)
    print(multiple)

def main():
    print("Choose a problem to solve:")
    print("1. Multiples of 3 and 5")
    print("2. Even Fibonacci Numbers")
    print("3. Largest Prime Factor")
    print("4. Largest Palindrome Product")
    print("5. Smallest Multiple")
    
    choice = int(input("Enter the problem number (1, 2, 3, 4, 5): "))

    if choice == 1:
        problem1()
    elif choice == 2:
        problem2()
    elif choice == 3:
        problem3()
    elif choice == 4:
        problem4()
    elif choice == 5:
        problem5()
    else:
        print("Invalid choice. Please enter a number from the list.")

if __name__ == "__main__":
    main()
