# test file for ajgar-transpiler (processed output)
print("Namaste")

naam = input("Aapka naam kya hai? ")

one = int("1")
pi = float(22 / 7)
print(one, pi)

if naam == "Aarsh":
    print("Namaste, Aarsh - Creator of Ajgar")
elif naam == "Mukhi":
    print("Mukhi i didnt know you can run Python?")
else:
    print("Namaste", naam)

for i in range(1, 100):
    print(i)

loop = True
while loop:
    print("loop")
    loop = False

def addition(a: int, b: int): return a + b
print(addition(1, 20))

input("Aage badhne ke liye enter dabaye ")
