from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    data = request.json
    problem = data.get('problem')
    
    # Placeholder for AI code generation logic
    generated_code = f"// This is the generated code for the problem: {problem}"
    
    return jsonify({'code': generated_code})

# Vercel expects an `app` callable by default, so no need to include `if __name__ == '__main__':` block
