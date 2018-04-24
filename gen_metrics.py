from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://172.17.0.2:27017')
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print "Printing Server Status"
pprint(serverStatusResult)

#do a lot of bulk inserts

#Create testdb
db = client.bulk_example
total = db.test.count()
print "Total entries before insert: %s" %total
#create 10k entries
db.test.insert(({'i': i} for i in xrange(10000)))
total = db.test.count()
print "Total entries after insert: %s" %total


