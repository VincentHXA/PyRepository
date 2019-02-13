
import src.patterns.abstract_factory as af
import pytest

def test_abstract_factory():

    world = af.choose_world_on_age(5)('Vincent')
    env = af.GameEnv(world)
    env.play()

    world = af.choose_world_on_age(13)('David')
    env = af.GameEnv(world)
    env.play()

    with pytest.raises(ValueError, match='age must be ') as excinfo:
        world = af.choose_world_on_age('hello')