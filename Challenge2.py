import pyrax
import time
import os
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))
cs = pyrax.cloudservers
id_of_server = cs.servers.list()[0].id 
image_id = cs.servers.create_image(id_of_server,"Image3")
print "beep boop boop beep...Creating Image" 
	
image_of_server = cs.images.get(image_id)

while image_of_server.status != "ACTIVE":
	time.sleep(10)
	image_of_server = cs.images.get(image_id)	

print "beep boop boop beep...Image Complete"

new_server = cs.servers.create("Tanks_Box2", image_of_server, "2")

print "beep boop boop beep...Server Building\n", "Admin Password", new_server.adminPass

while new_server.status != "ACTIVE":
	time.sleep(10)
	new_server = cs.servers.get(new_server.id)

print "Server Build Complete"
print "ID:", new_server.id
print "Status:", new_server.status
print "Networks:", new_server.networks


















