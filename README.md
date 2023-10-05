# Лабораторная 1 по дисциплине "Технологии программирования"

___Цель___  
Поработать с системой контроля Git и инструментом CI/CD GitHub Actions

___Описание проекта___  
В лабораторной работе используется проект, рассчитывающий средний рейтинг студентов по дисциплинам. Список студентов и полученных ими оценок приводится в текстовом файле. Проект написан на языке программирования Python 3, модульное тестирование в нем осуществляется с помощью библиотеки pytest

___Индивидуальное задание №3___  
Формат входного файла: XML  
Расчетная процедура: Определить и вывести на экран студента, имеющего 100 баллов по всем дисциплинам. Если таких студентов несколько, нужно вывести любого из них. Если таких студентов нет, необходимо вывести сообщение об их отсутствии.

### Используемые консольные команды
___Для установки библиотек___  
```
pip install -r requirements.txt 
```

___Для запуска с файлом data.txt___  
``` 
python3.10 src/main.py -p ./data/data.txt  
```

___Для запуска с файлом data.xml___  
``` 
python3.10 src/main.py -p ./data/data.xml  
```

# Ход работы
### Задание 1
Файл лицензии был создан по шаблону и находится в корневом разделе проекта под названием "LICENSE"
MIT License

Copyright (c) 2023 TDitS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Задание 2
Файл .gitignore находится в корневом разделе проекта, он включает в себя:
- Файлы операционной системы
- Файлы конфигурации, создаваемые такими приложениями, как редакторы кода и IDE
- Файлы, которые автоматически генерируются языком программирования или средой разработки
- Папки, созданные диспетчерами пакетов
- Файлы, которые содержат конфиденциальные данные и личную информацию
- Файлы среды выполнения

### Задание 3
### Создадим файл формата xml, класс xmlDataReader как наследник класса DataReader, тест этого класса и исправим файл main для работы с новым класом. Для этого откроем ветку xml проекта, а именно "xml".

#### data.xml:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<students>
    <student class="Иванов Иван">
        <математика>67</математика>
        <литература>100</литература>
        <программирование>91</программирование>
    </student>
    <student class="Петров Петр">
        <математика>78</математика>
        <химия>87</химия>
        <социология>61</социология>
    </student>
    <student class="Андреев Андрей">
        <математика>100</математика>
        <химия>89</химия>
        <социология>100</социология>
    </student>
    <student class="Артемов Артем">
        <математика>76</математика>
        <химия>100</химия>
        <социология>68</социология>
    </student>
    <student class="Данилов Данил">
        <математика>100</математика>
        <химия>100</химия>
        <социология>100</социология>
    </student>
</students>
```
#### Представленный в файле src/XmlDataReader.py класс реализует чтение данных из  файлов формата .xml
```python
# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader

import xml.etree.cElementTree as xml


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str):
        tree = xml.ElementTree(file=path)
        root = tree.getroot()
        students = list(root)

        for student in students:
            self.key = student.attrib.get("class")
            student_children = list(student)
            self.students[self.key] = []

            for student_child in student_children:
                self.students[self.key].append((student_child.tag,
                                                int(student_child.text)))

        return self.students
```

#### Тестирование класса XmlDataReader осуществляется с помощью класса, реализованного в файле test/test_XmlDataReader.py:
```python
# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader

import xml.etree.cElementTree as xml
import random


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '<?xml version="1.0" encoding="UTF-8" ?>\n' + \
               '<students>\n' + \
               '    <student class="Иванов Константин Дмитриевич">\n' + \
               '        <математика>91</математика>\n' + \
               '        <химия>100</химия>\n' + \
               '    </student>\n' + \
               '    <student class="Петров Петр Семенович">\n' + \
               '        <русскийязык>87</русскийязык>\n' + \
               '        <литература>78</литература>\n' + \
               '    </student>\n' + \
               '</students>'

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русскийязык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

```

#### main.py:
```python
# -*- coding: utf-8 -*-
import argparse
from decimal import Clamped
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if (path[-3:] == 'txt'):
        reader = TextDataReader()
    else:
        reader = XmlDataReader()

    students = reader.read(path)
    print("Students: ", students, "\n")

    rating = CalcRating(students).calc()
    print("Rating: ", rating, "\n")


if __name__ == "__main__":
    main()

