import redis

# Connect to Redis server on default port 6379 and use database 0
r = redis.Redis(host='192.168.1.64', port=6379, db=0)

# --- Basic String Example ---

# Set a key called 'welcome' with a string value
r.set('welcome', 'Hello, Redis!')

# Get the value of the key 'welcome'
# Output will be a byte string: b'Hello, Redis!'
print(r.get('welcome'))


# --- Hash Example (like a Python dict) ---

# Create a Redis hash under the key 'user:1'
# This hash stores fields 'name' and 'email' for a user
r.hset('user:1', mapping={
    'name': 'Alice',
    'email': 'alice@example.com'
})

r.hset('user:2', mapping={
    'name': 'Giuseppe',
    'email': 'giuseppe@example.com'
})

# Get all fields and values in the hash as a dictionary of byte strings
# Output: {b'name': b'Alice', b'email': b'alice@example.com'}
print(r.hgetall('user:2'))


# --- List Example (acts like a queue or stack) ---

# Push 'Task A' to the left of the list 'tasks'
r.lpush('tasks', 'Task A')

# Push 'Task B' to the left of the list 'tasks' (it becomes the first item)
r.lpush('tasks', 'Task B')

# Retrieve all elements from the list 'tasks' (from index 0 to -1, meaning the full list)
# Output: [b'Task B', b'Task A']
print(r.lrange('tasks', 0, -1))