-- Create a new user for the ALX Checker
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
       IDENTIFIED WITH mysql_native_password
       BY 'projectcorrection280hbtn';
-- Grant replication privilages for the holberton user
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
