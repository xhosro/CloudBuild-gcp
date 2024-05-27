import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    # Retrieve the environment variable 'someVar'
    someVarFromEnv = os.environ.get('someVar')
    # Return a formatted string including the value of 'someVarFromEnv'
    return 'I have changed the text here for testing: {}!\n second line'.format(someVarFromEnv)

if __name__ == "__main__":
    # Enable debug mode for more detailed error messages and auto-reloading
    app.debug = True
    # Run the Flask app, listening on all network interfaces (0.0.0.0) and port specified in environment or default to 8080
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
