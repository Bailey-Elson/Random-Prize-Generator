import pytest
import urllib3
from flask import Flask
import os


def test_service1():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5000/')
    assert 200 == r.status

def test_service2():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5001/prizetype')
    assert 200 == r.status

def test_service3():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5002/randomprize')
    assert 200 == r.status

def test_service4():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5003/generateprize')
    assert 200 == r.status