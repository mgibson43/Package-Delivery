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

# Method for retrieving the index of an address
def findAddress(address):
  for addr in addresses:
    if address in addr[2]:
      return int(addr[0])

# Method for retrieving the distance between two addresses
def findDistance(addr1, addr2):
  return distances[addr1][addr2]

def findMinDistance(curr_addr, pkg_list):
  next_addr = package_list.get(pkg_list[0]).address
  next_miles = findDistance(findAddress(curr_addr), findAddress(next_addr))
  index = 0

  for i in range(1, len(pkg_list) - 1):
    test_addr = package_list.get(pkg_list[i]).address
    test_miles = findDistance(findAddress(curr_addr), findAddress(test_addr))

    if (float(next_miles) > float(test_miles)):
      next_addr = test_addr
      next_miles = test_miles
      index = i

  return [next_addr, next_miles, index]  

truck1 = Truck("4001 South 700 East", 15, 0.0, True, datetime.timedelta(hours=8), [33,2,5,7,8,10,11,12,13,15,17,19,21,22,23,24])

def startTruckDelivery(truck):
  while len(truck.truck_package_list) > 0:
    
    next = findMinDistance(truck.curr_location, truck.truck_package_list)
    
    truck.next_addr = next[0]
    truck.miles += float(next[1])
    truck.truck_package_list.pop(next[2])

    print(truck.next_addr)
    print(truck.miles)
    print(truck.truck_package_list)


startTruckDelivery(truck1)