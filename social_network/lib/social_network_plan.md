1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns: user_email_address, username, pos, post_title, post_content, post_views


2. Infer the Table Name and Columns

Record    | Properties
---------- ------------
user      | user_email_address, username
posts     | user_id, post_title, post_content, post_views



3. Decide the column types

table: users
id: serial
user_email_address: text
username: text
post_id: int

table: posts
id: serial
post_title: text
post_content: text
post_views: int


# EXAMPLE:

4. Decide on The Tables Relationship
users have many posts

foreign key would be post_id

5. Write the SQL

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_email_address text,
    username text,
    user_id int
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title text,
    post_content text,
    post_views int,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade

);

6. Create the tables
psql -h 127.0.0.1 social_network < seeds/social_network.sql


7. Define the class names
class User()

class UserRepository()

class Post()

class PostRepository()


8. Implement the Model class
Class User():

Class Post()

9. Define the Repository Class interface
Class UserRepository()

Class PostRepository()

10. Write Test Examples


11. Test-drive and implement the Repository class behaviour
