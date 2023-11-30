
class User():
    # initially this designs the variables - usernames etc
    def __init__(self, id, username, user_email_address):
        self.id = id
        self.username = username
        self.user_email_address = user_email_address

    def __eq__(self, other):
    #define a function that ensures only unique usernames are added
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User(Username: {self.username}, email address: {self.user_email_address})"
