import pytest
from module.utils import template

def test_module():
    result = template()
    assert result == 'Template'