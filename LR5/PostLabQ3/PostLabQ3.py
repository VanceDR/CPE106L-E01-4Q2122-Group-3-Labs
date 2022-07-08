import sqlite3

conn = sqlite3.connect('PostLabQ3DB.db')
print("Database Opened")
# Adding Tables
conn.execute('''
CREATE TABLE "ADVENTURE_TRIP" (
	"TRIP_ID"	INTEGER NOT NULL,
	"TRIP_NAME"	VARCHAR(50),
	"START_LOCATION"	TEXT,
	"STATE"	TEXT,
	"DISTANCE"	NUMBER(5),
	"MAX_GRP_SIZE"	NUMBER(5),
	"TYPE"	TEXT,
	"SEASON"	TEXT
);
''')
print("Tables created successfully");
# Adding Values to Tables

conn.execute('''
INSERT INTO "ADVENTURE_TRIP" (
	TRIP_ID,
	TRIP_NAME,
	START_LOCATION,
	STATE,
	DISTANCE,
	MAX_GRP_SIZE,
	TYPE,
	SEASON
)
VALUES (
	45,
	"Jay Peak",
	"Jay",
	"VT",
	8,
	8,
	"Hiking",
	"Summer"
);
''')
print("Entries added successfully");
# Printing the Added Values

cursor = conn.execute('''
SELECT TRIP_ID, TRIP_NAME, START_LOCATION, STATE, DISTANCE, MAX_GRP_SIZE, TYPE, SEASON
FROM ADVENTURE_TRIP
''')

for row in cursor:
	print("TRIP_ID:\t", row[0])
	print("TRIP_NAME:\t", row[1])
	print("START_LOCATION:\t", row[2])
	print("STATE:\t\t", row[3])
	print("DISTANCE:\t", row[4])
	print("MAX_GRP_SIZE:\t", row[5])
	print("TYPE:\t\t", row[6])
	print("SEASON:\t\t", row[7], "\n")

print("Entries displayed successfully");
conn.close()