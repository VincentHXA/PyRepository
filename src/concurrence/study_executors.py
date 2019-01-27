
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

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
        executor_cls = ThreadPoolExecutor
    else:
        executor_cls = ProcessPoolExecutor

    with executor_cls(POOL_SIZE) as executor:
        futures = [executor.submit(work, name) for name in NAMES]

    for future in futures:
        print(future.result())

if __name__ == '__main__':
    main(True)
