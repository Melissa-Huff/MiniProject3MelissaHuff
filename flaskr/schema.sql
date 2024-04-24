DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS activity;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE activity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  date DATE NOT NULL,
  activity_type TEXT NOT NULL,
  duration INTEGER NOT NULL,  -- Duration in minutes
  calories_burned INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
