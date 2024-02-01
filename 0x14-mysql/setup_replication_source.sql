-- Create a new user for the ALX Checker
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
       IDENTIFIED WITH mysql_native_password
       BY 'projectcorrection280hbtn';
-- Grant replication privilages for the holberton user
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
-- Grant Select on mysql.user table for the holberton user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
-- Creat replication database
CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- Grant Select permission for holberton user on this databse
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';

-- Create a new user for the replication
CREATE USER IF NOT EXISTS 'replica_user'@'%'
       IDENTIFIED WITH mysql_native_password
       By '1234567890';
-- Grant replication premission for the replica_user
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

-- Create a new table nexus6 on tyrell_corp replication database
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(32),
       last_name VARCHAR(32)
       );
-- Insert a record to this table
INSERT INTO nexus6 (first_name, last_name) values (
       'Mojtaba',
       'Babiker'
       );
