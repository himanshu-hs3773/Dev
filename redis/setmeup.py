import redis

# noinspection PyUnresolvedReferences
connection = redis.Redis()
connection.ping()

# Redis Configuration
redis_host = 'localhost'
redis_port = 6379
redis_db = 0

# noinspection PyUnresolvedReferences
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
# print(redis_client)
print(redis_client.get("query"))
redis_client.setex("query", 300, "json.dumps()")
print(redis_client.get("query"))

redis_client.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})
# True

print(redis_client.hgetall('user-session:123'))
# {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}
