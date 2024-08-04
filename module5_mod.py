class NumberProcessor:
    def __init__(self):
        self.nums = []

    def get_data(self, n):
        for i in range(n):
            num = int(input("Enter number: "))
            self.nums.append(num)

    def find_num(self, x):
        if x in self.nums:
            return self.nums.index(x) + 1
        else:
            return -1
