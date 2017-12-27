import redis

rds = None


def make_connection():
    global rds
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    rds = redis.Redis(connection_pool=pool, max_connections=10)
    print("redis connection make ok")


def get(key):
    return rds.get(key)


def set(key, value):
    rds.set(key, value)


def incr(name, amount=10):
    return rds.incr(name, amount)


def exist(key) :
    return rds.exists(key)


def hset(name, key, value):
    rds.hset(name, key, value)


def hget(name, key):
    return rds.hget(name, key)


def hexist(name, key):
    return rds.hexists(name, key)


if __name__ == '__main__':
    make_connection()
    rds.set('foo','hi')
    print(rds.get('foo'))