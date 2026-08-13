from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        data_list = self.map[key]
        if data_list[0][0] > timestamp:
            return ""
        if data_list[-1][0] < timestamp:
            return data_list[-1][1]
        
        low, high = 0, len(data_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if data_list[mid][0] == timestamp:
                return data_list[mid][1]
            elif data_list[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return data_list[high][1]