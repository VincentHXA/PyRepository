
import src.patterns.proxy.virtual_proxy as vp


def test_virtual_proxy():
    t = vp.Test()
    print(t.x)
    print(t.y)

    import time
    time.sleep(2)

    print(t.resource)
    print(t.resource)

