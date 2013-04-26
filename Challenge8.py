import pyrax
import os

pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))
cf = pyrax.cloudfiles
dns = pyrax.cloud_dns 
cont = cf.create_container("Website Goes Here")
print "Name:", cont.name 

cf.make_container_public("Website Goes Here", ttl=300)

content = "This is brought to you by Cloud Files"

obj = cf.store_object("Website Goes Here", "index.html", content)

print "Stored object", obj
print "# of objects:", cont.object_count

cont = cf.get_container("Website Goes Here")

cont_uri = cont.cdn_uri

new_domain = dns.create(name="Webby.com", emailAddress="admin@example.com")
print "Adding Records"

new_domain.add_records({"type": "CNAME", "name": "www.Webby.com", "data": cont_uri, "ttl": "300"}
)

new_meta = {"X-Container-Meta-Web-Index": "index.html"}
cf.set_container_metadata(cont, new_meta)
