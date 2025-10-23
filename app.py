from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'OK', 200


@app.route('/data', methods=['POST'])
def data():
# Expect JSON payload with a `name` field
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({'error': 'Invalid or missing JSON'}), 400
    name = payload.get('name')
    if not name:
        return jsonify({'error': 'Missing "name" field'}), 400


# Simple echo response — replace with your logic
    return jsonify({'message': f'Hello, {name}!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)