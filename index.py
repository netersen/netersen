

from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get the user's IP address
    user_ip = request.remote_addr

    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Log the IP address and timestamp every time the page is accessed
    with open('access_log.txt', 'a') as log_file:
        log_file.write(f'IP: {user_ip}, Access Time: {timestamp}\n')

    # HTML/CSS for displaying the text
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        font-family: 'Poppins', sans-serif;
      }

      .main-text {
        text-align: center;
      }

      .bright-text {
        color: black;
      }

      .gray-text {
        color: gray;
      }
    </style>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap">
    </head>
    <body>
      <div class="main-text">
        <h1 class="bright-text">Netersen?</h1>
        <p class="gray-text">(heqiqeten)</p>
      </div>
    </body>
    </html>
    """

    return html_content

if __name__ == "__main__":
   app.run(debug=False,host="0.0.0.0")