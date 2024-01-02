from flask import Flask, request, jsonify

app = Flask(__name__)

# A list to store logged IP addresses
logged_ips = []

import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            ip_data = response.json()
            return ip_data.get('ip')
        else:
            return None
    except Exception as e:
        print(f"Error fetching public IP: {e}")
        return None

# Print the public IP address
public_ip = get_public_ip()
if public_ip:
    print(f"Public IP address of your remote machine: {public_ip}")
else:
    print("Unable to fetch public IP address.")

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
        <!-- Replace 'your-gif-filename.gif' with the actual filename of your GIF -->
        <img src="https://cdn.pixabay.com/photo/2016/06/14/14/09/skeleton-1456627_1280.png">
        <p>Hello There...</p>

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
    return jsonify({'logged_ips': 'nope'})

if __name__ == '__main__':
    # Run the app using Gunicorn
    app.run(debug=true)
