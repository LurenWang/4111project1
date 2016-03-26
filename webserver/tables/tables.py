stmt1 = """CREATE TABLE IF NOT EXISTS Users (
    uid INTEGER PRIMARY KEY,
    username STRING UNIQUE,
    name STRING,
    password STRING,
    contact_info STRING,
    description TEXT
);"""

stmt2 = """CREATE TABLE IF NOT EXISTS Sessions (
    uid INT,
    sid INTEGER PRIMARY KEY,
    start_time DATE NOT NULL,
    session_length INT NOT NULL,
    location TEXT NOT NULL,
    type TEXT CHECK (type IN ('study group', 'tutor', 'events')),
    description TEXT,
    FOREIGN KEY(uid) REFERENCES Users
);"""

stmt3 = """CREATE TABLE IF NOT EXISTS Attends (
    uid INT,
    sid INT,
    role TEXT CHECK (role IN ('attendee', 'admin')),
    PRIMARY KEY(uid, sid),
    FOREIGN KEY(uid) REFERENCES Users ON DELETE CASCADE,
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
    uid INT,
    sid INT,
    posted_text TEXT NOT NULL,
    FOREIGN KEY(uid) REFERENCES Users ON DELETE CASCADE,
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
    uid INT,
    time DATE,
    posted_text TEXT NOT NULL,
    PRIMARY KEY(pid, uid, time),
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
