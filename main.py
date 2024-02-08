# C950 - NHP3
# Student ID - 010776164
# Matthew Gibson

import csv
import datetime
from HashTable import *
from Package import *
from Truck import *
from Snapshot import *

# Initialize package hash table
package_list = HashTable()
snapshots = list()

# Read in package data from csv
with open('PackageData.csv') as csv_pkg:
    packages = csv.reader(csv_pkg, delimiter=',')

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
        status = "At the hub"
        departure_time = None
        delivery_time = None

        package = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status, departure_time,
                          delivery_time)

        # Add package to package hash table
        package_list.add(package_id, package)

# Read in distance data from csv
with open('AdjacencyMatrix.csv') as csv_dst:
    distances = csv.reader(csv_dst)
    distances = list(distances)

# Read in address data from csv
with open('Addresses.csv') as csv_add:
    addresses = csv.reader(csv_add)
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
        if float(next_miles) > float(test_miles):
            next_addr = test_addr
            next_miles = test_miles
            index = i

    return [next_addr, next_miles, index]


# Updates the status of the delivered package
def deliveryUpdate(truck, next_addr, miles, index):
    truck.curr_location = next_addr
    truck.miles += float(miles)
    truck.time += datetime.timedelta(hours=float(miles) / float(truck.speed))
    pkg = truck.truck_package_list.pop(index)

    package_list.get(pkg).status = "Delivered"
    package_list.get(pkg).delivery_time = truck.time

    # Checks time to update incorrect package
    if truck.time >= datetime.timedelta(hours=10, minutes=20):
        changePackageAddress(9, "410 S State St", "84111")

    takeSnapshot(truck.time, package_list)


# Updates package status of packages on truck to "En route" when a truck leaves the distribution center
def enRouteUpdate(truck):
    for pkg in truck.truck_package_list:
        package_list.get(pkg).status = "En Route"
        package_list.get(pkg).departure_time = truck.time


# Record snapshots of the packages at a given time
def takeSnapshot(time, package_list):
    snapshots.append(Snapshot(time, package_list))


def getSnapshot(time):
    if time > snapshots[len(snapshots) - 1].time:
        return snapshots[len(snapshots) - 1].package_list
    if time <= snapshots[0].time:
        return snapshots[0].pkg_list.package_list

    for i in range(len(snapshots) - 1):
        if time == snapshots[i].time:
            snapshot = snapshots[i].package_list
            break
        if time < snapshots[i].time:
            snapshot = snapshots[i - 1].package_list
            break

    return snapshot


# Create trucks and manually load each
final_load = [3, 6, 8, 9, 12, 18, 25, 26, 36, 37, 38]
truck1 = Truck("4001 South 700 East", 18, 0.0, datetime.timedelta(hours=8),
               [1, 2, 4, 5, 7, 10, 11, 13, 14, 15, 16, 19, 20, 34, 39, 40], 1)
truck2 = Truck("4001 South 700 East", 18, 0.0, datetime.timedelta(hours=9),
               [17, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 35], 2)


# Begins package delivery for given truck
def startTruckDelivery(truck):
    # Set packages to "En route"
    enRouteUpdate(truck)

    # Loop until all packages have been delivered
    while len(truck.truck_package_list) > 0:
        next_addr = findMinDistance(truck.curr_location, truck.truck_package_list)
        deliveryUpdate(truck, next_addr[0], next_addr[1], next_addr[2])
        takeSnapshot(truck.time, package_list)S

        # Load final set of packages only if the truck is truck 2
        if (int(truck.truck_number) == 2) and len(final_load) != 0:
            hub = findDistance(findAddress(truck.curr_location), 0)
            truck.miles += float(hub)
            truck.time += datetime.timedelta(hours=float(hub) / float(truck.speed))
            truck.curr_location = "4001 South 700 East"

            # Checks time to update incorrect package
            if truck.time < datetime.timedelta(hours=10, minutes=20):
                truck.time = datetime.timedelta(hours=10, minutes=20)
                changePackageAddress(9, "410 S State St", "84111")
            truck.truck_package_list = final_load

            startTruckDelivery(truck2)


# Changes the address and zip_code of a given package
def changePackageAddress(pkg, addr_new, zip_code):
    if package_list.get(int(pkg)).address == addr_new:
        return
    else:
        package_list.get(int(pkg)).address = addr_new
        package_list.get(int(pkg)).zip_code = zip_code


# Starts the user interface
def userInterface():
    total_miles = float(truck1.miles) + float(truck2.miles)

    print("Western Governors University Parcel Service")
    print("-" * 50)
    print("Total miles: " + str(total_miles))
    print("-" * 50)
    while True:

        user_input = input(
            "Enter a time for which you would like to see the status of the package(s) in HH:MM format: ")
        (h, m) = user_input.split(":")
        time = datetime.timedelta(hours=int(h), minutes=int(m))

        snapshot = getSnapshot(time)

        pkg = input("Enter a package number you would like to see the status of (Leave blank for all packages): ")
        print(f'\n\nPackage status at {time}: ')
        print("-" * 50)

        if pkg == '':
            for i in range(1, 41):
                print(str(snapshot.get(i)))
                print("-" * 50)
        else:
            print(str(snapshot.get(int(pkg))))
            print("-" * 50)

        end = input("Enter 'q' to quit (Press Enter to continue):")
        if end == "q":
            break
    return


startTruckDelivery(truck1)
startTruckDelivery(truck2)

userInterface()
