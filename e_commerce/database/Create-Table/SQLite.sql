 CREATE TABLE "Users" (
  "First_Name" TEXT NOT NULL,
  "Last_Name" TEXT NOT NULL,
  "Username" TEXT NOT NULL,
  "Password" TEXT NOT NULL,
  "User_ID" INTEGER NOT NULL,
  PRIMARY KEY("USER_ID")
  );
  
  CREATE TABLE "Payment_Info" (
  "Payment_ID" INTEGER NOT NULL,
  "User_ID" INTEGER NOT NULL,
  "Payment_Type" TEXT NOT NULL,
  "Card_Number" INTEGER NOT NULL,
  "CVV" INTEGER NOT NULL,
  "Address_Line_1" TEXT NOT NULL,
  "Address_Line_2" TEXT NOT NULL,
  "City" TEXT NOT NULL,
  "State" TEXT NOT NULL,
  "Zip_Code" INTEGER NOT NULL,
  "Phone_Number" INTEGER NOT NULL,
  PRIMARY KEY("Payment_ID")
  );
  
  CREATE TABLE "Shipping_Info" (
  "Shipping_ID" INTEGER NOT NULL,
  "User_ID" INTEGER NOT NULL,
  "Address_Line_1" TEXT NOT NULL,
  "Address_Line_2" TEXT NOT NULL,
  "City" TEXT NOT NULL,
  "State" TEXT NOT NULL,
  "Zip_Code" INTEGER NOT NULL,
  "Phone_Number" INTEGER NOT NULL,
  PRIMARY KEY("Shipping_ID")
  );
   
 
 CREATE TABLE User_History (
  ISBN varchar(14) NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  User_ID INTEGER NOT NULL,
  Quantity INTEGER NOT NULL,
  Price INTEGER NOT NULL
  );

CREATE TABLE Cart (
  ISBN varchar(14) NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  User_ID INTEGER NOT NULL,
  Quantity INTEGER NOT NULL,
  Price INTEGER NOT NULL
  );
 
 cREATE TABLE Inventory (
  ISBN varchar(14) NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  Quantity INT,
  Price INT,
  PRIMARY KEY(ISBN)
  );

INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-0451524935', 'First Book', 'George Orwell', '1949', 'Dystopian', 100, 15);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-0446310789', 'Mockingbird', 'Harper Lee', '1960', 'Southern Gothic', 100, 25);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-0156028356', 'The Color Purple', 'Alice Walker', '1982', 'Epistolary', 100, 20);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-1400033416', 'Beloved', 'Toni Morrison', '1987', 'American Literature', 100, 15);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-1501156748', 'Misery', 'Stephen King', '1987', 'Psychological Horror', 100, 30);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-0312424404', 'Gilead', 'Marilynne Robinson', '2004', 'Novel', 100, 20);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
('978-0307265432', 'The Road', 'Cormac McCarthy', '2006', 'Post apocalyptic fiction', 3, 20);