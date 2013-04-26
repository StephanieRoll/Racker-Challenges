import pyrax
import time
import os
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))

cdb = pyrax.cloud_databases

inst = cdb.create("Challenge_Instance", flavor= "512MB Instance", volume=1)
print inst

print "Creating MySQL Instance"

while inst.status != "ACTIVE":
	time.sleep(10)
	inst = cdb.get(inst)	

print "Creating Database"

db = inst.create_database("Important_Database")
print "DB:", db.name

user = inst.create_user(name="Important_User", password="hush hush", database_names=[db])
print "User:", user.name



