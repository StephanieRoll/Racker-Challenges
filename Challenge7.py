import pyrax
import time
import os
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))
cs = pyrax.cloudservers
clb = pyrax.cloud_loadbalancers
img_id = cs.images.list()[0].id 
flavor_id = cs.flavors.list()[0].id

server1 = cs.servers.create("server1", img_id, flavor_id)
s1_id = server1.id
server2 = cs.servers.create("server2", img_id, flavor_id)
s2_id = server2.id 

print "Building Servers"

while not (server1.networks and server2.networks):
    time.sleep(1)
    server1 = cs.servers.get(s1_id)
    server2 = cs.servers.get(s2_id)

server1_ip = server1.networks["private"][0]
server2_ip = server2.networks["private"][0]

print "Creating Nodes"

node1 = clb.Node(address=server1_ip, port=80, condition="ENABLED")
node2 = clb.Node(address=server2_ip, port=80, condition="ENABLED")

print "Creating VIP for LB"

vip = clb.VirtualIP(type="PUBLIC")

print "Creating LB"

lb = clb.create("Challenge7_LB", port=80, protocol="HTTP",
        nodes=[node1, node2], virtual_ips=[vip])

print "Continuing With Server Build"

while server1.status and server2.status != "ACTIVE":
	time.sleep(10)
	server1 = cs.servers.get(server1.id)
	server2 = cs.servers.get(server2.id)

print "Server Build Complete"
print "Name:", server1.name 
print "ID:", server1.name, server1.id
print "Status:", server1.name, server1.status
print "Networks:", server1.name, server1.networks
print "Name:", server2.name 
print "ID:", server2.name, server2.id
print "Status:", server2.name, server2.status
print "Networks:", server2.name, server2.networks


