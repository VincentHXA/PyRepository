
import test.pytest_markers as pytest_markers

# 跳过级别：module
# import pytest
# import src.base.py_ver_adapter as py_ver_adapter
# pytestmark = pytest.mark.skipif(py_ver_adapter.later_than(3, 5, 0), reason='at least python-3.5.0 required')

# 跳过级别：method
@pytest_markers.minversion
def test_not_run():
    assert False