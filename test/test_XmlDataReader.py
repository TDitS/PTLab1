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
