import timeit


res_1: float = timeit.timeit('"".join(str(n) for n in range(100))', number=10000)
print(res_1)


res_2: float = timeit.timeit('"".join(map(str, [i for i in range(100)]))', number=10000)
print(res_2)

res_3: float = timeit.timeit('"".join([str(i)for i in range(100)] * 10000)', number=1)
print(res_3)