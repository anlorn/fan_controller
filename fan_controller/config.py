from fan_controller import errors


GPIO_TX = 25

# TODO use file
remotes = {}


def add_remote(remote_name: str, remote_address: str):
    int_remote_address = int(remote_address, 16)
    if int_remote_address < 124395444549723 or int_remote_address > 341789950499115:
        raise errors.WrongRemoteAddress(remote_address)

    if remote_name not in remotes:
        remotes[remote_name] = remote_address


def del_remote(remote_name: str):
    if remote_name in remotes:
        del remotes[remote_name]


def get_remote_address(remote_name: str):
    return remotes[remote_name]
