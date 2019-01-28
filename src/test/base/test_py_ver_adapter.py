
import pytest
import src.base.py_ver_adapter as pvadapter

if pvadapter.earlier_than(3, 5, 0):
    # assert True
    pytest.skip('skip because of Python version', allow_module_level=True)
elif pvadapter.later_than(2, 7, 0):
    # assert True
    pytest.skip('skip because of Python version', allow_module_level=True)
else:
    assert False

def test_not_run():
    assert False