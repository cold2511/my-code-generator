from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return "Welcome to the Code Generator!"

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()
        app.logger.debug(f'Received data: {data}')
        
        if data is None:
            return jsonify({'error': 'Request does not contain a valid JSON payload'}), 400

        problem = data.get('problem')
        app.logger.debug(f'Problem: {problem}')

        if not problem:
            return jsonify({'error': 'No problem provided'}), 400

        # Placeholder code generation logic
        generated_code = f"# Code for the problem: {problem}"

        return jsonify({'code': generated_code})
    except Exception as e:
        app.logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
