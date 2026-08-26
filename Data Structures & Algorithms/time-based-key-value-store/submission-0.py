class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        res = ""
        if key not in self.store:
            return res

        values = self.store[key]
        low, high = 0, len(values) - 1

        while low <= high:
            mid = (low + high) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return res