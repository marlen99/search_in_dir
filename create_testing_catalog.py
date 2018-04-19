import os
import random
import sys
import argparse
WORD_1 = ["Awesome", "Unknown", "Some", "Hello,"] #список первых слов для генерации строк
WORD_2 = ["text.", "world!", "person", "test?"] #список вторых слов для генерации строк
NAME = "test_{}{}"


def mk_cycl_dir(path, depth, width):
    os.chdir(path)
    if depth != 0:
        for i in range(1, random.randint(0, width)+1): #создание случайного числа(от 1 до width) папок в данной директории
            os.mkdir(NAME.format(str(i), ''))
            mk_cycl_dir(NAME.format(str(i), ''), depth - 1, width) #рекурсивный вызов функции для созданной папки с глубиной вложенности, меньшей на 1
            os.chdir("..")
    for i in range(1, random.randint(0, width)+1):
        try:
            f = open(NAME.format(str(i), '.txt'), "w") #проверка возможности создания файла
        except OSError:
            print("Cannot create a file", file=sys.stderr)
        else:
            print(random.randint(1, 10000), WORD_1[random.randint(0, 3)], WORD_2[random.randint(0, 3)], file=f) #запись случайной строки в файл
            f.close()


def main():
    parser = argparse.ArgumentParser(prog='create_testing_catalog')
    parser.add_argument('path', help='путь к создаваемой директории')
    parser.add_argument('--depth', nargs='?', default=5, type=int, help='глубина вложенности папок')
    parser.add_argument('--width', nargs='?', default=5, type=int, help='максимальное число папок и файлов в одной директории')
    args = parser.parse_args()
    os.mkdir(args.path)
    mk_cycl_dir(args.path, args.depth, args.width)


if __name__ == "__main__":
    main()
