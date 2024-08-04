from module5_mod import NumberProcessor

np = NumberProcessor()

n = int(input("Enter a positive integer N: "))
np.get_data(n)

x = int(input("Enter an integer X: "))
result = np.find_num(x)

print(result)