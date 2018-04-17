import os
import sys


def check_dir(path='.'):
    res = [] #инициализация возвращаемого списка пар чисел и строк
    try:
        os.scandir(path)
    except OSError:
        print("Cannot open a directory", path, file=sys.stderr)
    else:
        for entry in os.scandir(path): #обход всех файлов и папок в данном каталоге
            if entry.is_dir():
                res.extend(check_dir(entry.path)) #запись в список результата рекурсивного вызова  
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
                            res.append([num, line]) #добавление пары из числа и строки из файла в возвращаемый список
    return res


def main():
    ans = check_dir()
    ans.sort()
    for i in ans:
        print(i[1])


if __name__ == "__main__":
    main()
