
from abc import ABCMeta, abstractmethod


class NewsPublisher:

    def __init__(self):
        self._subscribers = []
        self._last_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def deattach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_all(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def notify(self, subscriber):
        subscriber.update()

    def add_news(self, news):
        self._last_news = news

    def get_news(self):
        return 'Got news: ', self._last_news


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):

    def __init__(self, publiser):
        self._publiser = publiser
        self._publiser.attach(self)

    def update(self):
        print(type(self).__name__, self._publiser.get_news())


class SMSSubscriber(Subscriber):

    def __init__(self, publisher):
        self._publisher = publisher
        self._publisher.attach(self)

    def update(self):
        print(type(self).__name__, self._publisher.get_news())


class EmailSubscriber(Subscriber):

    def __init__(self, publisher):
        self._publisher = publisher
        self._publisher.attach(self)

    def update(self):
        print(type(self).__name__, self._publisher.get_news())


class AnyOtherSubscriber(Subscriber):

    def __init__(self, publisher):
        self._publisher = publisher
        self._publisher.attach(self)

    def update(self):
        print(type(self).__name__, self._publisher.get_news())
