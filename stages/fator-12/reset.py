from redis import Redis
import signal, os

host_redis=os.environ.get('HOST_REDIS', 'redis')
port_redis=os.environ.get('PORT_REDIS', '6379')

redis = Redis(host=host_redis, port=port_redis)

redis.set('hits', 0)