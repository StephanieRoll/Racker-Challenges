import pyrax
import os
import sys
pyrax.set_credential_file(os.path.expanduser("~/.rackspace_cloud_credentials"))

if len(sys.argv) !=3:
	print "Wrong number of arguments, please provide a total of three."
	
fqdn = sys.argv[1]
ip = sys.argv[2]

dns = pyrax.cloud_dns
domainname = ".".join(fqdn.split(".")[-2:])

print "Creating Domain"

new_domain = dns.create(name=domainname, emailAddress="admin@example.com")

print "Adding Records"

new_domain.add_records({"type": "A", "name": fqdn, "data": ip, "ttl": "300"})

for record in dns.list_records(new_domain):
	print record.name
	