```

#### Тестирование проводилось в ОС Linux, дистр. Ubuntu 20.04 LTS
#### Работа кода ветки xml
![pull_xml](/img/xml.png)

#### Результаты модульных тестов
![pull_xml_test](/img/test1.png)

#### Успешный запуск на GitHub при слиянии веток main <- xml
![pull_merge](/img/merge1.png)

### Задание 4
### Создаем класс PrintStudents100 как наследник класса CalcRating, тест для этого класса и добавим запуск класса в файл main. Для этого откроем новую ветку, а именно "code100".
#### Представленный в файле src/PrintStudents100.py класс определяет и выводит на экран студента, имеющего 100 баллов по всем дисциплинам. Если таких студентов несколько, нужно вывести любого из них. Если таких студентов нет, необходимо вывести сообщение об их отсутствии.
```python
# -*- coding: utf-8 -*-
from Types import DataType

import random


class PrintStudents100:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.students: str = []

    def calc(self) -> str:
        for student in self.data:
            is100 = True
            for subject in self.data[student]:
                if int(subject[1]) != 100:
                    is100 = False
            if (is100):
                self.students.append(student)

        if len(self.students) == 0:
            return ("Ни у одного студента нет 100 баллов по всем дисциплинам")
        else:
            return ("У студента " + self.students
                    [random.randint(0, len(self.students)-1)] +
                    " 100 баллов по всем дисциплинам")
```

#### Тестирование класса PrintStudents100 осуществляется с помощью класса, реализованного в файле test/test_PrintStudents100.py:
```python
# -*- coding: utf-8 -*-
from src.Types import DataType
from src.PrintStudents100 import PrintStudents100
import pytest


class TestPrintStudents100:

    @pytest.fixture()
    def input_dataNo100(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        students: str = "Ни у одного студента" \
                        " нет 100 баллов по всем дисциплинам"

        return data, students

    @pytest.fixture()
    def input_data100(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        students: str = "У студента Абрамов Петр"\
                        " Сергеевич 100 баллов по всем дисциплинам"

        return data, students

    @pytest.fixture()
    def input_data100_2(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100),
                    ("литература", 100)
                ]
        }

        students: str = ["У студента Абрамов Петр Сергеевич"
                         " 100 баллов по всем дисциплинам",
                         "У студента Петров Игорь Владимирович"
                         " 100 баллов по всем дисциплинам"]

        return data, students

    def test_init_print_students_No100(self, input_dataNo100:
                                       tuple[DataType, str]) -> None:

        print_students_No100 = PrintStudents100(input_dataNo100[0])
        assert input_dataNo100[0] == print_students_No100.data

    def test_printNo100(self, input_dataNo100: tuple[DataType, str]) -> None:

        resultNo100 = PrintStudents100(input_dataNo100[0]).calc()
        assert resultNo100 == input_dataNo100[1]

    def test_init_print_students_100(self, input_data100:
                                     tuple[DataType, str]) -> None:

        print_students_100 = PrintStudents100(input_data100[0])
        assert input_data100[0] == print_students_100.data

    def test_print100(self, input_data100: tuple[DataType, str]) -> None:

        result100 = PrintStudents100(input_data100[0]).calc()
        assert result100 == input_data100[1]

    def test_init_print_students_100_2(self, input_data100_2:
                                       tuple[DataType, str]) -> None:

        print_students_100_2 = PrintStudents100(input_data100_2[0])
        assert input_data100_2[0] == print_students_100_2.data

    def test_print100_2(self, input_data100_2: tuple[DataType, str]) -> None:

        result100 = PrintStudents100(input_data100_2[0]).calc()
        assert (result100 == input_data100_2[1][0]) | (result100 ==
                                                       input_data100_2[1][1])

```

#### main.py:
```python
# -*- coding: utf-8 -*-
import argparse
from decimal import Clamped
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from PrintStudents100 import PrintStudents100


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if (path[-3:] == 'txt'):
        reader = TextDataReader()
    else:
        reader = XmlDataReader()

    students = reader.read(path)
    print("Students: ", students, "\n")

    rating = CalcRating(students).calc()
    print("Rating: ", rating, "\n")

    students100 = PrintStudents100(students).calc()
    print(students100)


if __name__ == "__main__":
    main()

```

#### Тестирование проводилось в ОС Linux, дистр. Ubuntu 20.04 LTS
#### Работа кода ветки code100
![pull_code100](/img/st100.png)

#### Результаты модульных тестов
![pull_xml_test2](/img/test2.png)

#### Успешный запуск на GitHub при слиянии веток main <- code100
![pull_merge2](/img/merge2.png)

#### Диаграмма загрузок branch и их слияний
![pull_network](/img/network.png)

### Задание 5
### UML-диаграмма классов проекта : 
![pull_uml](/img/uml.png)