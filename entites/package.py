class Package:
  def __init__(self, package_id, address, city, state, zip_code, deadline, weight, instructions):
    self.package_id = package_id
    self.address = address
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.deadline = deadline
    self.weight = weight
    self.instructions = instructions
    self.delivered = False
    self.departure_time = 0
    self.delivery_time = 0