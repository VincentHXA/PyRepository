
from abc import ABCMeta, abstractmethod


# class SensitiveInfo(metaclass=ABCMeta):
class SensitiveInfo(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('{} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user: {}'.format(user))


class InfoProxy:
    class ConcreteSensitiveInfo(SensitiveInfo):
        def __init__(self):
            self.users = ['nick', 'tom', 'ben', 'mike']

    def __init__(self):
        self.password = '123456'
        self.protected = self.ConcreteSensitiveInfo()
        # self.password = config.get('password')

    def read(self):
        self.protected.read()

    def add(self, user, psd):
        self.protected.add(user) if psd == self.password else print('password wrong')





