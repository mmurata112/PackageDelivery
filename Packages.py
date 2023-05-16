import DeliveryInfo
import Distances
import datetime

# Empty arrays created for truck packages and truck distances
trucK_1_delivery = []
trucK_2_delivery = []
truck_3_delivery = []
truck_1_distance = []
truck_2_distance = []
truck_3_distance = []

# arrays for start time and time of deliveries
first_departure = ['8:00:00']
second_departure = ['9:15:00']
third_departure = ['10:30:00']

# Set delivery_start in package_data for truck 1 packages to first_departure: O(N)
for index, delivery_start in enumerate(DeliveryInfo.get_truck_1()):
    DeliveryInfo.get_truck_1()[index][9] = first_departure[0]
    trucK_1_delivery.append(DeliveryInfo.get_truck_1()[index])

# Compare package address to distance_address.csv: O(N^2)
for index, package_address in enumerate(trucK_1_delivery):
    for distance_name in Distances.get_address():
        if package_address[2] == distance_name[2]:
            truck_1_distance.append(package_address[0])
            trucK_1_delivery[index][1] = distance_name[0]

# Call greedy algorithm to sort the packages for optimal route in truck_1
Distances.optimize_route(trucK_1_delivery, 1, 0)
total_distance_1 = 0

# Calculate total distance of the first truck and distance of each package: O(N)
for index in range(len(Distances.get_1_index())):
    try:
        total_distance_1 = Distances.get_total_distance(int(Distances.get_1_index()[index]), int(Distances.get_1_index()[index + 1]), total_distance_1)
        package_distance = Distances.get_time(Distances.get_current_distance(int(Distances.get_1_index()[index]), int(Distances.get_1_index()[index + 1])), first_departure)
        Distances.get_1_sorted()[index][10] = (str(package_distance))
        DeliveryInfo.get_hash_map().update(int(Distances.get_1_sorted()[index][0]), trucK_1_delivery)
    except IndexError:
        pass

# Repeat of the 3 for loops above for trucks 2 and 3.  Setting delivery_start for truck 2 packages to second_departure: O(N)
for index, delivery_start in enumerate(DeliveryInfo.get_truck_2()):
    DeliveryInfo.get_truck_2()[index][9] = second_departure[0]
    trucK_2_delivery.append(DeliveryInfo.get_truck_2()[index])

# Compare package address to distance_address.csv: O(N^2)
for index, package_address in enumerate(trucK_2_delivery):
    for distance_name in Distances.get_address():
        if package_address[2] == distance_name[2]:
            truck_2_distance.append(package_address[0])
            trucK_2_delivery[index][1] = distance_name[0]

Distances.optimize_route(trucK_2_delivery, 2, 0)
total_distance_2 = 0

# Calculate total distance of the second truck and distance of each package: O(N)
for index in range(len(Distances.get_1_index())):
    try:
        total_distance_2 = Distances.get_total_distance(int(Distances.get_2_index()[index]), int(Distances.get_2_index()[index + 1]), total_distance_1)
        package_distance = Distances.get_time(Distances.get_current_distance(int(Distances.get_2_index()[index]), int(Distances.get_2_index()[index + 1])), second_departure)
        Distances.get_2_sorted()[index][10] = (str(package_distance))
        DeliveryInfo.get_hash_map().update(int(Distances.get_2_sorted()[index][0]), trucK_2_delivery)
    except IndexError:
        pass

# Repeat of the 3 for loops above for trucks 2 and 3.  Setting delivery_start for truck 3 packages to third_departure: O(N)
for index, delivery_start in enumerate(DeliveryInfo.get_truck_3()):
    DeliveryInfo.get_truck_3()[index][9] = third_departure[0]
    truck_3_delivery.append(DeliveryInfo.get_truck_3()[index])

# Compare package address to distance_address.csv: O(N^2)
for index, package_address in enumerate(truck_3_delivery):
    for distance_name in Distances.get_address():
        if package_address[2] == distance_name[2]:
            truck_3_distance.append(package_address[0])
            truck_3_delivery[index][1] = distance_name[0]

Distances.optimize_route(truck_3_delivery, 3, 0)
total_distance_3 = 0

# Calculate total distance of the third truck and distance of each package: O(N)
for index in range(len(Distances.get_3_index())):
    try:
        total_distance_3 = Distances.get_total_distance(int(Distances.get_3_index()[index]), int(Distances.get_3_index()[index + 1]), total_distance_3)
        package_distance = Distances.get_time(Distances.get_current_distance(int(Distances.get_3_index()[index]), int(Distances.get_1_index()[index + 1])), third_departure)
        Distances.get_3_sorted()[index][10] = (str(package_distance))
        DeliveryInfo.get_hash_map().update(int(Distances.get_3_sorted()[index][0]), truck_3_delivery)
    except IndexError:
        pass

# Gets the total distance from the sum of the 3 trucks: O(1)
def get_total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3