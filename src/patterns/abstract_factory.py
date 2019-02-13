
from abc import ABCMeta, abstractmethod


class Character:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the {} encounters {} and {}!'.format(self,
                                                       self.name, obstacle, obstacle.action()))

class Frog(Character):
    pass


class Wizard(Character):
    pass


class Insect(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def action(self):
        pass


class Bug(Insect):
    def __repr__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class Ork(Insect):
    def __repr__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class FairyTallWorld(metaclass=ABCMeta):
    def __init__(self, name):
        print(self)
        self.player_name = name

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_character(self):
        pass

    @abstractmethod
    def make_obstacle(self):
        pass


class FrogWorld(FairyTallWorld):
    def __repr__(self):
        return '\n\n\t------- Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class WizardWorld(FairyTallWorld):
    def __repr__(self):
        return '\n\n\t------- Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnv:
    def __init__(self, world):
        self.hero = world.make_character()
        self.obstacle = world.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def choose_world_on_age(age):
    if not isinstance(age, int):
        raise ValueError('age must be integer')

    if age < 10:
        return FrogWorld
    else:
        return WizardWorld


