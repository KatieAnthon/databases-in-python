DROP TABLE IF EXISTS users cascade;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_email_address text,
    username text
);

DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title text,
    post_content text,
    post_views int,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);


INSERT INTO users (user_email_address, username) VALUES ('rose@hotmail.co.uk','katierose');
INSERT INTO users (user_email_address, username) VALUES ('xerox@hotmail.co.uk','xerox');
INSERT INTO users (user_email_address, username) VALUES ('coder123@hotmail.co.uk', 'coder123');



INSERT INTO posts (post_title, post_content, post_views, user_id) VALUES ('its the time','you will never believe', 4, 3);
INSERT INTO posts (post_title, post_content, post_views, user_id) VALUES ('winter','it is freezing!', 5, 2);
INSERT INTO posts (post_title, post_content, post_views, user_id) VALUES ('Santa','have your presents arrived yet?', 2, 1);