import sys
#allowing command line args
if len(sys.argv) > 1:
    limit = int(sys.argv[1])
else:
    limit = 250

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://localhost:27017/admin')
#client = MongoClient('mongodb://172.17.0.2:27017/admin')
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
#print "Printing Server Status"
#pprint(serverStatusResult)

#do a lot of bulk inserts

#Create testdb
db = client.bulk_example
total = db.bulk_example.count()
print "Starting IO Traffic"
print "Total entries before insert: %s" %total
#Stimulate Inserts 10k entries
for i in xrange(limit):
    db.bulk_example.insert_one(({'Variable1': i})) 
    db.bulk_example.insert_one(({'Variable2': i})) 
    db.bulk_example.insert_one(({'Variable3': i})) 
total = db.bulk_example.count()
print "Total entries after insert: %s" %total

#Simulate Deletes
for i in xrange(limit):
    db.bulk_example.delete_many(({'Variable1': i}))
total = db.bulk_example.count()
print "Total entries after insert: %s" %total




#total = db.bulk_example.count()
#print "Total entries after deletes: %s" %total
