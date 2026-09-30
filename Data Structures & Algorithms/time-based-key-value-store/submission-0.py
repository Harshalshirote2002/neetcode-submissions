class TimeMap:

    def __init__(self):
        self._mappings = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._mappings.keys():
            self._mappings[key].append({
                "value": value,
                "timestamp": timestamp
            })
        else:
            self._mappings.update({key: [{"value": value, "timestamp":timestamp}]})
        

    def get(self, key: str, timestamp: int) -> str:
        values_list = self._mappings.get(key, [])
        if not values_list:
            return ""
        start = 0
        end = len(values_list) - 1
        if values_list[0]["timestamp"] > timestamp:
            return ""
        while start <= end:
            mid = start + (end-start)//2
            
            if timestamp == values_list[mid]["timestamp"]:
                return values_list[mid]["value"]
            elif timestamp > values_list[mid]["timestamp"]:
                start = mid + 1
            else:
                end = mid - 1

        if values_list[mid]["timestamp"] < timestamp:
            return values_list[mid]["value"]
        else:
            return values_list[mid-1]["value"]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)