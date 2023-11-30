from lib.user_repository import UserRepository
from lib.user import User

#test that all function returns all values in users table
def test_user_repository_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    user_repository = UserRepository(db_connection)
    users = user_repository.all()
    assert users == [
        User(1, "katierose", "rose@hotmail.co.uk"),
        User(2, "xerox", "xerox@hotmail.co.uk"),
        User(3, "coder123", "coder123@hotmail.co.uk"),
        ]

# test that find function finds specific user entry based on id

def test_user_repository_finds_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user = user_repository.find(1)

    assert user == User(1, "katierose", "rose@hotmail.co.uk")


#test function that checks specifidc value has been added to the table
def test_user_repository_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user_repository.create(User(None,"newuser", "newuser@hotmail.co.uk"))
    users = user_repository.all()
    assert users == [
        User(1, "katierose", "rose@hotmail.co.uk"),
        User(2, "xerox", "xerox@hotmail.co.uk"),
        User(3, "coder123", "coder123@hotmail.co.uk"),
        User(4, "newuser", "newuser@hotmail.co.uk")
        ]

