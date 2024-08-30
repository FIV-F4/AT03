import pytest
from main import *

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'weather': [{'description': 'test'}],'main': {'temp': 10}}

    weather = get_weather('test', 'test')
    assert weather['weather'][0]['description'] == 'test'

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {'error': 'test'}

    weather = get_weather('test', 'test')
    assert weather == None

def test_get_github_username(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'login': 'test', 'id': 1,'name': 'test'}

    username = get_github_username('test', 'test')
    assert username == {'login': 'test', 'id': 1,'name': 'test'}

def test_get_github_username_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {'error': 'test'}

    username = get_github_username('test', 'test')
    assert username == None



def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    url = get_random_cat_image()
    assert url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    url = get_random_cat_image()
    assert url is None
