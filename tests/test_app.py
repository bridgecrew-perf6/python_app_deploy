import pytest
from app import index

def test_index():
	string = "Hello, World!!!"
	assert index() == string