
CREATE USER 'holberton_user'@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@localhost;
GRANT SELECT on mysql.user TO 'holberton_user'@'localhost';

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
| mydql-bin.000001 |      154 |