import grpc
from concurrent import futures
import redis
import cache_pb2_grpc
import cache_pb2

# Conexión con Redis Cluster
redis_nodes = [
    {'host': 'redis-server-1', 'port': '6379'},
    {'host': 'redis-server-2', 'port': '6380'},
    {'host': 'redis-server-3', 'port': '6381'}
]

r = redis.RedisCluster(startup_nodes=redis_nodes, decode_responses=True)

class CacheServicer(cache_pb2_grpc.CacheServicer):
    def Set(self, request, context):
        r.set(request.key, request.value)
        return cache_pb2.SetResponse(status="success")

    def Get(self, request, context):
        value = r.get(request.key)
        return cache_pb2.GetResponse(value=value)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_CacheServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
