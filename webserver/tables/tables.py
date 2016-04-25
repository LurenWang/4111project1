stmt1 = """CREATE TABLE IF NOT EXISTS Users (
    username TEXT PRIMARY KEY,
    name TEXT,
    password TEXT,
    contact_info TEXT,
    description TEXT
);"""

stmt2 = """CREATE TABLE IF NOT EXISTS Sessions (
    username TEXT,
    sid SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    start_time TEXT NOT NULL,
    session_length INT NOT NULL,
    location TEXT NOT NULL,
    meta JSON NOT NULL,
    description TEXT,
    FOREIGN KEY(username) REFERENCES Users
);"""

stmt3 = """CREATE TABLE IF NOT EXISTS Attends (
    username TEXT,
    sid INT,
    role TEXT CHECK (role IN ('attendee', 'admin')),
    PRIMARY KEY(username, sid),
    FOREIGN KEY(username) REFERENCES Users ON DELETE CASCADE,
    FOREIGN KEY(sid) REFERENCES Sessions on DELETE CASCADE
);"""

#Most popular tags
stmt4 = """CREATE TABLE IF NOT EXISTS MetaTags (
    tag TEXT UNIQUE NOT NULL,
    count INT DEFAULT 1,
    PRIMARY KEY(tag)
);"""

stmt5 = """CREATE TABLE IF NOT EXISTS Posts (
    pid SERIAL PRIMARY KEY,
    username TEXT,
    timestamp TIMESTAMP DEFAULT NOW(),
    sid INT,
    posted_text TEXT NOT NULL,
    FOREIGN KEY(username) REFERENCES Users ON DELETE CASCADE,
    FOREIGN KEY(sid) REFERENCES Sessions ON DELETE CASCADE
);"""

stmt6 = """CREATE TABLE IF NOT EXISTS Posted_Pictures (
    pid INT,
    image_path TEXT PRIMARY KEY,
    sid INT,
    FOREIGN KEY(pid) REFERENCES Posts ON DELETE CASCADE,
    FOREIGN KEY(sid) REFERENCES Sessions ON DELETE CASCADE
);"""

stmt7 = """CREATE TABLE IF NOT EXISTS Comments (
    pid INT,
    username TEXT,
    timestamp TIMESTAMP DEFAULT NOW(),
    posted_text TEXT NOT NULL,
    PRIMARY KEY(pid, username, timestamp),
    FOREIGN KEY(pid) REFERENCES Posts ON DELETE CASCADE
);"""

#stmt8 = """DROP TABLE IF EXISTS Users CASCADE;"""
#stmt9 = """DROP TABLE IF EXISTS Sessions CASCADE;"""
#stmt10 = """DROP TABLE IF EXISTS Attends CASCADE;"""
#stmt11 = """DROP TABLE IF EXISTS Tags CASCADE;"""
#stmt12 = """DROP TABLE IF EXISTS Posts CASCADE;"""
#stmt13 = """DROP TABLE IF EXISTS Posted_Pictures CASCADE;"""
#stmt14 = """DROP TABLE IF EXISTS Comments CASCADE;"""
stmt8 = """drop schema public cascade;"""
stmt9 = """create schema public;"""

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
