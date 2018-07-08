import mysql.connector as sql

#       QUESTION 1

con = sql.connect(user='root', password='123', host='localhost', database='assignment')
cur = con.cursor()

cur.execute("CREATE TABLE ZIPCODES (ZIPCodeID INT NOT NULL PRIMARY KEY, ZIPCode INT, State VARCHAR(100), City VARCHAR(100))")
cur.execute("CREATE TABLE PUBLISHERS (PublisherID INT NOT NULL PRIMARY KEY, Name VARCHAR(100), StAdd VARCHAR(100), SuiteNo INT, ZIPCodeID INT, FOREIGN KEY (ZIPCodeID) REFERENCES ZIPCODES (ZIPCodeID))")
cur.execute("CREATE TABLE AUTHORS (AuthorID INT NOT NULL PRIMARY KEY, FirstName VARCHAR(100), MiddleName VARCHAR(100), LastName VARCHAR(100))")
cur.execute("CREATE TABLE TITLES (TitleID INT NOT NULL PRIMARY KEY, Title VARCHAR(100), ISBN VARCHAR(100), PublisherID INT, PublicationYear INT, FOREIGN KEY (PublisherID) REFERENCES PUBLISHERS (PublisherID))")
cur.execute("CREATE TABLE BOOK (BookID INT NOT NULL PRIMARY KEY, TitleID INT, Location VARCHAR(100), Genre VARCHAR(100), FOREIGN KEY (TitleID) REFERENCES TITLES (TitleID))")
cur.execute("CREATE TABLE AUTHORS_TITLES (AuthorTitleID INT NOT NULL PRIMARY KEY, TitleID INT, AuthorID INT, FOREIGN KEY (AuthorID) REFERENCES AUTHORS (AuthorID))")


#       QUESTION 2

cur.execute("INSERT INTO ZIPCODES VALUES(1, 11, 'J&K', 'Srinagar');")
cur.execute("INSERT INTO ZIPCODES VALUES(2, 22, 'WB', 'Siliguri');")
cur.execute("INSERT INTO ZIPCODES VALUES(3, 33, 'MP', 'Bhopal');")
cur.execute("INSERT INTO PUBLISHERS VALUES(100, 'RK', 'Mumbai', 12, 1);")
cur.execute("INSERT INTO PUBLISHERS VALUES(101, 'Rohit Mehra', 'Sikkim', 13, 2);")
cur.execute("INSERT INTO PUBLISHERS VALUES(102, 'Babu Rao', 'Delhi', 13, 3);")
cur.execute("INSERT INTO AUTHORS VALUES(007, 'Dan', '', 'Brown');")
cur.execute("INSERT INTO AUTHORS VALUES(008, 'J', 'K', 'Rowling');")
cur.execute("INSERT INTO AUTHORS VALUES(009, 'Vikram', '', 'Chandra');")
cur.execute("INSERT INTO TITLES VALUES(999, 'Inferno', 'ABC123456', 100, 2012);")
cur.execute("INSERT INTO TITLES VALUES(998, 'Harry Potter', 'ABC123459', 101, 1998);")
cur.execute("INSERT INTO TITLES VALUES(997, 'Sacred Games', 'ABC123480', 103, 2006);")
cur.execute("INSERT INTO BOOK VALUES(45, 999, 'Florence', 'Thriller');")
cur.execute("INSERT INTO BOOK VALUES(46, 998, 'Hogwarts', 'Fantasy');")
cur.execute("INSERT INTO BOOK VALUES(47, 997, 'Mumbai', 'Crime-Thriller');")
cur.execute("INSERT INTO AUTHORS_TITLES VALUES(7, 999, 007);")
cur.execute("INSERT INTO AUTHORS_TITLES VALUES(8, 998, 008);")
cur.execute("INSERT INTO AUTHORS_TITLES VALUES(6, 997, 009);")
con.commit()


#       QUESTION 3

cur.execute("UPDATE BOOK SET Location = 'Bombay' WHERE BookID = 47;")
con.commit()
cur.execute("SELECT * FROM BOOK;")
cur.fetchall()
cur.close()
con.close()
