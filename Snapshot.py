from HashTable import *
from Package import *


class Snapshot:
    def __init__(self, time, pkg_list):
        self.time = time
        self.package_list = HashTable()
        for i in range(1, 41):
            pkg = pkg_list.get(i)
            package = Package(pkg.package_id, pkg.address, pkg.city, pkg.state, pkg.zip_code, pkg.deadline, pkg.weight,
                              pkg.notes, pkg.status, pkg.departure_time, pkg.delivery_time)
            self.package_list.add(package.package_id, package)
