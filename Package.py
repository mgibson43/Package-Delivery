class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, departure_time,
                 delivery_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departure_time = departure_time
        self.delivery_time = delivery_time

    def __str__(self):
        return f'Package ID: {self.package_id}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nZip Code: {self.zip_code}\nDeadline: {self.deadline}\nWeight: {self.weight}\nStatus: {self.status}\nDeparture Time: {self.departure_time}\nDelivery Time: {self.delivery_time}\nNotes: {self.notes}'

    def getStatus(self):
        return f'Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, Delivery Time: {self.delivery_time}, Status: {self.status}'