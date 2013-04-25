import pyrax
import time
import os
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))
cs = pyrax.cloudservers
flvs = cs.flavors.list()

for x in range(0, 3):
	
	print "currently building server pyrax" + str(x)
	server = cs.servers.create("Web" + str(x), "8bf22129-8483-462b-a020-1754ec822770", "2")
 
	print "Admin password:", server.adminPass

	while server.status != "ACTIVE":
		time.sleep(10)
 		server = cs.servers.get(server.id)



	print "ID:", server.id
	print "Status:", server.status
	print "Networks:", server.networks

