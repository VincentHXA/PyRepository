
"""
This module gathers self-defined pytest fixtures.

Fixtures contained in this module don't need to be imported explicitly,
they will be automatically discovered by pytest.
"""

import pytest
import time

@pytest.fixture(scope='module')
def example_connection():
    print('setup example connection')
    yield ('Hello', 'World')
    print('teardown example connection')
