import os
import subprocess
from flask import Flask, request

app = Flask(__name__)
logger = app.logger

@app.route("/open-vscode", methods=["POST"])
def open_vscode():
    res = request.get_json()
    logger.info(f"{res=}")
    if res['is_file'] == 1:
        path_dir = os.path.dirname(res['path'])
        file_name = os.path.basename(res['path'])
    else:
        path_dir = res['path']
        file_name = None
    cmd = ["code", "--folder-uri", f"vscode-remote://ssh-remote+{request.remote_addr}{path_dir}"]
    # if file_name:
    #     cmd = cmd + ["-g", file_name]
    logger.info(f"{cmd=}")
    subprocess.run(cmd, shell=False, check=True)
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)