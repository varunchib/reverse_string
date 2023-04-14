from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/reverse', methods=[ 'POST'])
def reverse_string():
    input_string = request.args.get('input_string', '')
    reversed_string = input_string[::-1]
    response = {'reversed_string': reversed_string}
    return jsonify(response)

@app.route('/status', methods=['GET'])
def check_status():
    response = {'status': 'OK'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
