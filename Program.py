def GetOnlyMaxThreeSymbols(arr):
    cnt = len(arr)
    arr_pos = [0 for e in range(cnt)]
    arr_new = []
    pos = -1
    el_cnt = 4
    for i in range(cnt):
        el_cnt = len(arr[i])
        if el_cnt <= 3:
            pos += 1
            arr_pos[pos] = i

    if pos == -1:
        print("Нет строк менее или равных 3")
    else:
        pos += 1
        print(f"Создан массив размером {pos}")
        arr_new = [0 for e in range(pos)]
        for pos_new in range(pos):
            arr_new[pos_new] = arr[arr_pos[pos_new]]
    return arr_new

def Input():
    arr = []
    while True:
        val = input("Введите значение или !q для выхода:")
        if val == '!q':
            break
        arr.append(val)
    return arr

def PrettyPrint(arr):
    print("[" + ', '.join(arr) + "]")

if __name__ == '__main__':
    PrettyPrint(GetOnlyMaxThreeSymbols(["hello", "2", "world", ":-)"]))
    PrettyPrint(GetOnlyMaxThreeSymbols(["1234", "1567", "-2", "computer science"]))
    PrettyPrint(GetOnlyMaxThreeSymbols(["Russia", "Denmark", "Kazan"]))
    PrettyPrint(GetOnlyMaxThreeSymbols(Input()))

