from flask import Flask
import os
import subprocess
from datetime import datetime
import  pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Monika Gour"
    username = os.getenv("USERNAME")

    zone = pytz.timezone("ASia/Kolkata")
    serverTime = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S %f')

    output = subprocess.getoutput("top -bn1")

    return f"""
    <html>
        <body>
            <h2>Name: {name} </h2>
            <h2>User: {username} </h2>
            <h2>Server Time (IST): {serverTime} </h2>
            <pre> {output} </pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(port=5000)