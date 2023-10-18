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
