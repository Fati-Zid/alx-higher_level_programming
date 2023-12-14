Certainly! Here's a highlighted version of the tasks:

```markdown
# 0x0D. SQL - Introduction

## Author
Fati-Zid

## Introduction
This repository contains SQL scripts that demonstrate various database operations. The scripts are designed to be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25). The tasks cover fundamental SQL operations, such as creating and deleting databases, listing tables, and performing CRUD operations on tables.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e., syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)

### Installation of MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connect to MySQL server
```bash
$ sudo mysql
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.
...
mysql> quit
Bye
```

### Use "container-on-demand" to run MySQL
- In the container, credentials are root/root
- Ask for a container with Ubuntu 20.04
- Connect via SSH or connect via the Web terminal
- In the container, start MySQL before interacting with it:
```bash
$ service mysql start
 * Starting MySQL database server mysqld
```

## Tasks
1. **List Databases**
   - Write a script that lists all databases of your MySQL server.
   ```bash
   $ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
   ```

2. **Create a Database**
   - Write a script that creates the database `hbtn_0c_0` in your MySQL server.
   ```bash
   $ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
   ```

3. **Delete a Database**
   - Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
   ```bash
   $ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
   ```

4. **List Tables**
   - Write a script that lists all the tables of a database in your MySQL server.
   ```bash
   $ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
   ```
   <!-- Additional tasks are omitted for brevity -->
```
