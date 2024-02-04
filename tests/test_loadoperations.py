from src.func import load_operations


def test_load_operations():
    file_name = 'test_operations.json'
    operation = load_operations(file_name)
    assert len(operation) == 2
