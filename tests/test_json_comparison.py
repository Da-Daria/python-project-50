import json
import pytest

def compare_json(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1 == data2

def test_compare_json():
    assert compare_json('tests/test_data/file1.json', 'tests/test_data/file2.json') == True
