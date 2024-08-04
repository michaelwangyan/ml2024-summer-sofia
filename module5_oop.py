

class NumberHandler:
    def __init__(self):
        self.nums = []

    def get_numbers(self, n):
        for _ in range(n):
            num = int(input("Enter a number: "))
            self.nums.append(num)

    def find_num(self, x):
        if x in self.nums:
            return self.nums.index(x) + 1
        else:
            return -1

if __name__ == "__main__":
    handler = NumberHandler()
    
    n = int(input("Enter how many numbers to input (N): "))
    handler.get_numbers(n)
    
    x = int(input("Enter the number to find (X): "))
    result = handler.find_num(x)
    
    print(result)
