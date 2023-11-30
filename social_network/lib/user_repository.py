from lib.user import User

class UserRepository():
    #function used to connect to table and implement all and find functions
    #firstly need to initialise the gloabl variables
    def __init__(self, connection):
        self.connection = connection

    #function finds all entries in user table
    def all(self):
        rows = self.connection.execute('SELECT * FROM users;')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["user_email_address"])
            users.append(item)
        return users

    #function finds a specific entry in the user table
    # returns specifc user
    def find(self,user_id):
        rows = self.connection.execute('SELECT * FROM users WHERE id=%s;',[user_id])
        user = rows[0]
        return User(user["id"], user["username"], user["user_email_address"])

    #function that creates a user in the user table
    # side effects - adds value to table
    # returns - nothing  
    def create(self, user):
        self.connection.execute('INSERT INTO users (username, user_email_address) VALUES (%s, %s)', [
            user.username, user.user_email_address])
        return None