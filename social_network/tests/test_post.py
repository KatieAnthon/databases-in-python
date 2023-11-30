from lib.post import Post


def test_post_function_recognises_the_same_value_as_equal():
    post = Post(1, "Post_title1", "post_content1", 4, 2)
    post2 = Post(1, "Post_title1", "post_content1", 4, 2)

    assert post == post2

# create/ test function that returns the post entry in readable format

def test_repr_function_is_working():
    post = Post(1, "Post_title1", "post_content1", 4, 2)
    assert str(post) ==  "Post(1, Post_title1, post_content1, 4, 2)"




