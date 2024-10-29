def compare_funcs(func1:str, func2:str):
    import timeit

    time1 = timeit.timeit(func1, setup=f"from __main__ import {func1}", number=1000)
    time2 = timeit.timeit(func2, setup=f"from __main__ import {func2}", number=1000)

    print(f"Time for {func1}: {time1:.6f} seconds")
    print(f"Time for {func2}: {time2:.6f} seconds")

    if time1 < time2:
        print(f"{func1} is faster")
    else:
        print(f"{func2} is faster")

