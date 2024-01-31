# C950 - NHP3
# Student ID - 010776164
# Matthew Gibson

import csv
from HashTable import *
from Package import *

package_list = HashTable()


with open('data\PackageData.csv') as csvfile:
  packages = csv.reader(csvfile, delimiter=',')

  for package in packages:
    package_list.add(int(package[0]), package)

with open('data\Distances.csv') as csvfile:

