from module5_mod import NumberHandler

if __name__ == "__main__":
    handler = NumberHandler()
    
    n = int(input("Enter how many numbers to input (N): "))
    handler.get_numbers(n)
    
    x = int(input("Enter the number to find (X): "))
    result = handler.find_num(x)
    
    print(result)