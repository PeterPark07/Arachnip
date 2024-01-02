from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Get the user's IP address from the request object
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()

    return f"IP Address logged successfully. {ip_address}"

if __name__ == '__main__':
    # Run the app using Gunicorn
    app.run(debug=True)
