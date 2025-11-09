# app.py
from flask import Flask, jsonify
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
counter_file = "/var/log/counter.log"
count = 0

# Logger: write to file (so the sidecar can tail it) and to stdout
logger = logging.getLogger("counter")
logger.setLevel(logging.INFO)
# Rotating file
fh = RotatingFileHandler(counter_file, maxBytes=5*1024*1024, backupCount=2)
fh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
logger.addHandler(fh)
# stdout
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
logger.addHandler(sh)

@app.route("/")
def root():
    global count
    count += 1
    msg = f"counter={count}"
    logger.info(msg)
    return jsonify({"message": msg, "count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
