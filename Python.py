import hashlib
import time
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

mining = False
block_found = False

def mine_block(difficulty):
    global block_found
    nonce = 0
    while not block_found:
        # Simulate mining by hashing the block header with varying nonce values
        block_header = f"Block Header: nonce={nonce}"
        block_hash = hashlib.sha256(block_header.encode()).hexdigest()
        # Check if the hash meets the required difficulty level
        if block_hash.startswith('0' * difficulty):
            block_found = True
            print(f"Block mined! Nonce: {nonce}, Hash: {block_hash}")
        else:
            nonce += 1

@app.route('/start_mining', methods=['POST'])
def start_mining():
    global mining, block_found
    if not mining:
        # Start a new thread for mining
        mining = True
        block_found = False
        data = request.get_json()
        difficulty = data.get('difficulty', 4)  # Default difficulty level
        threading.Thread(target=mine_block, args=(difficulty,)).start()
        return jsonify({'message': 'Mining started'})
    else:
        return jsonify({'error': 'Mining process is already running'})

@app.route('/get_statistics', methods=['GET'])
def get_statistics():
    # Logic for fetching mining statistics
    # Simulated response
    statistics = {
        'total_blocks': 100,
        'total_rewards': 1000,
        'average_hashrate': 50
    }
    return jsonify(statistics)

@app.route('/send_to_wallet', methods=['POST'])
def send_to_wallet():
    data = request.get_json()
    wallet_address = data.get('wallet_address')
    # Simulated response
    return jsonify({'message': 'Rewards sent to wallet'})

if __name__ == '__main__':
    app.run(debug=True)
    