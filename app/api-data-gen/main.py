from flask import Flask, jsonify, request

from src.data_generator import transaction, consumer, product

app = Flask(__name__)


@app.route('/transactions')
def transactions():
    top = int(request.args.get('top', default=10))
    data = {'value': []}
    for _ in range(top):
        data['value'].append(transaction())
    return jsonify(data)


@app.route('/consumers')
def consumers():
    top = int(request.args.get('top', default=10))
    data = {'value': []}
    for _ in range(top):
        data['value'].append(consumer())
    return jsonify(data)


@app.route('/products')
def products():
    top = int(request.args.get('top', default=10))
    data = {'value': []}
    for _ in range(top):
        data['value'].append(product())
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)