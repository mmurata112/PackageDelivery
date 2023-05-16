import csv
import datetime

# read csv files with the address names and distance data
with open("distance_address.csv") as distance_name:
    distance_name = list(csv.reader(distance_name, delimiter=','))
with open("Distance_Data.csv") as distance_data:
    distance_data = list(csv.reader(distance_data, delimiter=','))

    # Get the address data
    def get_address():
        return distance_name

    # calculate the total distance using Distance_Data.csv: O(1)
    def get_total_distance(row, col, total):
        distance = distance_data[row][col]
        if distance == '':
            distance = distance_data[col][row]

        return total + float(distance)

    # calculate the current distance only (same as above w/o total): O(1)
    def get_current_distance(row, col):
        distance = distance_data[row][col]
        if distance == '':
            distance = distance_data[col][row]

        return float(distance)

    # calculates time for each delivery and totals for a given truck: O(N)
    def get_time(distance, truck_time_list):
        time = distance / 18
        distance_in_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
        final_time = distance_in_min + ':00'
        truck_time_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_time_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        return total

    # empty arrays that will contain the packages sorted efficiently for delivery
    truck_1_sorted = []
    truck_1_index = []
    truck_2_sorted = []
    truck_2_index = []
    truck_3_sorted = []
    truck_3_index = []

    # Algorithm uses the greedy approach through the use of recursion in order to determine the shortest route
    #   by determining which vertices are closest to the current location
    # Uses 3 parameters
    #   1. List of the packages     2. The truck number     3. Current location of the truck
    # shortest_route set to 50 since no distances between any of the vertices were larger than 50
    # location = 0 which is the starting point of the deliveries (The Hub)
    def optimize_route(package_list, truck_num, current_location):
        if not len(package_list):
            return package_list
        shortest_route = 50.0
        location = 0

        # for loop through package list to determine which vertex has the shortest distance from the current location
        # repeatedly update the shortest route until the smallest value is found: O(N)
        for i in package_list:
            value = int(i[1])
            if get_current_distance(current_location, value) <= shortest_route:
                shortest_route = get_current_distance(current_location, value)
                location = value

        # Once shortest route is found, the for loop cycles through the packages until the distance is == shortest_route
        # Dependent on truck number it is then appended to both the sorted array and the index array while also being
        #   popped from the package_list indicating that we are done using that package
        # current location is updated and then the optimize_route function is recursively called until the package_list
        #   is empty: O(N) --> O(N^2)
        for i in package_list:
            if get_current_distance(current_location, int(i[1])) == shortest_route:
                if truck_num == 1:
                    truck_1_sorted.append(i)
                    truck_1_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    optimize_route(package_list, 1, current_location)
                if truck_num == 2:
                    truck_2_sorted.append(i)
                    truck_2_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    optimize_route(package_list, 2, current_location)
                if truck_num == 3:
                    truck_3_sorted.append(i)
                    truck_3_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    optimize_route(package_list, 3, current_location)

    # insert 0 for first index of each list as the starting point
    truck_1_index.insert(0, '0')
    truck_2_index.insert(0, '0')
    truck_3_index.insert(0, '0')

    # all get functions to return a value from one of the arrays created from the greedy algorithm: O(1)
    def get_1_sorted():
        return truck_1_sorted

    def get_1_index():
        return truck_1_index

    def get_2_sorted():
        return truck_2_sorted

    def get_2_index():
        return truck_2_index

    def get_3_sorted():
        return truck_3_sorted

    def get_3_index():
        return truck_3_index