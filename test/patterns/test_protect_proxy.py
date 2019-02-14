
from src.patterns.proxy.protest_proxy import InfoProxy


def test_protect_proxy():
    info_proxy = InfoProxy()

    info_proxy.read()
    info_proxy.add('Vincent', '123456')
    info_proxy.add('David', '123')
