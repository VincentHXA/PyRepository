
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool

import time
import os

NAMES = (
    'Vincent', 'David', 'Victor', 'Dominique', 'Linda'
)

POOL_SIZE = 5


def work(name):
    time.sleep(3)
    print('{} - pid: {} sleep 3 s'.format(name, os.getpid()))
    return name + "_done"


def main(use_threas = False):
    if use_threas:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool

    with pool_cls(POOL_SIZE) as pool:
        results = pool.map(work, NAMES)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()
