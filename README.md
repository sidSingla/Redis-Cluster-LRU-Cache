<h1>Description</h1>
LRU Cache has been implemented using Redis Cluster as the caching system.<br/>
Redis Cluster - https://redis.io/topics/cluster-tutorial.<br/>
Redis Cluster Python Implementation - https://github.com/Grokzen/redis-py-cluster.<br/>

Redis cluster was setup. Same host machine was used with different ports to mimic distributed setting. 3 masters and 3 slaves according to the minimum requirement for a cluster.<br/> 
https://medium.com/@iamvishalkhare/create-a-redis-cluster-faa89c5a6bb4#:~:text=Running%20Redis%20in%20cluster%20mode&text=Every%20instance%20also%20contains%20the,every%20time%20it%20is%20needed.<br/>

<h1>Expected Code Output</h1>
b'3'<br/>
None<br/>
b'3'<br/>
b'5'<br/>
b'6'<br/>

<h1>Future Work</h1>
Multi-threaded client implementation.
