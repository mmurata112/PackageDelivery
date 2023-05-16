import csv
from HashMap import HashMap

# Read CSV file and separate by commas in order to enter into value
with open("PackageFile.csv", "r") as package_data:
    package_data = csv.reader(package_data, delimiter=',')

    # Create hashmap function
    # Create arrays for packages to be delivered on truck_1, truck_2, truck_3
    hash_map = HashMap()
    truck_1 = []
    truck_2 = []
    truck_3 = []

    # Insert values from the csv file into key/value pairs: O(N)
    for row in package_data:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        delivery_start = ' '
        address_location = ' '
        delivery_status = 'At hub'

        value = [id, address_location, address, city, state, zip, deadline, weight, note, delivery_start, delivery_status]

        # Assigning packages to truck_1
        # If package has a deadline or isn't delayed --> placed in truck_1
        if "EOD" not in value[6] and 'Delayed' not in value[8]:
            truck_1.append(value)

        # B/c 13/15 placed in truck_1, package 19 added to truck_1 due to the note
        if value[0] == '19':
            truck_1.append(value)

        # Assigning packages to truck_2
        # Note stating package can only be on truck_2 or won't arrive until after 9:05 AM
        if 'Can only' in value[8] or 'Delayed' in value[8]:
            truck_2.append(value)

        # Updating address and assigning to truck_3 b/c info unknown until 10:20 AM
        if value[0] == '9':
            value[2] = '410 S State St'
            value[5] = '84111'
            truck_3.append(value)

        # Insert remaining packages into truck_2 and truck_3
        # Adding to truck_2 if total amount of packages is less than truck_3 knowing it won't exceed 16 packages
        if value not in truck_1 and value not in truck_2 and value not in truck_3:
            if len(truck_2) < len(truck_3):
                truck_2.append(value)
            else:
                truck_3.append(value)

        # Insert each package into the hash map
        hash_map.insert(id, value)

    # Get list of packages on truck_1: O(1)
    def get_truck_1():
        return truck_1

    # Get list of packages on truck_2: O(1)
    def get_truck_2():
        return truck_2

    # Get list of packages on truck_3: O(1)
    def get_truck_3():
        return truck_3

    # Get complete list of all key/value pairs of all packages: O(1)
    def get_hash_map():
        return hash_map