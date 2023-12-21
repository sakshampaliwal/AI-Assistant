from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute_command', methods=['POST'])
def execute_command():
    if request.method == 'POST':
        data = request.get_json()
        command = data['command']
        
        if command == 'time':
            result = subprocess.check_output(['python', 'main.py']).decode('utf-8')
            return jsonify({'result': result})
        
        # Add more conditions for other commands and execute corresponding Python functions

    return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
