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


def incr(name, amount=1):
    return rds.incr(name, amount)

def zadd(key, value):
    return rds.zadd(key, value, 0)

def zrange(key):
    return rds.zrange(key,0,-1)

def exist(key) :
    return rds.exists(key)


def hset(name, key, value):
    rds.hset(name, key, value)


def hget(name, key):
    return rds.hget(name, key)

def hgetall(name):
    return rds.hgetall(name)

def hexist(name, key):
    return rds.hexists(name, key)


if __name__ == '__main__':
    make_connection()
    set('foo','hi')
    zadd("hi","ho")
    zadd("hi","het")
    print(zrange("hi"))
    print(rds.get('foo'))