from flask import Flask, request

from fan_controller import controller
app = Flask(__name__)


@app.route('/command/<remote_name>/<command>', methods=['GET', 'POST'])
def process_command(remote_name, command):
    controller.send_command(remote_name, command)
    return ''

@app.route('/modify/remote/<remote_name>', methods=['PUT', 'DELETE'])
def modify_remote(remote_name: str):
    controller.del_remote(remote_name)
    return ''


@app.route('/new/remote', methods=['POST'])
def new_remote():
    req = request.json
    controller.add_remote(req['remote_name'], req['remote_id'])
    return ''
