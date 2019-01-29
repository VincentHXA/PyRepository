import test.pytest_markers as pytest_markers

# 跳过级别：module
# import pytest
# import src.base.os_adapter as osadapter
# pytestmark = pytest.mark.skipif(osadapter.is_windows(), reason='windows only')

# 跳过级别：method
@pytest_markers.win_only
def test_not_run():
    assert False