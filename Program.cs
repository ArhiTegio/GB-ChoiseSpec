void Main(){
    GetOnlyMaxThreeSymbols(new string[]{"hello", "2", "world", ":-)"});
    GetOnlyMaxThreeSymbols(new string[]{"1234", "1567", "-2", "computer science"});
    GetOnlyMaxThreeSymbols(new string[]{"Russia", "Denmark", "Kazan"});
}

string[] GetOnlyMaxThreeSymbols(string[] arr)
{
    var cnt = arr.Length;
    var arr_pos = new int[cnt];
    var arr_new = new string[0];
    var pos = -1;
    var el_cnt = 4;
    for(var i = 0; i < cnt; ++i)
    {
        el_cnt = arr[i].Length;
        if(el_cnt <= 3){
            ++pos;
            arr_pos[pos] = i;
        }
    }

    if(pos == -1){
        Console.WriteLine("Нет строк менее или равных 3");
    }
    else{   
        Console.WriteLine($"Создан массив размером {pos}");
        ++pos;
        arr_new = new string[pos];
        for(var pos_new = 0; pos_new < pos; ++pos_new)
        {
            arr_new[pos_new] = arr[arr_pos[pos_new]];
        }
    }
    return arr_new;
}


Main();