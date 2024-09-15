import redis
from flask import Flask, request, jsonify

# Inicializa la aplicación Flask
app = Flask(__name__)

# Configuración de Redis Cluster
redis_nodes = [
    {'host': 'redis-server-1', 'port': '6379'},
    {'host': 'redis-server-2', 'port': '6380'},
    {'host': 'redis-server-3', 'port': '6381'}
]

# Conectar al cluster de Redis
r = redis.RedisCluster(startup_nodes=redis_nodes, decode_responses=True)

# Rutas de ejemplo
@app.route('/set', methods=['POST'])
def set_key():
    data = request.json
    key = data['key']
    value = data['value']
    r.set(key, value)
    return jsonify({'status': 'success', 'message': f'Key {key} set to {value}'}), 200

@app.route('/get', methods=['GET'])
def get_key():
    key = request.args.get('key')
    value = r.get(key)
    if value:
        return jsonify({'key': key, 'value': value}), 200
    else:
        return jsonify({'error': 'Key not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)