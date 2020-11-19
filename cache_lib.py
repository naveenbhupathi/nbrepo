import time

class CachedItem(object):
    """
    This class is used to track the last timestamp and frequency the function/logic called
    key : function name
    value: function result
    frequency: how many times function called
    display method: returns function cached details in list format
    """
    def __init__(self, key, value, frequency):
        self.key = key
        self.value = value
        self.timeStamp = time.time()
        self.frequency = frequency

    def display(self):
        return [self.key, self.value, self.timeStamp, self.frequency]

class CachedDict(dict):
    """
    Cache functionality:
    MAX_CACHE_SIZE set to 3
    Check if function which needs to be cached exists in cache memory or not.
        if not exists:
            check if cache memory is free:
                if cache memory is free:
                    insert function with corresponding result, its current timestamp and frequency of occurrence
                    of the function.
                if cache memory is full:
                    1. fetch old timestamp exists in cache,
                    2. for the old timestamp pick the entries which have less frequently used
                    3. delete the entry in cache and insert new entry
        if key exists:
            increment frequency of the key and update latest timestamp for the key in the cache
    """

    def clear_cache(self):
        self.clear()

    def cacheIt(self, key, value):

        MAX_CACHE_SIZE = 3

        if key not in self:
            if len(self) < MAX_CACHE_SIZE:
                # insert data in cache
                print('adding new value')
                c1 = CachedItem(key, value, 1)
                self[key] = c1.display()
            else:
                # implement cache eviction that picks entry having old age and less frequently used.
                values = list(self.values())
                minimum_timestamp = min(values, key = lambda x: x[2])[2]
                record_key = min(
                    list(
                        filter(
                            lambda min_timestamp_records: min_timestamp_records[2] == minimum_timestamp, values)
                    ),
                    key = lambda min_freq_records : min_freq_records[3]
                )
                delete_key = record_key[0]
                del self[delete_key]
                print('adding new value')
                c1 = CachedItem(key, value, 1)
                self[key] = c1.display()

        else:
            print('loading from cache')
            frequency = self[key][3] + 1
            c1 = CachedItem(key, value, frequency)
            self[key] = c1.display()

        print("self : ", self)

        return '<CachedItem {%s:%s} last updated with frequency %s>' \
               % (self[key][0], self[key][1], self[key][3])

if __name__ == '__main__':

    cd = CachedDict()
    print(cd.cacheIt('a', 10))
    print("------------")
    print(cd.cacheIt('e', 14))
    time.sleep(2)
    print("------------")
    print(cd.cacheIt('c', 17))
    print("------------")
    print(cd.cacheIt('c', 10))
    time.sleep(2)
    print("------------")
    print(cd.cacheIt('d', [1,2,3,4]))
    print("------------")
    print(cd.cacheIt('a', 10))
    print("------------")
    print(cd.cacheIt('b', 17))
    print("------------")
    print(cd.cacheIt('f', 12))
    time.sleep(2)
    print(cd.cacheIt('a', 13))
    print(cd.cacheIt('b', 14))
    time.sleep(5)
    print(cd.cacheIt('a', 15))
    print(cd.cacheIt('b', 16))
    time.sleep(1)
    print(cd.cacheIt('e', 2))

    cd.clear_cache()

    print(cd.cacheIt('s', {'a':1, 'b':2}))
