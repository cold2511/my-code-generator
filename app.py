from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()
        if not data or 'problem' not in data:
            return jsonify({"error": "Request does not contain a valid JSON payload"}), 400
        
        problem = data['problem']
        # Example logic to generate code based on the problem description
        if "add two numbers" in problem.lower():
            generated_code = """
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(2, 3))
"""
        else:
            generated_code = "# Code for the problem: " + problem

        return jsonify({"code": generated_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
