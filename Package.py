class Package:
  def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, departure_time, delivery_time):
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
    return f'Package ID: {self.package_id}\nAddress: {self.address}, {self.city}, {self.state} {self.zip_code}\nWeight: {self.weight}\nNotes: {self.notes}\nStatus: {self.status}\nDeparture Time: {self.departure_time}\nDelivery Time: {self.delivery_time}'