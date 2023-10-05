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
