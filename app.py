from flask import Flask, request, jsonify
from repository import get_first_aid_instructions  # Import your function from the module where it's defined

app = Flask(__name__)

@app.route('/first-aid', methods=['GET'])
def get_first_aid_instructions_handler():
    # Get symptoms from query parameters
    symptoms = request.args.getlist('symptoms')

    # Check if symptoms are provided
    if not symptoms:
        return jsonify({'error': 'Symptoms not provided'}), 400

    # Call your function to get first aid instructions
    instructions = get_first_aid_instructions(*symptoms)

    return jsonify(instructions)

if __name__ == '__main__':
    app.run(debug=True)


    
