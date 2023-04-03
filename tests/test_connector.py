from project_classes.connector import Connector

def test_str_connector(path):
    """Тестируем метод str"""
    file = Connector(path)
    assert file.__str__() == "Коннектор работает с файлом file_connector.json"

def test_repr_connector(path):
    """Тестируем метод repr"""
    file = Connector(path)
    assert file.__repr__() == "Коннектор работает с файлом file_connector.json"

def test_insert_select_connector(path):
    """Тестируем методы insert,select"""
    file = Connector(path)
    data_for_file = [{'name': "Python"}]
    file.insert(data_for_file)
    assert file.select({'name': "Python"}) == [{'name': "Python"}]
    file.delete({'name': "Python"})

def test_delete_connector(path):
    """Тестируем метод delete"""
    file = Connector(path)
    data_for_file = [{'name': "Java"},{'name': "Python"} ]
    file.insert(data_for_file)

    assert file.delete({}) is None
    file.delete({'name': "Java"})
    assert file.select({}) == [{'name': "Python"}]
    file.delete({'name': "Python"})

def test_data_file_connector(path):
    """Тестируем установку нового файла и проверку пути старого"""
    file = Connector(path)

    assert file.data_file == 'file_connector.json'
    file.data_file = 'file_connector2.json'
    assert file.data_file == 'file_connector2.json'