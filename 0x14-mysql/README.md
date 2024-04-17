#                 0x14. MySQL


1, First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
* sudo apt install mysql-server
* sudo systemctl start mysql.service
* sudo systemctl start mysql.service

2, Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn
* CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
* GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

3, In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
* CREATE DATABASE tyrell_corp; USE tyrell_corp; 丶CREATE TABLE nexus6 (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL
 ); INSERT INTO nexus6 (name) VALUES ('Leon');
* INSERT INTO nexus6 (name) VALUES ('Leon');

4, Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.
The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
* CREATE USER 'replica_user'@'%' IDENTIFIED BY ‘your_password’;
* GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'slave_host' IDENTIFIED BY 'your_password';
* GRANT SELECT ON mysql.user TO 'holberton_user'@'your_host';

5, Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

. MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
. Edit the MySQL configuration file on web-01
* sudo vin /etc/mysql/mysql.conf.d/mysqld.cnf
* [mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp

sudo systemctl restart mysql
sudo mysql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'%';
FLUSH PRIVILEGES;


. Edit Replica Server (web-02)
* sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
* Add line
[mysqld]
server-id = 2
relay-log = /var/log/mysql/mysql-relay-bin.log
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp


sudo systemctl restart mysql
sudo mysql
CHANGE MASTER TO MASTER_HOST='web-01', MASTER_USER='replica_user', MASTER_PASSWORD='your_password', MASTER_LOG_FILE='mysql-bin.000009', MASTER_LOG_POS=107;
START SLAVE;
