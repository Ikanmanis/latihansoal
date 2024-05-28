
# #no 1
# x = 3
# y = 2
# total = x + y
# print(total)

# #no 2
# x = 2
# y = 1
# x,y = y,x
# print("\nnilai x = " + str(x))
# print("nilai y = " + str(y))

# #no 3
# int = 1
# float = 0.1
# str = 'string'
# boolean = True
# print(f"tipe datanya adalah = {type(int)}")
# print(f"tipe datanya adalah = {type(float)}")
# print(f"tipe datanya adalah = {type(str)}")
# print(f"tipe datanya adalah = {type(boolean)}")

# #no 4 
# name = "raya"
# print(f"length = {len(name)}")
# print(f"uppercase = {name.upper()}")


def count_sheep(i):
    res = ""
    while i < 5+1:
        res += f"{i} sheep..."
        i += 1
    print(res)

i = 1
run = count_sheep(i)