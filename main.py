# C950 - NHP3
# Student ID - 010776164
# Matthew Gibson

import csv
from HashTable import *
from Package import *
from Truck import *

package_list = HashTable()


with open('data\PackageData.csv') as csvpkg:
  packages = csv.reader(csvpkg, delimiter=',')

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

    package_list.add(package_id, package)

with open('data\Distances.csv') as csvdst:
  distances = csv.reader(csvdst)
  distances = list(distances)

with open('data\Addresses.csv') as csvadd:
  addresses = csv.reader(csvadd)
  addresses = list(addresses)

def findDistance(add1, add2):
  return distances[add1][add2]

def deliverPackages(truck):
  while len(truck.package_list) > 0:
    


