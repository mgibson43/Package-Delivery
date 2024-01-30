from HashTable import *

class Truck:
  def __init__(self, curr_location, speed, miles, driver, depart_time):
    self.max_packages = 16
    self.curr_packages = 0
    self.package_list = [None] * max_packages
    self.driver = driver
    self.speed = speed
    self.miles = miles
    self.curr_location = curr_location
    self.depart_time = depart_time