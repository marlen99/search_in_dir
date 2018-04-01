import os, random, sys
word_1 = ["Awesome", "Unknown", "Some", "Hello,"] #список первых слов для генерации строк
word_2 = ["text.", "world!", "person", "test?"] #список вторых слов для генерации строк
def mk_cycl_dir(path, depth):
    """
    рекурсивная функция, создающая вложенные
    папки с файлами в данной директории
    """
    os.chdir(path)
    if depth != 0:
        for i in range(1, random.randint(0, width)+1): #создание случайного числа(от 1 до width) папок в данной директории
            os.mkdir("test_" + str(i))
            mk_cycl_dir("test_" + str(i), depth - 1) #рекурсивный вызов функции для созданной папки с глубиной вложенности, меньшей на 1
            os.chdir("..")
    for i in range(1, random.randint(0, width)+1):
        try:
            f = open("test_" + str(i) + ".txt", "w") #проверка возможности создания файла
        except OSError:
            print("Cannot create a file", file=sys.stderr)
        else:
            print(random.randint(1, 10000), word_1[random.randint(0, 3)], word_2[random.randint(0, 3)], file=f) #запись случайной строки в файл    
print("Enter creating catalog's name:", end=" ")
catalog = input()
try:
    os.mkdir(catalog)
except OSError:
    print("Can't create directory \""+catalog+"\"", file=sys.stderr)
else:
    print("Enter depth of nesting:", end=" ")
    try:
        depth = int(input()) #считывание глубины вложенности папок
    except ValueError:
        print("Incorrect input", file=sys.stderr)
    else:
        print("Enter max number of files and directories in one directory:", end=" ")
        try:
            width = int(input()) #считывание максимального числа файлов и папок в одной директории 
        except ValueError:
            print("Incorrect input", file=sys.stderr)
        else:
            mk_cycl_dir(catalog, depth)
