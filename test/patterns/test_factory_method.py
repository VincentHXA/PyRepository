
import src.patterns.factory.factory_method as fm
import pytest


def test_factory_method():
    json_file = fm.connect_to('example.json')
    print(json_file)

    xml_file = fm.connect_to('example.xml')
    print(xml_file)

    xlsx_file = fm.connect_to('example.xlsx')

    with pytest.raises(ValueError, match='Cannot connect to') as excinfo:
        xlsx_file = fm.connection_factory('example.xlsx')