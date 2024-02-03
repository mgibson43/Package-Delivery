# C950 - NHP3
# Student ID - 010776164
# Matthew Gibson

import csv
import datetime
from HashTable import *
from Package import *
from Truck import *

# Initialize package hash table
package_list = HashTable()

# Read in package data from csv
with open('data\PackageData.csv') as csvpkg:
  packages = csv.reader(csvpkg, delimiter=',')

  # Create package item from read in data
  for item in packages:
    package_id = int(item[0])
    address = item[1]
    city = item[2]
    state = item[3]
    zip_code = item[4]
    deadline = item[5]
    weight = item[6]
    notes = item[7]

    package = Package(package_id, address, city, state, zip_code, deadline, weight, notes)

    # Add package to package hash table
    package_list.add(package_id, package)

# Read in distance data from csv
with open('data\AdjacencyMatrix.csv') as csvdst:
  distances = csv.reader(csvdst)
  distances = list(distances)

# Read in address data from csv
with open('data\Addresses.csv') as csvadd:
  addresses = csv.reader(csvadd)
  addresses = list(addresses)

# Method for retrieving the distance between two addresses
def findDistance(addr1, addr2):
  return distances[addr1][addr2]

# Method for finding the shortest edge between the current node and the given nodes
def findMinDistance(curr_addr, pkg_list):
  curr_addr = findAddress(curr_addr)
  test_addr = findAddress(package_list.get(pkg_list[0]).address)
  curr_min = findDistance(curr_addr, test_addr)
  next_addr = package_list.get(pkg_list[0]).address
  curr_pkg = pkg_list[0]

  for i in range(1, len(pkg_list)-1):
    test_addr = findAddress(package_list.get(pkg_list[i]).address)
    dist = findDistance(curr_addr, test_addr)
    if float(dist) < float(curr_min):
      curr_min = dist
      next_addr = package_list.get(pkg_list[i]).address
      curr_pkg = i
  return [next_addr, curr_min, curr_pkg]

# Method for retrieving the index of an address
def findAddress(address):
  for addr in addresses:
    if address in addr[2]:
      return int(addr[0])

truck1 = Truck("4001 South 700 East", 15, 0.0, True, datetime.timedelta(hours=8), [1,2,5,7,8,10,11,12,13,15,17,19,21,22,23,24])

def startTruckDelivery(truck):
  while len(truck.truck_package_list) > 0:
    min = findMinDistance(truck.curr_location, truck.truck_package_list)
    print(min)
    truck.curr_location = min[0]
    truck.miles += float(min[1])
    truck.truck_package_list.pop(min[2])
    print(truck.curr_location)
    print(truck.miles)
    print(truck.truck_package_list)
    
 

startTruckDelivery(truck1)