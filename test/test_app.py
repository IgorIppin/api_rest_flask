# Tests for first level
import requests
import pytest


def test_home():
    url = 'http://0.0.0.0:2560?date=2020-11-29'
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()['original_date'] == '2020-11-29'
    assert res.json()['timestamp'] == 1606604400


def test_home_not_args():
    url = 'http://0.0.0.0:2560'
    res = requests.get(url)
    assert res.status_code == 400
    assert res.json()['error'] == 'No se envio ninguna fecha.'


def test_home_key_error_args():
    url = 'http://0.0.0.0:2560?datee=2020-11-29'
    res = requests.get(url)
    assert res.status_code == 400
    assert res.json()['error'] == "La key debe llamarse 'date'."
