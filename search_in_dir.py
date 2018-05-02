import os
import sys
import argparse


def check_dir(path):
    res = [] #инициализация возвращаемого списка строк
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
                        line = file.readline() #чтение первой строки файла
                        try:
                            int(line.split()[0])
                        except TypeError:
                            file.close()
                            continue
                        else:
                            res.append(line) #добавление строки из файла в возвращаемый список
                            file.close()
    return res


def sort_by_num(string):
    return int(string.split()[0])


def main():
    parser = argparse.ArgumentParser(prog='search_in_dir')
    parser.add_argument('path', help='путь к директории, в которой будет производиться поиск')
    args = parser.parse_args()
    ans = check_dir(args.path)
    ans.sort(key=sort_by_num)
    for string in ans:
        print(string)


if __name__ == "__main__":
    main()
