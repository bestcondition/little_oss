import os
from pathlib import Path

from flask import Flask, request

app = Flask(__name__)
share_data_path = Path(os.environ['CONTAINER_PATH'])


def get_file_path(filename):
    return share_data_path / filename


@app.route('/<filename>', methods=['GET'])
def read(filename):
    return get_file_path(filename).read_bytes()


@app.route('/<filename>', methods=['POST'])
def write(filename):
    data = request.data
    wc = get_file_path(filename).write_bytes(data)
    result = dict(length=wc)
    return result
