import pytest
import app as webapp
import DBcm
from appconfig import config


@pytest.fixture
def app():
    """This fixture create the client object before each tets runs 
    assuming the test references the client object"""
    app = webapp.app
    return app


@pytest.fixture
def clean_up_db():
    """This code removes any and all test data from the db 
    after the tests which refer to it run
    """
    # this code before the yield runs before the test runs
    yield
    # this code after the yield, runs after the test runs

    with DBcm.UseDatabase(config) as db:
        SQL = "delete from comments where email = 'test@test.com'"
        db.execute(SQL)

    with DBcm.UseDatabase(config) as db:
        SQL = "delete from comments where email = 'test2@test.com'"
        db.execute(SQL)

    with DBcm.UseDatabase(config) as db:
        SQL = "delete from comments where email = 'test3@test.com'"
        db.execute(SQL)
