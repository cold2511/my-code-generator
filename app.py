from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Code Generator!"

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    problem = request.json.get('problem')
    if not problem:
        return jsonify({'error': 'No problem provided'}), 400
    
    # Implement your code generation logic here
    generated_code = f"# Code for the problem: {problem}"
    
    return jsonify({'code': generated_code})

if __name__ == '__main__':
    app.run(debug=True)
