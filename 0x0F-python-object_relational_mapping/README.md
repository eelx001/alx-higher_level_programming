# 0x0F. Python - Object-relational mapping
In this project, I learned about how object-relational mapping is used for database scripting. I became familiar with using MySQLdb and SQLAlchemy to query, create, edit, and delete tables in MySQL.

# Before you start…
Please make sure your MySQL server is in 8.0 -> [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/elyse502/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/README.md)

# Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

# Resources🏗️
### Read or watch:
* [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (_please don’t pay attention to `_mysql`_)
* [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
* [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
* [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
* [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
* [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (_**Warning**: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL_)
* [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
* [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

# General🧵
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

# Requirements
## General
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* You are not allowed to use `execute` with sqlalchemy

# More Info
## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install `MySQLdb` module version `2.0.x`
For installing `MySQLdb`, you need to have `MySQL` installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/elyse502/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/README.md)
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient  -->| Remove sudo if it fails to install..... 
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
## Install `SQLAlchemy` module version `1.4.x`
```
$ sudo pip3 install SQLAlchemy  -->| Remove sudo if it fails to install.....
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
#### Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)
```
You can ignore it.

# Tasks 📃
## 0. Get all states: [0-select_states.py](0-select_states.py)
A script that lists all `states` from the database `hbtn_0e_0_usa`:
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**

## 1. Filter states: [1-filter_states.py](1-filter_states.py)
A script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$
```
**No test cases needed**

## 2. Filter states by user input: [2-my_filter_states.py](2-my_filter_states.py)
A script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You must use `format` to create the SQL query with the user input
* Results must be sorted in ascending order by `states.id`
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**

## 3. SQL Injection...: [3-my_safe_filter_states.py](3-my_safe_filter_states.py)
Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?
```
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$
```
What? Empty?

Yes, it’s an [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
































