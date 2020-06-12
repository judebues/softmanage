mysqldump -uroot -p121511 mshd | gzip > /home/backup/mshd_$(date+%Y%m%d_%H%M%S).sql.gz
