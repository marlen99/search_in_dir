###### Версия Python - 3.5
# Запуск скриптов
  Для запуска скрипта search_in_dir требуется в командной строке ввести команду:
  ```
  python3 <путь_к_скрипту> <путь_к_папке_в_которой_будет_осуществлен_поиск>         (Linux)
  <путь_к_скрипту> <путь_к_папке_в_которой_будет_осуществлен_поиск>                 (Windows)
  ```
  Для запуска скрипта create_testing_catalog соответственно:
  ```
  python3 <путь_к_скрипту> <путь_к_создаваемой_директории> [--width <число_папок_и_файлов_в_одной_директории>] [--depth <глубина_вложенности>]         (Linux)
  <путь_к_скрипту> <путь_к_создаваемой_директории> [--width <число_папок_и_файлов_в_одной_директории>] [--depth <глубина_вложенности>]                 (Windows)
  ```
# Скрипт search_in_dir
  Ищет текстовые файлы в заданной директории и во всех подпапках, в том числе и вложенных. В результате выводит все первые строки этих файлов в порядке возрастания первого числа каждой строки.
  
### Пример
  Есть папка root, которая хранит директории и файлы:
  ```
  root/file.txt: 5 Is it test?
  root/folder_1/file.txt: 7 All right
  root/folder_2/file.txt: 9 Good job!
  root/folder_2/file1.txt: 2 Hi, stranger
  root/folder_2/folder/file.txt: 4 Hello, world!
  ```
  Будучи запущенной в директории root, скрипт выведет:
  ```
  2 Hi, stranger
  4 Hello, world!
  5 Is it test?
  7 All right
  9 Good job!
  ```
# Скрипт create_testing_catalog
  Получает на вход путь к создаваемой директории, глубину вложенности папок(**depth**) и число файлов и папок в одной директории(**width**). В результате создает каталог с папками с максимальной глубиной вложенности, введенной пользователем(**depth**), и текстовыми файлами, содержащими одну строку. Количество файлов и папок в одной директории не превышает введенного числа(**width**).
  
  Названия папок и файлов имеют вид:
  ```
  test_<номер_файла_или_папки_в_директории>
  ```
  Строки в файлах имеют вид:
  ```
  <число><пробел><случайное_первое_слово><пробел><случайное_второе_слово>
  ```
### Пример
  Запустим скрипт:
  ```
  python3 create_testing_catalog.py catalog --width 2 --depth 2
  ```
  В результате получим:
  ```
  catalog/test_1.txt: 2417 Unknown person
  catalog/test_1/test_1.txt: 6378 Some person
  catalog/test_1/test_1/test_1.txt: 547 Some text.
  catalog/test_2/test_1/test_1.txt: 9908 Awesome world!
  catalog/test_2/test_1/test_2.txt: 4326 Unknown test?
  ```
