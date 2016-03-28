stmt1 = """CREATE TABLE IF NOT EXISTS Users (
    username STRING PRIMARY KEY,
    name STRING,
    password STRING,
    contact_info STRING,
    description TEXT
);"""

stmt2 = """CREATE TABLE IF NOT EXISTS Sessions (
    username STRING,
    sid INTEGER PRIMARY KEY,
    title STRING NOT NULL,
    start_time STRING NOT NULL,
    session_length INT NOT NULL,
    location TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY(username) REFERENCES Users
);"""

stmt3 = """CREATE TABLE IF NOT EXISTS Attends (
    username STRING,
    sid INT,
    role TEXT CHECK (role IN ('attendee', 'admin')),
    PRIMARY KEY(username, sid),
    FOREIGN KEY(username) REFERENCES Users ON DELETE CASCADE,
    FOREIGN KEY(sid) REFERENCES Sessions on DELETE CASCADE
);"""

stmt4 = """CREATE TABLE IF NOT EXISTS Tags (
    sid INT,
    tag TEXT NOT NULL,
    PRIMARY KEY(sid, tag),
    FOREIGN KEY(sid) REFERENCES Sessions ON DELETE CASCADE
);"""

stmt5 = """CREATE TABLE IF NOT EXISTS Posts (
    pid INTEGER PRIMARY KEY,
    username STRING,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    sid INT,
    posted_text TEXT NOT NULL,
    FOREIGN KEY(username) REFERENCES Users ON DELETE CASCADE,
    FOREIGN KEY(sid) REFERENCES Sessions ON DELETE CASCADE
);"""

stmt6 = """CREATE TABLE IF NOT EXISTS Posted_Pictures (
    title TEXT,
    pid INT,
    image_path TEXT NOT NULL,
    PRIMARY KEY(title, pid),
    FOREIGN KEY(pid) REFERENCES Posts ON DELETE CASCADE
);"""

stmt7 = """CREATE TABLE IF NOT EXISTS Comments (
    pid INT,
    username STRING,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    posted_text TEXT NOT NULL,
    PRIMARY KEY(pid, username, timestamp),
    FOREIGN KEY(pid) REFERENCES Posts ON DELETE CASCADE
);"""

stmt8 = """DROP TABLE IF EXISTS Users;"""
stmt9 = """DROP TABLE IF EXISTS Sessions;"""
stmt10 = """DROP TABLE IF EXISTS Attends;"""
stmt11 = """DROP TABLE IF EXISTS Tags;"""
stmt12 = """DROP TABLE IF EXISTS Posts;"""
stmt13 = """DROP TABLE IF EXISTS Posted_Pictures;"""
stmt14 = """DROP TABLE IF EXISTS Comments;"""

create_lst = []
create_lst.append(stmt1)
create_lst.append(stmt2)
create_lst.append(stmt3)
create_lst.append(stmt4)
create_lst.append(stmt5)
create_lst.append(stmt6)
create_lst.append(stmt7)

del_lst = []
del_lst.append(stmt8)
del_lst.append(stmt9)
del_lst.append(stmt10)
del_lst.append(stmt11)
del_lst.append(stmt12)
del_lst.append(stmt13)
del_lst.append(stmt14)
