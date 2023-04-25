CREATE TABLE "Cart" (
  "Item_ID" INTEGER NOT NULL,
  "Item_Name" TEXT NOT NULL,
  "User_ID" INTEGER NOT NULL,
  "Quantity" INTEGER NOT NULL,
  "Price" INTEGER NOT NULL
  );
 
 CREATE TABLE "Users" (
  "First_Name" TEXT NOT NULL,
  "Last_Name" TEXT NOT NULL,
  "Username" TEXT NOT NULL,
  "Password" TEXT NOT NULL,
  "User_ID" INTEGER NOT NULL,
  PRIMARY KEY("USER_ID")
  );
  
  CREATE TABLE "Inventory" (
  "Item_ID" INTEGER NOT NULL,
  "Item_Name" TEXT NOT NULL,
  "Item_Count" INTEGER NOT NULL,
  "Price" INTEGER NOT NULL,
  "Genre" TEXT NOT NULL,
  PRIMARY KEY("Item_ID")
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
  
  
  