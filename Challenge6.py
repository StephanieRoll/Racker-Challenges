import pyrax
import os
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))
cf = pyrax.cloudfiles

cont = cf.create_container("Stuff Goes Here")
print "Name:", cont.name 

print "# of objects:", cont.object_count

cf.make_container_public("Stuff Goes Here", ttl=300)
