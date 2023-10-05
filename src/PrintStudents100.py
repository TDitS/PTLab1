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
