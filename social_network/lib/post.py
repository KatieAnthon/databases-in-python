# class defines a single post

class Post():
    def __init__(self, id, post_title, post_content, post_views, user_id):
        self.id = id
        self.post_title = post_title
        self.post_content = post_content
        self.post_views = post_views
        self.user_id = user_id

    # function to ensure that the same nblog entry is only entered once - no duplicates
    # side effects: None
    # returns nothing 
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # function to return post in readable value
    # side effects: adjusts object to readable value
    # returns a strin in readable format 
    def __repr__(self):
        return f"Post({self.id}, {self.post_title}, {self.post_content}, {self.post_views}, {self.user_id})"



