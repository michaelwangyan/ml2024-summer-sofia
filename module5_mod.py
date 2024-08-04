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