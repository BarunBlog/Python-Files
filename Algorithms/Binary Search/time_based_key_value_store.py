# Leetcode: 981. Time Based Key-Value Store

class TimeMap:
    def __init__(self) -> None:
        self.hashMap: dict[list] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        
        self.hashMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        
        return self.search(self.hashMap[key], timestamp)
        
    def search(self, li: list[list], timestamp: int) -> str:
        left = 0
        right = len(li) - 1

        while left <= right:
            mid = (left + right) // 2

            if li[mid][0] == timestamp:
                return li[mid][1]
            if left == mid:
                if li[right][0] <= timestamp:
                    return li[right][1]
                else:
                    if li[left][0] > timestamp:
                        return ""
                    return li[left][1]
            
            if li[mid][0] > timestamp:
                right = mid
            if li[mid][0] < timestamp:
                left = mid

    def show(self) -> None:
        print(self.hashMap)

def main():
    timeMap = TimeMap()

    timeMap.set("test", "one", 10)
    timeMap.set("test", "two", 20)
    timeMap.set("test", "three", 30)

    # timeMap.show()

    print(timeMap.get("test", 15))
    print(timeMap.get("test", 25))


if __name__ == "__main__":
    main()