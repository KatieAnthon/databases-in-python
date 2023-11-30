from lib.post_repository import PostRepository
from lib.post import Post

def test_function_returns_all_entries(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1, "its the time", "you will never believe", 4, 3),
        Post(2, 'winter','it is freezing!', 5, 2),
        Post(3, 'Santa','have your presents arrived yet?', 2, 1),
    ]
    
def test_function_finds_post_id(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    posts = repository.find(2)

    assert posts == Post(2, 'winter','it is freezing!', 5, 2)

def test_create_function(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    new_entry = Post(None,"hello title", "post contents!", 5, 2)
    repository.create(new_entry)
    all_values = repository.all()

    assert all_values == [
        Post(1, "its the time", "you will never believe", 4, 3),
        Post(2, 'winter','it is freezing!', 5, 2),
        Post(3, 'Santa','have your presents arrived yet?', 2, 1),
        Post(4, 'hello title','post contents!', 5, 2),
    ]
