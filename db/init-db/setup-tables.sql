CREATE TABLE IF NOT EXISTS Users(
    username TEXT, email TEXT, password TEXT, requires_pass_change INT,
    PRIMARY KEY (username)
);
CREATE TABLE IF NOT EXISTS OldPasswords(
    id INTEGER PRIMARY KEY, username TEXT, password TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
);
CREATE TABLE IF NOT EXISTS Customers(
    name TEXT, id INT, address TEXT, animal TEXT, feet_size INT,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS LoginAudit(
    username TEXT, ts TIMESTAMP
);
