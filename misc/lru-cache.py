""""
Two way to implement it

1. using counter: increase number on every new page to cache and evict the lowest value page out of cache
2. Use Stack with removal from inbetween to put on top. If page is reference, pop it from stack and put it on top of the stack.
    Eviction: remove the bottom one page from the stack
"""



class LRU():

    cache = dict() # page -> counter
    counter = 0
    cache_size = 4

    def __init__(self, cache_size):
        self.cache_size = cache_size

    def evictpage(self) -> int:
        sorted_cache = sorted(self.cache.items(), key=lambda x: x[1])
        evicted_page = sorted_cache[0]
        del self.cache[evicted_page[0]]
        print(evicted_page[0])
        return evicted_page

    def addpage(self, page:int) :
        self.counter += 1
        if len(self.cache) < self.cache_size:
            self.cache[page] = self.counter
        else:
            self.evictpage()
            self.cache[page] = self.counter
        # print("adding", page, self.cache)



'''
fine key with lowest value, if exist
lookup will be o(1)
removal: 
'''

page_stream = [1,2,3,4,2,3,4,5,3,4,5,2]
cache_size = 4

# lru_cache = LRU(cache_size)
# for page in page_stream:
#     lru_cache.addpage(page)



''''
Second method is by using stack
'''

class LRUStack():

    lrustack = []
    capacity = 4

    def __init__(self, capacity:int):
        self.capacity = capacity
    
    def evictpage(self) -> int:
        # delete from bottom of the stack
        evicted_page =  self.lrustack[0]
        print(evicted_page)
        del self.lrustack[0]

    def addpage(self, page:int) -> bool:
        print("adding", page, self.lrustack)
        if page in self.lrustack:
            # pop and push it to top
            pg_idx = self.lrustack.index(page)
            del self.lrustack[pg_idx]
            self.lrustack.append(page)
            return
        if len(self.lrustack) >= self.capacity:
            self.evictpage()
            self.lrustack.append(page)
        else:
            self.lrustack.append(page)

        


lru_cache = LRUStack(cache_size)
for page in page_stream:
    lru_cache.addpage(page)