
from src.patterns.adapter.external import Human, Synthesizer


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        dict_adapted_methods = dict(adapted_methods)
        self.__dict__.update(dict_adapted_methods)

    def __str__(self):
        return str(self.obj)

    @property
    def name(self):
        return self.obj.name


def demo():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    human = Human('Vincent')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    objects.append(Adapter(human, dict(execute=human.speak)))

    for obj in objects:
        print('{} - {} - {}'.format(str(obj), obj.name, obj.execute()))