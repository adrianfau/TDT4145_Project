BEGIN TRANSACTION;
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
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (1,'floral','10.3.2022',1,1,10);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (2,'bland','11.3.2022',1,3,5);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (3,'amazing','07.02.2022',2,5,9);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (4,'floral','2022-03-25',4,1,7);
INSERT INTO "Post" ("PostID","tastingnotes","tastingdate","UserID","CoffeeID","points") VALUES (5,'banan','2022-03-25',4,6,8);
COMMIT;
