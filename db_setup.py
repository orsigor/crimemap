import pymysql
import dbconfig

connection=pymysql.connect(host='127.0.0.1',user=dbconfig.db_user,passwd=dbconfig.db_password)

try:
	with connection.cursor() as cursor:
		sql=""""create table if not exists crimemap.crimes(
			id int not null auto_increment,
			latitude FLOAT(10,6),
			longitude FLOAT(10,6),
			date DATETIME,
			category VARCHAR(50),
			description VARCHAR(1000),
			updated_at TIMESTAMP,
			PRIMARY  KEY (id))
		    """
		cursor.execute(sql)
	connection.commit()
finally:
	connection.close()


