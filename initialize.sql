DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id INT PRIMARY KEY,
	username VARCHAR(50),
	email VARCHAR(100),
	created_at DATETIME
);

CREATE TABLE posts (
	post_id INT PRIMARY KEY,
	user_id INT,
	title VARCHAR(100),
	body TEXT,
	posted_at DATETIME,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, created_at) VALUES (1, 'charlotte', 'charlotte@lab4.com', '2026-09-28 9:35:25');
INSERT INTO users (user_id, username, email, created_at) VALUES (2, 'julia', 'julia@lab4.com', '2026-09-28 9:36:13');
INSERT INTO users (user_id, username, email, created_at) VALUES (3, 'sienna', 'sienna@lab4.com', '2026-09-28 9:37:14');
INSERT INTO users (user_id, username, email, created_at) VALUES (4, 'anika', 'anika@lab4.com', '2026-09-28 9:37:30');
INSERT INTO users (user_id, username, email, created_at) VALUES (5, 'nina', 'nina@lab4.com', '2026-09-28 9:37:44');
INSERT INTO users (user_id, username, email, created_at) VALUES (6, 'lanier', 'lanier@lab4.com', '2026-09-28 9:38:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (7, 'lucy', 'lucy@lab4.com', '2026-09-28 9:38:20');
INSERT INTO users (user_id, username, email, created_at) VALUES (8, 'sam', 'sam@lab4.com', '2026-09-28 9:38:37');
INSERT INTO users (user_id, username, email, created_at) VALUES (9, 'tomas', 'tomas@lab4.com', '2026-09-28 9:38:56');
INSERT INTO users (user_id, username, email, created_at) VALUES (10, 'brody', 'brody@lab4.com', '2026-09-28 9:39:23');

INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (1, 1, 'CW', 'I am Charlotte', '2026-09-28 09:00:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (2, 2, 'JM', 'I am Julia', '2026-09-28 09:40:57');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (3, 3, 'SW', 'I am Sienna', '2026-09-28 09:41:36');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (4, 4, 'AG', 'I am Anika', '2026-09-28 09:42:49');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (5, 5, 'NT', 'I am Nina', '2026-09-28 09:43:22');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (6, 6, 'LE', 'I am Lanier', '2026-09-28 09:43:37');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (7, 7, 'LT', 'I am Lucy', '2026-09-28 09:43:59');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (8, 8, 'SP', 'I am Sam', '2026-09-28 09:44:17');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (9, 9, 'TG', 'I am Tomas', '2026-09-28 09:44:36');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (10, 10, 'BP', 'I am Brody', '2026-09-28 09:44:59');