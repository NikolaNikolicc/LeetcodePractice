from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    # O(log n)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""

        start, end = 0, len(self.cache[key]) - 1
        ret = ""
        while start <= end:
            mid = (start + end) // 2

            if self.cache[key][mid][0] < timestamp:
                start = mid + 1
                ret = self.cache[key][mid][1]
            elif self.cache[key][mid][0] > timestamp:
                end = mid - 1
            else:
                return self.cache[key][mid][1]

        return ret

            
