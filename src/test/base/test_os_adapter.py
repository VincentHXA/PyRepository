
import sys

import src.test.pytest_markers as pytest_markers

# pytestmark = pytest.mark.skipif(osadapter.is_windows(), reason='linux only')

# if osadapter.is_windows():
#     assert True
#     # pytest.skip('skip because on Windows system', allow_module_level=True)
# elif osadapter.is_linux():
#     # assert True
#     pytest.skip('skip because on Linux system', allow_module_level=True)
# else:
#     assert False

@pytest_markers.win_only
def test_not_run():
    assert False