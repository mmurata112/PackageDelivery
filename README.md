Package Delivery System
Overview
This project is a Python-based package delivery system designed to optimize the delivery of packages using a greedy algorithm. The system manages package information, calculates delivery routes, and tracks the status of packages at specific times. It uses a hash map for efficient package lookup and integrates data from CSV files to determine distances and addresses.

Features
Package Management: Stores and retrieves package information using a hash map.

Route Optimization: Uses a greedy algorithm to determine the shortest delivery route for each truck.

Delivery Status Tracking: Tracks the status of packages (e.g., "At Hub", "In Transit", "Delivered") at specific times.

Distance Calculation: Calculates the total distance traveled by each truck and the overall distance for all trucks.

User Interface: Provides a command-line interface for users to look up package information and delivery statuses.

Files
Main.py: The main script that runs the program and provides the user interface.

HashMap.py: Implements a hash map for storing and managing package data.

DeliveryInfo.py: Reads package data from a CSV file and assigns packages to trucks.

Distances.py: Reads distance and address data from CSV files and calculates optimal delivery routes.

PackageFile.csv: Contains package information (e.g., ID, address, deadline, weight, etc.).

Distance_Data.csv: Contains distance data between locations.

distance_address.csv: Maps addresses to distance indices.

How It Works
Package Assignment: Packages are assigned to one of three trucks based on their deadlines, special notes, and delivery constraints.

Route Optimization: The greedy algorithm determines the shortest route for each truck by finding the nearest neighbor at each step.

Delivery Simulation: The system simulates package deliveries and updates the delivery status based on the input time.

User Interaction: Users can interact with the system via a command-line interface to:

Look up the status of a specific package at a given time.

View the status of all packages within a specific time frame.

Get the total distance traveled by all trucks.
