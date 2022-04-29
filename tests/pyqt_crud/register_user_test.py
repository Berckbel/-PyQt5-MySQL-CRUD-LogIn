from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st
from hypothesis.strategies._internal.core import characters
from pytest import fixture

from pyqt_crud.controllers import user as ts
from pyqt_crud.models.user import User
from pyqt_crud.services import database


@fixture
def connection():
    return database.connect(':memory:')


@given(
    username=st.text(
        min_size=8,
        max_size=21,
        alphabet=characters(whitelist_categories=['L', 'N']),
    ),
    password=st.text(min_size=8, max_size=24),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_register_user(connection, username, password):
    controller = ts.UserController(connection)

    expected = User(username, password)
    controller.register(expected)

    assert controller.login(username, password)
