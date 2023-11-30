from lib.user import User

#test that checks user initialises values
def test_user_initalises():
    user = User(1, "katieanthonisz","anthonisz@live.co.uk")
    assert user.id == 1
    assert user.username == "katieanthonisz"
    assert user.user_email_address == "anthonisz@live.co.uk"


#test that user only adds unique names

def test_user_eq_works():
    user = User(1, "katieanthonisz","anthonisz@live.co.uk")
    user2 = User(1, "katieanthonisz","anthonisz@live.co.uk")
    assert user == user2


# tests that repr returns the format that is readable

def test_repr_function():
    user = User(1, "katieanthonisz","anthonisz@live.co.uk")
    assert str(user) == "User(Username: katieanthonisz, email address: anthonisz@live.co.uk)"


