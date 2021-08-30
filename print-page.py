def indexes(num: list) -> tuple:
    if len(num) == 3: print(f"range: {num[0]} - {num[1]} | {num[2]} Pages per sheet")
    else:  input("Please specify the number of pages per sheet\npress ENTER to exit")
    r = list(i for i in range(num[0], num[1] + 1))
    tup = list(zip(*[iter(r)]*num[2]))
    return (list(v for i, v in enumerate(tup) if i % 2 == 0), list(v for i, v in enumerate(tup) if not i % 2 == 0))
if __name__ == "__main__":
    final_tup = indexes(list(int(i) for i in input().split()))
    print("Print this first: " + ", ".join([str(", ".join(list(str(a) for a in i))) for i in final_tup[0]]) + "\n" + "Print this later: " + ", ".join([str(", ".join(list(str(a) for a in i))) for i in reversed(final_tup[1])]))
    input('Press ENTER to exit')
