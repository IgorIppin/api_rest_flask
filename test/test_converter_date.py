# Tests for second level

from service.converter_date import converter, create_json


def test_converter():
    res = converter('2020-11-29')
    assert res['original_date'] == '2020-11-29' and res['timestamp'] == 1606604400


def test_converter_error_slice():
    res = converter('2020/11/29')
    assert res['error'] == 'El formato o la fecha es incorrecto.'


def test_converter_error_date():
    res = converter('202020-11-29')
    assert res['error'] == 'El formato o la fecha es incorrecto.'


def test_create_json():
    date = '2020-11-29'
    timestamp = 1606604400
    res = create_json(date, timestamp)
    assert res['original_date'] == date
    assert res['timestamp'] == timestamp
