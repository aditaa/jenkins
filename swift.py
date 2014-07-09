from swiftclient import Connection

import logging


class Swift:

    def __init__(self, username, password, tenant, auth_url, region):
        self.swift_client = Connection(
            user=username,
            key=password,
            tenant_name=tenant,
            authurl=auth_url,
            auth_version="2.0",
            os_options={'region_name': region}
        )

        # Setup logging
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.WARNING)
    
        # Allow the logger to write all output to stdout too
        self.logger.addHandler(logging.StreamHandler())
  
    def list_containers(self):
        try:
            self.containers = self.swift_client.get_account()[1]
      
            self.logger.warning("Listing Containers")
            for container in self.containers:
                self.logger.warning(container['name'])
    
        except Exception:
            self.logger.error("Listing Containers Failed")
            self.exit(1)

    def list_objects(self):
        try:
            self.logger.warning("Listing Objects")
            for container in self.containers:
                for swift_container in self.swift_client.get_container(container['name'])[1]:
                    self.logger.warning(container['name'] + " " + swift_container['name'])
    
        except Exception as e:
            self.logger.error('Listing Objects Failed, Got exception: %s' % e)
            self.exit(1)

    def create_container(self, name):
        try:
            self.container = name
            self.swift_client.put_container(self.container)
            self.logger.warning("Created Container %s", self.container)

        except Exception:
            self.logger.error("Creating Container Failed")
            self.exit(1)

    def create_object(self, name, contents):
        try:
            self.object = name
            self.swift_client.put_object(self.container, self.object, contents)
            self.logger.warning("Created Object %s", self.object)

        except Exception:
            self.logger.error("Creating Object Failed")
            self.exit(1)

    def get_container(self):
        try:
            self.containers = self.swift_client.get_account()[1]

            for container in self.containers:
                if container['name'] == self.container:
                    self.logger.warning("Getting Container Succeeded")

                    return True

            self.logger.error("Getting Container Failed")
            self.exit(1)

        except Exception as e:
            self.logger.error('Getting Container Failed: Got exception: ' % e)
            self.exit(1)

    def get_object(self):
        try:
            object = self.swift_client.get_object(self.container, self.object)
            self.logger.warning("Object Get: %s", object)

        except Exception as e:
            self.logger.error('Object Get Failed, Got exception: %s' % e)
            self.exit(1)

    def delete_object(self):
        try:
            self.swift_client.delete_object(self.container, self.object)
            self.logger.warning("Object Deleted")

        except Exception as e:
            self.logger.error('Object Deletion Failed: Got exception: ' % e)
      
    def delete_container(self):
        try:
            self.swift_client.delete_container(self.container)
            self.logger.warning("Container Deleted")

        except Exception as e:
            self.logger.error('Container Deletion Failed: Got exception: ' % e)

    def exit(self, value):
        if hasattr(self, 'object'):
            self.delete_object()

        if hasattr(self, 'container'):
            self.delete_container()
    
        exit(value)

    def run(self):
        self.list_containers()
        self.list_objects()

        self.create_container()
        self.create_object()

        self.get_container()
        self.get_object()
    
        self.exit(0)
