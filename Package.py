class Package:
  def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
    self.package_id = package_id
    self.address = address
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.deadline = deadline
    self.weight = weight
    self.notes = notes
    self.delivered = False
    self.departure_time = 0
    self.delivery_time = 0

  def __str__(self):
    return f'Package ID: {self.package_id}\nAddress: {self.address}, {self.city}, {self.state} {self.zip_code}\nWeight: {self.weight}\nNotes: {self.notes}\nDelivered: {self.delivered}\nDeparture Time: {self.departure_time}\nDelivery Time: {self.delivery_time}'