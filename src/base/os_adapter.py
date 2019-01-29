
"""
TODO: TO FILL
"""


def get_os():
    import platform

    return platform.system()


def is_windows():
    return get_os() == 'Windows'


def is_linux():
    return get_os() == 'Linux'
