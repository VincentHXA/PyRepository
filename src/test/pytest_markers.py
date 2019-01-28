
import pytest
import src.base.py_ver_adapter as pvadapter
import src.base.os_adapter as osadapter

skipif = pytest.mark.skipif
skip = pytest.mark.skip
xfail = pytest.mark.xfail

minversion = skipif(pvadapter.later_than(3, 5, 0),
                                reason='at least python-3.5.0 required')

win_only = skipif(osadapter.is_windows(), reason='Windows only')
linux_only = skipif(osadapter.is_linux(), reason='linux only')

