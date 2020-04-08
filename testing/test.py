import pytest
import urllib3
from flask import Flask
import os

def test_service():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost/')
    assert 200 == r.status
def test_service1():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5000/')
    assert 200 == r.status
def test_service2():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.134.136:5000/')
    assert 200 == r.status
def test_service3():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.134.136/')
    assert 200 == r.status