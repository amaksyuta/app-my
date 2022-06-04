import app

def test_get_file_extension():
    assert app.get_file_extension("test.txt") == "txt" 
    assert app.get_file_extension("test.json") == "json"
    assert app.get_file_extension("test.csv") == "csv"


def test_get_file_name():
    assert app.get_file_name("test.txt") == "test"
    assert app.get_file_name("new_file.json") == "new_file"
    assert app.get_file_name("new.ttf") == "new"
    