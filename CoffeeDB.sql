BEGIN TRANSACTION;
DROP TABLE IF EXISTS "User";
CREATE TABLE IF NOT EXISTS "User" (
	"UserID"	INTEGER,
	"email"	TEXT,
	"password"	TEXT,
	"fullname"	TEXT,
	PRIMARY KEY("UserID")
);
DROP TABLE IF EXISTS "ProcessingMethod";
CREATE TABLE IF NOT EXISTS "ProcessingMethod" (
	"ProcessingMethodID"	INTEGER,
	"name"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("ProcessingMethodID")
);
DROP TABLE IF EXISTS "BeanInBatch";
CREATE TABLE IF NOT EXISTS "BeanInBatch" (
	"BatchID"	INTEGER NOT NULL,
	"BeanID"	INTEGER NOT NULL,
	FOREIGN KEY("BeanID") REFERENCES "Bean"("BeanID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("BatchID") REFERENCES "Batch"("BatchID") ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS "Farm";
CREATE TABLE IF NOT EXISTS "Farm" (
	"FarmID"	INTEGER,
	"masl"	NUMERIC,
	"region"	TEXT,
	"country"	TEXT,
	"name"	TEXT,
	PRIMARY KEY("FarmID")
);
DROP TABLE IF EXISTS "Bean";
CREATE TABLE IF NOT EXISTS "Bean" (
	"BeanID"	INTEGER,
	"name"	TEXT,
	"species"	TEXT,
	"FarmID"	INTEGER NOT NULL,
	PRIMARY KEY("BeanID"),
	FOREIGN KEY("FarmID") REFERENCES "Farm"("FarmID") ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS "Batch";
CREATE TABLE IF NOT EXISTS "Batch" (
	"BatchID"	INTEGER,
	"harvestyear"	NUMERIC,
	"priceperkilo"	NUMERIC,
	"ProcessingMethodID"	INTEGER NOT NULL,
	"FarmID"	INTEGER NOT NULL,
	FOREIGN KEY("FarmID") REFERENCES "Farm"("FarmID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("ProcessingMethodID") REFERENCES "ProcessingMethod"("ProcessingMethodID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("BatchID")
);
DROP TABLE IF EXISTS "Post";
CREATE TABLE IF NOT EXISTS "Post" (
	"PostID"	INTEGER,
	"tastingnotes"	TEXT,
	"tastingdate"	NUMERIC,
	"UserID"	INTEGER NOT NULL,
	"CoffeeID"	INTEGER NOT NULL,
	"points"	INTEGER,
	FOREIGN KEY("CoffeeID") REFERENCES "Coffee"("CoffeeID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("UserID") REFERENCES "User"("UserID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("PostID")
);
DROP TABLE IF EXISTS "Coffee";
CREATE TABLE IF NOT EXISTS "Coffee" (
	"CoffeeID"	INTEGER,
	"roastdegree"	TEXT,
	"roasteddate"	NUMERIC,
	"name"	TEXT,
	"description"	TEXT,
	"priceperkilo"	NUMERIC,
	"roastery"	INTEGER,
	"BatchID"	INTEGER NOT NULL,
	FOREIGN KEY("BatchID") REFERENCES "Batch"("BatchID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("CoffeeID")
);
INSERT INTO "User" ("UserID","email","password","fullname") VALUES (1,'adrianfauske@gmail.com','banan','Adrian Nasir Fauske');
INSERT INTO "User" ("UserID","email","password","fullname") VALUES (2,'williarh@stud.ntnu.no','eple','William Strand Hassel');
INSERT INTO "User" ("UserID","email","password","fullname") VALUES (3,'kraemer@ntnu.no','123','Frank Alexander Kraemer');
INSERT INTO "User" ("UserID","email","password","fullname") VALUES (4,'test','test','Test Testesen');
INSERT INTO "ProcessingMethod" ("ProcessingMethodID","name","description") VALUES (1,'washed','The coffee is washed');
INSERT INTO "ProcessingMethod" ("ProcessingMethodID","name","description") VALUES (2,'natural','The coffee is natural');
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (1,1);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (2,2);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (3,2);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (3,3);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (4,4);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (4,1);
INSERT INTO "BeanInBatch" ("BatchID","BeanID") VALUES (5,5);
INSERT INTO "Farm" ("FarmID","masl","region","country","name") VALUES (1,1500,'Santa Ana','El Salvador','Nombre de Dios');
INSERT INTO "Farm" ("FarmID","masl","region","country","name") VALUES (2,2100,'Caldas','Colombia','Don Eduardo');
INSERT INTO "Farm" ("FarmID","masl","region","country","name") VALUES (3,600,'Kigali','Rwanda','Rwanda Farmers Coffee Company');
INSERT INTO "Bean" ("BeanID","name","species","FarmID") VALUES (1,'Bourbon','c. Arabica',1);
INSERT INTO "Bean" ("BeanID","name","species","FarmID") VALUES (2,'Typica','c. Arabica',1);
INSERT INTO "Bean" ("BeanID","name","species","FarmID") VALUES (3,'Bourbon','c. Arabica',2);
INSERT INTO "Bean" ("BeanID","name","species","FarmID") VALUES (4,'Robusta','c. Robusta',2);
INSERT INTO "Bean" ("BeanID","name","species","FarmID") VALUES (5,'Liberica','c. Liberica',3);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (1,2021,8,2,1);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (2,2020,10,1,1);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (3,2021,7,1,2);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (4,2022,15,2,2);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (5,2019,8,1,3);
INSERT INTO "Batch" ("BatchID","harvestyear","priceperkilo","ProcessingMethodID","FarmID") VALUES (6,2022,12,2,3);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (1,'floral','10.3.2022',1,1,10);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (2,'bland','11.3.2022',1,3,5);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (3,'amazing','07.02.2022',2,5,9);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (4,'floral','2022-03-25',4,1,7);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (5,'banan','2022-03-25',4,6,8);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (6,'Wow - an odyssey for the taste buds: citrus peel, milk chocolate, apricot!','2022-03-25',1,1,10);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (1,'light','20.01.2022','Vinterkaffe 2022','A tasty and complex coffee for polar nights',600,'Jacobsen & Svart',1);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (2,'medium','11.11.2021','Sommersolsverv','A floral yet spicy medium roast for summer nights',500,'Jacobsen & Svart',2);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (3,'light','25.03.2022','Vårrengjøring 2022','A caramelly and strongly flavored coffee perfect after a large meal',750,'Tim Wendelboe',3);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (4,'dark','07.02.2022','Libardo Lasso','A deep chocolaty coffee for a special someone.',700,'Supreme Roastworks',4);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (5,'dark','20.04.2020','Chemex','A floral and tasty coffee for summer evenings',1500,'Back To Black',5);
INSERT INTO "Coffee" ("CoffeeID","roastdegree","roasteddate","name","description","priceperkilo","roastery","BatchID") VALUES (6,'dark','25.03.2022','test','floral',10,'test',6);
COMMIT;
