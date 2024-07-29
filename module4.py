

def main():
    N = int(input("Enter a positive integer N: "))
    
    numbers = []
    for i in range(N):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    
    X = int(input("Enter an integer X: "))
    
    if X in numbers:
        print(numbers.index(X) + 1)
    else:
        print("-1")

if __name__ == "__main__":
    main()
