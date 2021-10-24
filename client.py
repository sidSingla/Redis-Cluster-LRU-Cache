from redis_lru_cache import LRUCache

host_port_mapping = [{"host": "127.0.0.1", "port": "6379"},
						{"host": "127.0.0.1", "port": "6380"},
						{"host": "127.0.0.1", "port": "6381"},
						{"host": "127.0.0.1", "port": "6382"},
						{"host": "127.0.0.1", "port": "6383"},
						{"host": "127.0.0.1", "port": "6384"}]
cache = LRUCache(cluster_host_port_mapping=host_port_mapping)
cache.set(1,3)
cache.set(2,4)
cache.set(3,5)

# Cache reached capacity but no eviction yet. key 1 is still present.
print(cache.get(1))

# Least recently used key-2 will be evicted. key 4 will be added.
cache.set(4,6)

# Key 2 is not present in cache. Therefore None
print(cache.get(2))

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))