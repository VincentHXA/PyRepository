
class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))

class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def demo():
    mw = MainWindow()
    sd = SendDialog(mw)
    mt = MsgText(sd)

    for _ in ('down', 'close', 'paint', 'whatever'):
        evt = Event(_)
        mt.handle(evt)
