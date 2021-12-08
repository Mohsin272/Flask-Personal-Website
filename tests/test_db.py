import DBcm
from appconfig import config


def test_running_locally():
    """Check to see if the config is running for the local setting"""
    assert config["host"] == "127.0.0.1"


def test_count_increase(client, clean_up_db):
    """Check to insure the number of rows in the database and increment it by 1"""
    with DBcm.UseDatabase(config) as db:
        SQL = "select count(*) from comments"
        db.execute(SQL)
        results = db.fetchall()
    initial_count = results[0][0]  # gets count of rows before we send

    form_data = {
        "email": "test2@test.com",
        "message": "test",
    }
    # Send the data to the webapp using the forms url
    client.post("/processform", data=form_data)

    # go get the get the count of rows and check if it is +1
    with DBcm.UseDatabase(config) as db:
        SQL = "select count(*) from comments"
        db.execute(SQL)
        results = db.fetchall()
    new_count = results[0][0]  # gets count of rows before we send
    assert new_count == initial_count + 1


def test_last_row(client, clean_up_db):
    """Is the last row of data equal to what was submitted via the form"""
    form_data = {
        "email": "test3@test.com",
        "message": "test",
    }
    # Send the data to the webapp using the forms url
    client.post("/processform", data=form_data)

    with DBcm.UseDatabase(config) as db:
        SQL = """select email,message
                 from comments
                 order by id desc
                 limit 1"""
        db.execute(SQL)
        results = db.fetchall()
    assert results[0][0] == form_data["email"]
    assert results[0][1] == form_data["message"]
