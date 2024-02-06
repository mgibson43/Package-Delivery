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

# Method for finding the shortest edge given a starting node and a list of nodes
def findMinDistance(curr_addr, pkg_list):
  
  # Initialize variables and find first distance
  next_addr = package_list.get(pkg_list[0]).address
  next_miles = findDistance(findAddress(curr_addr), findAddress(next_addr))
  index = 0

  # Iterate through list and update minimum distance
  for i in range(1, len(pkg_list) - 1):
    test_addr = package_list.get(pkg_list[i]).address
    test_miles = findDistance(findAddress(curr_addr), findAddress(test_addr))

    # If min distance is found, update address, miles, and index
    if (float(next_miles) > float(test_miles)):
      next_addr = test_addr
      next_miles = test_miles
      index = i

  return [next_addr, next_miles, index]  

def statusUpdate(truck, next_addr, miles, index):
  truck.curr_location = next_addr
  truck.miles += float(miles)
  truck.time += datetime.timedelta(hours=float(miles) / float(truck.speed))
  delivered = truck.truck_package_list.pop(index)

  
  package_list.get(delivered).status = "Delivered"

# Create trucks and manually load each
final_load = [3,6,8,9,12,18,25,26,36,37,38]
truck1 = Truck("4001 South 700 East", 18, 0.0, datetime.timedelta(hours=8), [1,2,4,5,7,10,11,13,14,15,16,19,20,34,39,40], 1)
truck2 = Truck("4001 South 700 East", 18, 0.0, datetime.timedelta(hours=9), [17,21,22,23,24,27,28,29,30,31,32,33,35], 2)

# Begins package delivery for given truck
def startTruckDelivery(truck):

  for i in range(1, 41):
    package_list.get(i).status = "En route"
  
  while len(truck.truck_package_list) > 0:
    
    next = findMinDistance(truck.curr_location, truck.truck_package_list)
    statusUpdate(truck, next[0], next[1], next[2])
    
    
  
  if ((int(truck.truck_number) == 2) and len(final_load) != 0):
    next = findDistance(findAddress(truck.curr_location), 0)
    truck.miles += float(next)
    truck.curr_location = "4001 South 700 East"
    truck.truck_package_list = final_load
    startTruckDelivery(truck2)

startTruckDelivery(truck1)
startTruckDelivery(truck2)