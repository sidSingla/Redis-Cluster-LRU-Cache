# RedisCluster is used which provides availability and consistency. 
# LRU cache is implemented by storing keys in double ended-list to add/remove key and key-value is stored in another store.
import redis
from rediscluster import RedisCluster
from rediscluster.connection import ClusterConnectionPool

class LRUCache:
    def __init__(self, cluster_host_port_mapping=[{"host": "127.0.0.1", "port": "6379"}], ttl=60, cache_size=3):
        self.startup_nodes = cluster_host_port_mapping
        self.ttl = ttl
        self.conn = None
        self.max_conn = 50
        self.max_conn_per_node = 10
        self.cache_size=cache_size
        self.CACHE_KEYS = "cache_lru_keys"
        self.CACHE_STORE = "cache_lru_store"

        self.pool = ClusterConnectionPool(
            max_connections=self.max_conn,
            max_connections_per_node=self.max_conn_per_node,
            startup_nodes=self.startup_nodes,
            init_slot_cache=True, skip_full_coverage_check=True)
        
        # Flushes keys so that results are consistent for the example client code. Not to be used in real-world deployment.
        self.flush_all()

    def connect(self):
        conn = redis.RedisCluster(connection_pool=self.pool, skip_full_coverage_check=True)
        return conn

    def flush_all(self):
        conn = self.connect()
        conn.flushall()
    
    def get(self, key):
        conn = self.connect()
        result = conn.hget(self.CACHE_STORE, key)
        
        if result:
            conn.lrem(self.CACHE_KEYS, 1, key)
            conn.lpush(self.CACHE_KEYS, key)
        
        return result

    def set(self, key, value):
        conn = self.connect()
        if not conn.hexists(self.CACHE_STORE, key):
            self.check_capacity(conn)
            conn.hset(self.CACHE_STORE, key, value)
            conn.lpush(self.CACHE_KEYS, key)

    def check_capacity(self, conn):
        if conn.llen(self.CACHE_KEYS) >= self.cache_size:
            to_pop = conn.rpop(self.CACHE_KEYS)
            conn.hdel(self.CACHE_STORE, to_pop)
            conn.delete(to_pop)
