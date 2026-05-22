from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "Hi"
=======
    return "Hello EC2 sever!"
>>>>>>> 6453ab5a3bb0961c2096fb4d9392c1044bebcb6e

@app.route("/health")
def health():
    return {
        "status": "running",
        "server": "EC2"
    }

if __name__ == "__main__":
    # 0.0.0.0 allows external access
    app.run(host="0.0.0.0", port=5000)
