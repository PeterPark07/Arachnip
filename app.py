from flask import Flask, request, jsonify

app = Flask(__name__)

# A list to store logged IP addresses
logged_ips = []

@app.route('/', methods=['GET'])
def index():
    return """
    <html>
    <head>
        <title>Static Webpage</title>
        <script>
            function logIP() {
                fetch('https://api64.ipify.org?format=json')  // You can use any IP lookup service
                    .then(response => response.json())
                    .then(data => {
                        // Send the IP address to the server
                        fetch('/log', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ ip: data.ip }),
                        });
                    })
                    .catch(error => {});
            }

            // Execute logIP() when the page loads
            window.onload = logIP;
        </script>
    </head>
    <body>
        <h1>This is a Static Webpage</h1>
        <p>Some text here...</p>

        <!-- Replace 'your-gif-filename.gif' with the actual filename of your GIF -->
        <img src="https://cdn.pixabay.com/animation/2023/12/22/00/19/00-19-58-407_512.gif" alt="Nice to meet you">

    </body>
    </html>
    """

@app.route('/log', methods=['POST'])
def log_ip():
    data = request.get_json()
    ip_address = data.get('ip')

    if ip_address:
        # Log the IP address to the list
        logged_ips.append(ip_address)
        return jsonify({'message': 'Hello There.'}), 200
    else:
        return jsonify({'error': 'Invalid request.'}), 400

@app.route('/get_logs', methods=['GET'])
def get_logs():
    return jsonify({'logged_ips': logged_ips})

if __name__ == '__main__':
    # Run the app using Gunicorn
    app.run(debug=true)
