from itertools import*
def Tester():
    k = 0
    for i in range(0, 7):
        path1 = "test." + str(i) + ".in"
        path2 = "test." + str(i) + ".out"
        file_in = open(path1, "r")
        file_out = open(path2, "r")
        solve=Solve(int(file_in.readline()))
        print("для теста ", path1, "ответ", solve, "правильный ответ", int(file_out.readline()))

def Solve(n):
    if n == 1:
        return 10
    summa_number = [0]*100
    for number in [t for t in product("0123456789", repeat=n)]:
        summa = sum([int(t) for t in number])
        summa_number[summa] += 1
    return sum([t**2 for t in summa_number])

Tester()







