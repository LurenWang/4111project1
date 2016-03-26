#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from sqlalchemy import *
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, url_for, \
        flash
import pdb
from tables import *
from forms import *

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following uses the sqlite3 database test.db -- you can use this for debugging purposes
# However for the project you will need to connect to your Part 2 database in order to use the
# data
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@w4111db.eastus.cloudapp.azure.com/username
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@w4111db.eastus.cloudapp.azure.com/ewu2493"
#
DATABASEURI = "sqlite:///test.db"


#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)
Session = None


#
# START SQLITE SETUP CODE
#
# after these statements run, you should see a file test.db in your webserver/ directory
# this is a sqlite database that you can query like psql typing in the shell command line:
# 
#     sqlite3 test.db
#
# The following sqlite3 commands may be useful:
# 
#     .tables               -- will list the tables in the database
#     .schema <tablename>   -- print CREATE TABLE statement for table
# 
# The setup code should be deleted once you switch to using the Part 2 postgresql database
#
#engine.execute("""DROP TABLE IF EXISTS test;""")
#engine.execute("""CREATE TABLE IF NOT EXISTS test (
  #id serial,
  #name text
#);""")
#engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")
for stmt in del_lst:
    engine.execute(stmt)

for stmt in create_lst:
    engine.execute(stmt)
#
# END SQLITE SETUP CODE
#

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    global Session
    g.conn = engine.connect()
    Session = scoped_session(sessionmaker(bind=engine))
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
    return render_template('index.html')

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another
#
# notice that the functio name is another() rather than index()
# the functions for each app.route needs to have different names
#
@app.route('/another')
def another():
  return render_template("anotherfile.html")


# Example of adding new data to the database
#@app.route('/add', methods=['POST'])
#def add():
  #name = request.form['name']
  #g.conn.execute('INSERT INTO test VALUES (NULL, ?)', name)
  #return redirect('/')


@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        q = "SELECT USERNAME FROM USERS U WHERE U.USERNAME = :u;"
        s = Session()
        result = s.execute(q, {'u':form.username.data})
        rows = result.fetchall()
        if len(rows) == 0:
            q1 = "INSERT INTO USERS VALUES (:a, :b, :c, :d, :e)"
            s.execute(q1, {'a':form.username.data, 'b':form.name.data,
                'c':form.password.data, 'd':form.contact_info.data, 
                'e':form.description.data})
            s.commit()
            return redirect(url_for('home', username=form.username.data))
        else:
            flash('Username already taken')
    return render_template('createaccount.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        s = Session()
        q = "SELECT PASSWORD FROM USERS U WHERE U.USERNAME = :u"
        result = s.execute(q, {'u':form.username.data})
        rows = result.fetchall()
        if len(rows) == 0:
            flash('Account not found')
            return render_template('error.html')
        password = rows[0]
        if password[0] == form.password.data:
            flash('Logged in')
            return redirect(url_for('home', username=form.username.data))
        else:
            flash('Incorrect password')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/home/<username>')
def home(username):
    return render_template('homepage.html', username=username)

@app.route('/createsession/<username>', methods=['GET', 'POST'])
def create_session(username):
    form = CreateSessionForm()
    if form.validate_on_submit():
        s = Session()
        q = "insert into sessions values (:u, NULL, :a, :b, :c, :d, :e)"
        s.execute(q, {'u':username, 'a':form.title.data, 'b':form.start_time.data, 
            'c':form.length.data, 'd':form.location.data, 'e':form.description.data})
        s.commit()
        return redirect(url_for('home', username=username))
    return render_template('createsession.html', form=form)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = '1234567890'
    app.run(host=HOST, port=PORT, debug=True, threaded=threaded)


  run()
