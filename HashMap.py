# https://www.youtube.com/watch?v=9HFbhPscPU0&ab_channel=JoeJames

class HashMap:
    def __init__(self):
        self.size = 41
        self.map = [None] * self.size
        # Size of hashmap = 41 because we know there are 40 packages so we need total + 1 so no overlap
        # Map = array the data will be stored in * 40 cells

    # Function to create hash key: O(1)
    def _get_hash(self, key):
        return int(key) % self.size
        # creates the hash key O(1)

    # Function to insert package into the hash table: O(N)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for package in self.map[key_hash]:
                if package[0] == key:
                    package[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Update a package thats already in the hash table: O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for package in self.map[key_hash]:
                if package[0] == key:
                    package[1] = value
                    print([1])
                    return True
        elif value == 0:
            pass
        else:
            print("Error updating following package: " + str(key))

    # Get value from the hash table using the key: O(N)
    def get_info(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for package in self.map[key_hash]:
                if package[0] == key:
                    return package[1]
        else:
            print("No info is available")

    # Deletes value from the hash table: O(N)
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        else:
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                    return True

    # Prints out hash table: O(N)
    def print(self):
        print('------------------------------------------------PACKAGE HASHMAP------------------------------------------------')
        for item in self.map:
            if item is not None:
                print(item)