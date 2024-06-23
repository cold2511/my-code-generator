from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.json
        problem = data.get('problem')

        # Check if problem is provided
        if not problem:
            raise ValueError("Problem statement is required")

        # Placeholder for AI code generation logic
        generated_code = f"// This is the generated code for the problem: {problem}"

        return jsonify({'code': generated_code})

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
