#Q1.
import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute("""CREATE TABLE BOOKS IF NOT EXIST(book_id varchar(20),title str(10
            ),genre str(10)""")#3 quotes is called doc string which is used to write multiple lines wihtout special breaks
c.execute("""CREATE TABLE TITLES IF NOT EXIST(ISBN int(20),title_str(10
            ),publisher_id(10),publication year_int(6)""")
c.execute("""CREATE TABLE PUBLISHERS IF NOT EXIST(name str(20),street address varchar(10
            ),zipcode id int(10)""")
c.execute("""CREATE TABLE ZIPCODES IF NOT EXIST(city_str(20),state_str(10
            ),zipcode_int(10)""")
c.execute("""CREATE TABLE AUTHORS TITLES IF NOT EXIST(author_id varchar(20),title_str(10
            )""")
c.execute("""CREATE TABLE AUTHORS IF NOT EXIST(first_name str(20),middle_name str(10
            ),last_name str(10))""")
conn.commit()
conn.close()

#Q2.

c.execute("INSERT INTO BOOKS VALUES(467213,'the blue umbrella','drama')")
c.execute("INSERT INTO TITLES VALUES(3563423,'the blue umbrella',5613456123,1993)")
c.execute("INSERT INTO PUBLISHERS VALUES('Ruskin bond','Ivy Cottage , Landour defence colony, near Domo's cafe',67666)")
c.execute("INSERT INTO ZIPCODES VALUES('mussorie','uttrakhand',67666)")
c.execute("INSERT INTO AUTHOR TITLES VALUES(8907889,'the blue umbrella')")
c.execute("INSERT INTO AUTHORS VALUES('Ruskin','','bond')")

conn.commit()
conn.close
