from flask import Flask, jsonify, request, render_template
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html is in a 'templates' folder

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['prompt']
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer API-key',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': user_message}]
        }
    )
    if 'choices' in response.json():
        reply = response.json()['choices'][0]['message']['content']
        return jsonify({'reply': reply})
    else:
        error = response.json()['error']['message']
        return jsonify({'reply': error})
if __name__ == '__main__':
    app.run(debug=True, port=5001)


            const data = await response.json();
            responseBox.innerText = data.choices[0].message.content; // Display the response
        });
    </script>
</body>
</html>
