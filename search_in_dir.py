import os, sys
def check_dir(path='.'):
    """
    рекурсивная функция поиска вглубину в каталоге path,
    возвращающая список из пар чисел и строк из всех первых строк из .txt файлов
    """
    res = [] #инициализация возвращаемого списка пар чисел и строк
    try:
        os.scandir(path)
    except OSError:
        print("Cannot open a directory", path, file=sys.stderr)
    else:
        for entry in os.scandir(path): #обход всех файлов и папок в данном каталоге
            if entry.is_dir():
                res += check_dir(entry.path) #запись в список результата рекурсивного вызова  
            else:
                if entry.name.endswith(".txt"):
                    try:
                        file = open(entry.path) #проверка на возможность открытия файла
                    except OSError:
                        print("Cannot open a file", entry.path, file=sys.stderr) #вывод ошибки на экран
                    else:
                        line = file.readline().strip() #чтение первой строки файла
                        if line.split()[0].isdigit(): 
                            num = int(line.split()[0]) 
                            i = 0
                            res += [[num, line]] #добавление пары из числа и строки из файла в возвращаемый список
    return res
l = check_dir()
l.sort()
for i in l:
   print(i[1])
