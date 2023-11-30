from lib.post import Post
# class which enables user to add, show specifc posts and all posts
class PostRepository():
    #initialies conntection to sql database
    def __init__(self, connection):
        self._connection = connection

    # function shows all posts
    # side effects: returns all posts
    # returns all posts in table 
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []

        for row in rows:
            item = Post(row["id"], row["post_title"], row["post_content"], row["post_views"], row["user_id"])
            posts.append(item)

        return posts

    # function shows one post based on id
    # side-effects: returns 1 post 
    # returns post
    def find(self, post_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id=%s', [post_id])
        row = rows[0]
        return Post(row["id"], row["post_title"], row["post_content"], row["post_views"], row["user_id"])

    # function that creates a post entry
    # side effects: creates entry
    # returns None

    def create(self, new_post):
        self._connection.execute('INSERT INTO posts (post_title, post_content, post_views, user_id) VALUES (%s, %s, %s, %s)', [new_post.post_title, new_post.post_content, new_post.post_views, new_post.user_id])

        return None