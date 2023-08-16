# 0x0D. SQL - Introduction
This was my first project in which I began to work with SQL and relational databases. I began practicing introductory data definition and data manipulation language, making subqueries, and using functions.

# Concepts
_For this project, we expect you to look at these concepts:_
* [Databases](https://intranet.alxswe.com/concepts/37)
* [Databases](https://intranet.alxswe.com/concepts/556)

![rtcwz](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/e619f37b-b99b-4a4f-8aa6-6dd3a06fd5e6)

# Databases
### What are databases?
First, what are databases for?

Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

Then, why not store your data in flat files, as you did in the “Relational databases, done wrong” project? A solid database is expected to be acid, which means it guarantees:
* **A**tomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
* **C**onsistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
* **I**solation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
* **D**urability: unplug your server at any time, boot it back up, and it didn’t lose any data.

Also, a solid database will provide strong performance (because I/O is your bottleneck and databases are I/O, so their performance makes a whole lot more of a difference than the performance of your application’s code) and scalability (inserting one user in a collection of 5 users should take about the same time as inserting one user in a collection of 5 billion users).

## ACID is a cool acronym! CRUD is another cool one
You will definitely run into the concept of “CRUD” operations. It’s just a fancy way to refer to the 4 operations that can be performed on the data itself:
* **C**reate some data;
* **R**ead some data;
* **U**pdate some data;
* **D**estroy some data.

Obviously, a database should allow all four. Yes, that’s it.

## 2+ kinds of databases
When people talk about databases, they’re usually referring to **relational databases** (such as PostgreSQL, MySQL, Oracle, …); but there are many other kinds of databases used in the industry, which are globally referred to as **“NoSQL” databases**, even though they can be very different from each other, and serve very various purposes. Also, the name “NoSQL” comes from **SQL**, which is the name of the syntax used to give orders (CRUD operations, creating and deleting tables, …) to a relational databases; however, some non-relational databases, which are referred to as “NoSQL” give the option to use the SQL syntax. Therefore, the term “NoSQL” is quite controversial to refer to non-relational databases, but it is still widely used.

“NoSQL” (non-relational) databases have known a boost in popularity, over the last decade or so, so much that there was a point, a few years ago, where people were wondering if they were to replace relational databases entirely. But years later, the market has now solidified, NoSQL databases’ market share doesn’t progress much anymore and is now quite steady. The result: many NoSQL databases have made it into solid maturity, and are used in some very ambitious projects (as well as small ones), but relational databases are still by far the most used in projects, and are not going anywhere after all.

Therefore: it is crucial for a software engineer to know very well how relational databases work, because the odds are very strong that you will encounter them in your career; but it is also very important to get acquainted with the most popular types of NoSQL databases, because the odds that you run into them, however kinda smaller, are pretty strong too.

## SQL
In order to work with relational databases, you will need to get familiar with SQL syntax. A lot of developers will acknowledge that they find the SQL syntax unpleasantly hard to use, which has some outcomes:

* Engineers that are comfortable with SQL are very respected in the industry, even more so in this age where data has gotten so valuable. To be honest, the fact that I aced the SQL challenge on my Apple interview is probably a huge reason for me to have gotten the job; it turns out the initial role was a lot about manipulating data.
* The fear of SQL explains a lot why non-relational databases got called “NoSQL”, a bit like if it was a statement, a complain. Non-relational databases push a lot the button of not having to use SQL.
* Modern full-fledged frameworks contain tools that are called ORMs, and one of their roles is to abstract away SQL queries (which is good for day-to-day ease of use, but [can turn out very dangerous](https://github.com/gmile/gmile.github.io/blob/master/_posts/2016-02-01-raw-sql-in-a-rails-project.md)). We’ll cover ORMs more later, but it’s worth noting that you do find back-end engineers in the industry who work with relational databases, but never write a line of SQL, which makes them a lot less valuable on a project.
* For a beginner, keep in mind that SQL’s syntax is a bit hard to wrap your head around, so maybe you should follow a tutorial first. Please don’t try to memorize the SQL syntax. I’ve used SQL extensively in very advanced cases, on systems with hundreds of millions of records, and I still go on Google each time I need to compose a SQL query.

## Some terminology around relational databases
One good thing about relational databases is that whether they’re PostgreSQL, MySQL, Oracle, or other, they’ve managed to be pretty consistent across brands. Therefore, not only are their versions of SQL pretty decently similar (at least for CRUD operations), but the terminology they’re using are mostly the same.

Say you need to store users. To do that, you create a table that is called “users”.

Your users have 3 pieces of information to store: their “id”, their “login”, and their “password”. Those are called columns, and they all have types, like integer for the “id”, varchar(32) for “login” (a string of variable length, but maximum 32), and char(32) (a string of exactly 32 characters, which is the case for all text encrypted with the md5 algorithm, for instance). The available types may vary heavily from one database “brand” to the other.

Now, let’s add a user in the database with SQL:
```
INSERT INTO users (login, password) VALUES ('rudy', '01234567890123456789012345678901');
```
This adds a **row** in the table (sometimes also refered to as a **record**, or more rarely, a **tuple**).
## Why are they called “relational” databases?
Historically, the initial reason was that tables used to be called “relations” (they gather a lot of datas that are “related” to each other, since they follow the same structure). However, tables are now tables, and the term “relation” has now been recycled for another use.

A **relation** as used today is something that ties two records together, most often across different tables. For instance, say you have a blog, and you have 2 tables:
* posts, with the fields id, title and body
* comments, with the fields id and body

In both tables, the “id” fields are **primary keys**, because they uniquely identify the row that they belong to (if you say “give me the post of id 4”, you’re sure to be getting only one post).

But how do you know that a given comment is attached to a given post. Well, you add a postid field to the comments table, containing the id of the post you with to attach it to. The postid field is called a **foreign key**, uniquely identifying another’s table primary key.

Now that you have that, you can easily identify, from a comment, which post it is attached to; but you can also easily identify, from a post, which comments are attached to it. Just fetch the comments whose post_id field contain the id of the post you had in mind. The fact that you can do that is what is called a relation.

Once you have your relation, you can do pretty advanced things. For instance, you can join tables together while querying them, which will allow you to search for “the comments whose posts were published within the last month”, for instance (well, provided the posts table has a published_at column of type date, for instance).

Note: you can have a relation between rows of the same table, for instance, a user that is the “sponsor” of another one, a comment that is a “reply” of another one, …

## Some more terminology around relational databases
### Indexes
Say you want to get all of the comments that are attached to the post of ID 12:
```
SELECT * FROM comments WHERE post_id=12;
```
If you have millions or billions of comments, having your database extract the comments that match this condition can be amazingly time-consuming. Therefore, you can add an index on the comments table, that applies to the post_id column. This will “precompute” every possible SELECT query with WHERE conditions on this column, which will update themselves every time you modify data, so that those calls are ready to respond very quickly.

Let’s complicate things a bit, and say you want to optimize this query:
```
SELECT * FROM comments WHERE post_id=12 AND published=1;
```
Your index on the post_id column might not help much on that query. However, for that query, you can absolutely define an index on multiple column (in this case, the columns post_id and published).

Setting indexes properly is a known quick win to improve performance of relational databases on queries that are performed very often and take a long time to respond (so-called slow queries). I can quote at least a dozen occurrences in my career where setting up an index properly boosted a database’s performance with minimal effort, the most notable of which allowed us to boost a data migration that was taking ~48 hours, to suddenly complete in about 3 hours.

## Joins
You can join tables together that have relations between each other, so that you can operate on data across those tables. For instance, I want the titles of all posts that have published comments.
```
SELECT posts.title FROM posts JOIN comments ON posts.id = comments.post_id WHERE comments.published=1;
```
(Note: each post on that query will appear as many times as it has comments, but let’s focus on the join for now.)

Performance is dramatically better if you manage to get the database to do most of the work, as opposed to your application, because the database knows most about your data and how to handle it most efficiently. Joins are amazing wins for that, because the other way to get it done is to perform many separate SQL queries, and manipulate that data in your code, which is very inefficient.

Note: you can join tables together across many relations. The largest join in my career was 7-fold, in a database at Apple that contained information about localization projects.

## A NoSQL kind of database: document-based databases
One particularly popular type of NoSQL database is document-oriented databases, such as MongoDB or CouchDB. One reason they’re popular is because their learning curve is very smooth, and they feel natural to use: you just send them JSON documents, much like we’ve done in the “Relational databases done wrong” project, and they make it right when you need to fetch them back. You don’t need your JSON documents to have specific fields of specific types, just send whatever JSON you want; the technical word for this is that they are schemaless.

One caveat is that they’re much, much harder to scale than relational databases (the data being more “formatted” in relational databases makes it easier and faster to work with).

Another caveat is that there is some comfort in having the database enforcing a schema (proper columns of proper types, …); if the database doesn’t do it, you can expect that some JSON documents in the collection are not of the schema you expect, and then you have to enforce schema in your code, which means more work. As a result, some document-based databases offer ways to enforce some schema, but I don’t believe many developers use it, because it defeats the purpose of having schemaless storage.

Just as relational databases, document-based databases offer a variety of extra features to tune your usage of the data: indexes, joins, … sometimes even relations!

Document-based databases will be covered towards the end of year 1.

## Another NoSQL kind of database: key-value stores
Some applications may need very large key-value storage, which you may think of as the persistence of a single huge “dictionary” structure (the same structure that Ruby calls “hash”, Python calls “dict”, PHP calls “associative array”, Objective C and Swift calls “dictionary”, …). An obvious need for that is around caching (if you don’t understand why, we’ll cover this when we talk about caching). Cassandre, memcached and Redis are popular key-value stores.

As your collection of key-values grows, you may need pretty advanced ways to organize them (and expire them, for instance), so, obviously, each key-value storage solution comes with more advanced tools than just the usual CRUD operations.

## At the intersection of NoSQL and relational
As mentioned before, NoSQL databases sometimes get closer to relational databases by allowing to be queried using the SQL syntax (like Cassandra and Hypertable); but databases are getting closer also the other way around, as relational databases themselves have started offering some document-based storage.

A mature example of that is PostgreSQL’s “hstore” type, which allows to store JSON data in PostgreSQL, in a way that is queriable. Most recently, this has allowed PostgreSQL to have a certain leg up against their competition of open-source relational databases, because MySQL hasn’t been able to ship a similar feature yet, although they’re expected too (MySQL development has dramatically slowed down now that they belong to Oracle, which is a direct closed-source competitor; a few years ago, most MySQL contributors went ahead to create another open-source database called MariaDB, which never really became mainstream, so maybe there won’t ever be document-based storage in MySQL, actually).

## What NoSQL storage do I need?
NoSQL databases address all kinds of requirements, and therefore the ways they work are dramatically different. Here’s a really accurate map of the various solutions: http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis

Note: in year 1, your main project must be done using a relational database, and we’ll cover document-oriented databases (probably MongoDB) and key-value stores (probably Redis) towards the end of the year.

# Resources🧵
### Read or watch:
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php) (_no need to read the chapter “Privileges”_)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

# General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does `DDL` and `DML` stand for
* How to `CREATE` or `ALTER` a table
* How to `SELECT` data from a table
* How to `INSERT`, `UPDATE` or `DELETE` data
* What are `subqueries`
* How to use MySQL functions

# More Info
### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
### Use “container-on-demand” to run MySQL
**In the container, credentials are** `root/root`
* Ask for container `Ubuntu 20.04`
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
In the container, credentials are `root/root`

# Tasks 📃
## 0. List databases: [0-list_databases.sql](0-list_databases.sql)
A script that lists all databases of your MySQL server.
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```
## 1. Create a database: [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
A script that creates the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
```
## 2. Delete a database: [2-remove_database.sql](2-remove_database.sql)
A script that deletes the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` doesn’t exist, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```
## 3. List tables: [3-list_tables.sql](3-list_tables.sql)
A script that lists all the tables of a database in your MySQL server.
* The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)
```
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$
```
## 4. First table: [4-first_table.sql](4-first_table.sql)
A script that creates a table called `first_table` in the current database in your MySQL server.
* `first_table` description:
    * `id` INT
    * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```
## 5. Full description: [5-full_table.sql](5-full_table.sql)
A script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements
```
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$
```
## 6. List all in table: [6-list_values.sql](6-list_values.sql)
A script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* All fields should be printed
* The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```
## 7. First add: [7-insert_value.sql](7-insert_value.sql)
A script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
* New row:
  * `id` = `89`
  * `name` = `Best School`
* The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
```
## 8. Count 89: [8-count_89.sql](8-count_89.sql)
A script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
* The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$
```
## 9. Full creation: [9-full_creation.sql](9-full_creation.sql)
A script that creates a table ``second_table`` in the database ``hbtn_0c_0`` in your MySQL server and add multiples rows.
* ``second_table`` description:
   * ``id`` INT
   * ``name`` VARCHAR(256)
   * ``score`` INT
* The database name will be passed as an argument to the ``mysql`` command
* If the table ``second_table`` already exists, your script should not fail
* You are not allowed to use the ``SELECT`` and ``SHOW`` statements
* Your script should create these records:
   * ``id`` = 1, ``name`` = “John”, ``score`` = 10
   * `id` = 2, ``name`` = “Alex”, ``score`` = 3
   * `id` = 3, ``name`` = “Bob”, ``score`` = 14
   * `id` = 4, ``name`` = “George”, ``score = 8``
```
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```
## 10. List by best: [10-top_score.sql](10-top_score.sql)
A script that lists all records of the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the ``mysql`` command
```
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```
## 11. Select the best: [11-best_score.sql](11-best_score.sql)
A script that lists all records with a ``score >= 10`` in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```
## 12. Cheating is bad: [12-no_cheating.sql](12-no_cheating.sql)
A script that updates the score of Bob to `10` in the table ``second_table``.
* You are not allowed to use Bob’s id value, only the ``name`` field
* The database name will be passed as an argument of the ``mysql`` command
```
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```
## 13. Score too low: [13-change_class.sql](13-change_class.sql)
A script that removes all records with a ``score <= 5`` in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* The database name will be passed as an argument of the ``mysql`` command
```
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```
## 14. Average: [14-average.sql](14-average.sql)
A script that computes the score average of all records in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* The result column name should be ``average``
* The database name will be passed as an argument of the ``mysql`` command
```
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$
```
## 15. Number by score: [15-groups.sql](15-groups.sql)
A script that lists the number of records with the same score in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* The result should display:
   * the ``score``
   * the number of records for this ``score`` with the label ``number``
* The list should be sorted by the number of records (descending)
The database name will be passed as an argument to the ``mysql`` command
```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$
```
## 16. Say my name: [16-no_link.sql](16-no_link.sql)
A script that lists all records of the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.
* Don’t list rows without a ``name`` value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the ``mysql`` command

In this example, new data have been added to the table ``second_table``.
```
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```
## 17. Go to UTF8: [100-move_to_utf8.sql](100-move_to_utf8.sql)
A script that converts ``hbtn_0c_0`` database to UTF8 (``utf8mb4``, collate ``utf8mb4_unicode_ci``) in your MySQL server.

You need to convert all of the following to ``UTF8``:
* Database ``hbtn_0c_0``
* Table ``first_table``
* Field ``name`` in ``first_table``
```
guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$
```
## 18. Temperatures #0: [101-avg_temperatures.sql](101-avg_temperatures.sql)
Import in hbtn_0c_0 database this table dump: **`download`**

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
```
guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 
```
## 19. Temperatures #1: [102-top_city.sql](102-top_city.sql)
Import in `hbtn_0c_0` database this table dump: **`download`** (same as `Temperatures #0`)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
```
guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$
```
## 20. Temperatures #2: [103-max_state.sql](103-max_state.sql)
Import in `hbtn_0c_0` database this table dump: ** `download`** (same as `Temperatures #0`)

Write a script that displays the max temperature of each state (ordered by State name).
```
guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$
```





