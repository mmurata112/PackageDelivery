# Michael Murata ID:001509498

from DeliveryInfo import get_hash_map
from Packages import get_total_distance
import datetime


class Main:
    # Display message as well as user interface in order to access information on any of the packages
    print("====================================================================")
    print("Welcome to the Western Governors University Parcel Service Interface")
    print("====================================================================\n")

    option = input("""Please select one of the following options:
------------------------------------------- 
1: Lookup information of a particular package at a specific time
2: Lookup status of all packages within a specific time frame
3: Lookup total distance of all trucks
4: Exit
""")

    # Use a while loop in order for the interface to be active until either an error or "exit" is chosen
    while option != "4":
        # User selects 1: Get info for a single package at a particular time: O(N)
        if option == '1':
            try:
                package = input("Enter package ID: ")
                departure_time = get_hash_map().get_info(str(package))[9]
                delivery_time = get_hash_map().get_info(str(package))[10]
                time = input("Enter a time in form (HH:MM:SS): ")
                (hrs, mins, secs) = time.split(':')
                new_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = departure_time.split(':')
                new_departure_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = delivery_time.split(':')
                new_delivery_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Seeing if the departure time is greater than the input time
                # if departure_time is greater than the input = package has not left yet
                if new_departure_time >= new_time:
                    get_hash_map().get_info(str(package))[10] = "At Hub"
                    get_hash_map().get_info(str(package))[9] = "Leaves at " + departure_time

                    # Prints Packages current info
                    print(
                        f"Package ID: {get_hash_map().get_info(str(package))[0]}\n"
                        f"Address: {get_hash_map().get_info(str(package))[2]}, {get_hash_map().get_info(str(package))[3]}, {get_hash_map().get_info(str(package))[5]}\n"
                        f"Deadline: {get_hash_map().get_info(str(package))[6]}\n"
                        f"Weight: {get_hash_map().get_info(str(package))[7]}\n"
                        f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                    )
                # If departure_time is less than input time, means package is either in transit or has been delivered
                elif new_departure_time <= new_time:
                    # input time is less than delivery time = in transit
                    if new_time < new_delivery_time:
                        get_hash_map().get_info(str(package))[10] = "In transit"
                        get_hash_map().get_info(str(package))[9] = "Left at " + departure_time

                        print(
                            f"Package ID: {get_hash_map().get_info(str(package))[0]}\n"
                            f"Address: {get_hash_map().get_info(str(package))[2]}, {get_hash_map().get_info(str(package))[3]}, {get_hash_map().get_info(str(package))[4]}, {get_hash_map().get_info(str(package))[5]}\n"
                            f"Deadline: {get_hash_map().get_info(str(package))[6]}\n"
                            f"Weight: {get_hash_map().get_info(str(package))[7]}\n"
                            f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                        )

                    # if new_time is greater than delivery_time means it's been delivered already
                    else:
                        get_hash_map().get_info(str(package))[10] = "Delivered at " + delivery_time
                        get_hash_map().get_info(str(package))[9] = "Left at " + departure_time

                        print(
                            f"Package ID: {get_hash_map().get_info(str(package))[0]}\n"
                            f"Address: {get_hash_map().get_info(str(package))[2]}, {get_hash_map().get_info(str(package))[3]}, {get_hash_map().get_info(str(package))[5]}\n"
                            f"Deadline: {get_hash_map().get_info(str(package))[6]}\n"
                            f"Weight: {get_hash_map().get_info(str(package))[7]}\n"
                            f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                        )

            except ValueError:
                print("Sorry invalid entry")
                exit()

        elif option == '2':
            # Choosing option to get info on all packages in a specific time frame: O(N)
            try:
                start_time = input("Enter a start time in form (HH:MM:SS): ")
                end_time = input("Enter an end time in form (HH:MM:SS): ")
                (hrs, mins, secs) = start_time.split(':')
                new_start_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = end_time.split(':')
                new_end_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Uses a for loop to go through each package in the hash_map: O(N)
                for package in range(1, 41):
                    try:
                        departure_time = get_hash_map().get_info(str(package))[9]
                        delivery_time = get_hash_map().get_info(str(package))[10]
                        (hrs, mins, secs) = departure_time.split(':')
                        new_departure_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = delivery_time.split(':')
                        new_delivery_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    # if the departure_time is less than the end_time it means that its either in transit/delivered
                    if new_departure_time < new_end_time:
                        # if delivery_time is < end_time it means that the package has been delivered
                        if new_delivery_time < new_end_time:
                            get_hash_map().get_info(str(package))[10] = "Delivered"

                            # print the package ID followed by its delivery status
                            print(
                                f"Package ID: {get_hash_map().get_info(str(package))[0]}, "
                                f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                            )
                        else:
                            # if delivery_time is greater than end_time, it hasn't been delivered so its "In Transit"
                            get_hash_map().get_info(str(package))[10] = "In Transit"

                            print(
                                f"Package ID: {get_hash_map().get_info(str(package))[0]}, "
                                f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                            )
                    # departure_time is greater than end_time means it hasn't left the hub yet
                    elif new_departure_time > new_end_time:
                        get_hash_map().get_info(str(package))[10] = "At Hub"

                        print(
                            f"Package ID: {get_hash_map().get_info(str(package))[0]}, "
                            f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                        )
                    # Departure_time is less than start_time meaning it hasn't left y et and is still at the hub
                    elif new_departure_time < new_start_time:
                        get_hash_map().get_info(str(package))[10] = "At Hub"

                        print(
                            f"Package ID: {get_hash_map().get_info(str(package))[0]}, "
                            f"Delivery Status: {get_hash_map().get_info(str(package))[10]}"
                        )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print("Sorry invalid entry")
                exit()
        # Choosing option 3 which is to return the total distance of the trucks: O(1)
        elif option == '3':
            print(f"The total distance of the 3 trucks is: {get_total_distance():.2f} miles")
            break

        # user selects 4 which exits the program
        elif option == "4":
            print("Thank you and have a nice day!")
            exit()

        else:
            print("Invalid entry")
            exit()