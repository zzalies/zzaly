import redis

rds = None


def make_connection():
    global rds
    rds = redis.StrictRedis(host='localhost', port=6379, db=1, charset='utf-8')
    print("redis connection make ok")

def get(key):
    return rds.get(key)

def delete(key):
    return rds.delete(key)

def mget(keylist):
    return rds.mget(keylist)

def keys(pat):
    return rds.keys(pat)


def set(key, value):
    rds.set(key, value)


def incr(name, amount=1):
    return rds.incr(name, amount)

def hincr(name, key, amount=1):
    return rds.hincrby(name,key,amount)

def hkeys(name):
    return rds.hkeys(name)

def zadd(key, value, score):
    return rds.zadd(key, score, value)

def zrange(key):
    return rds.zrange(key,0,-1)

def exist(key) :
    return rds.exists(key)


def hset(name, key, value):
    rds.hset(name, key, value)

def hmset(name, mapping):
    rds.hmset(name, mapping)

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