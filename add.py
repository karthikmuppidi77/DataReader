from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='redis.finvedic.in', port=6379)

@app.route('/read/<stock>', methods=['GET'])
def read_stock(stock):
    data = r.get(stock)
    if data:
        return jsonify(json.loads(data)), 200
    return jsonify({'message': 'Stock not found'}), 404

if __name__ == '__main__':
    app.run(port=5002)
