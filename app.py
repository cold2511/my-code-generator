from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Code Generator!"

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()
        problem = data.get('problem')
        if not problem:
            return jsonify({'error': 'No problem provided'}), 400

        # Placeholder code generation logic
        generated_code = f"# Code for the problem: {problem}"

        return jsonify({'code': generated_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
