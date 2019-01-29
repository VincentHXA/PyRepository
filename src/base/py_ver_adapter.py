
import sys

def get_py_version():
    return sys.version_info

def earlier_than(major=3, minor=0, micro=0):
    return get_py_version() < (major, minor, micro)

def later_than(major=3, minor=0, micro=0):
    return get_py_version() > (major, minor, micro)

