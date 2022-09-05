class WrongRemoteAddress(Exception):
    def __init__(self, remote_address):
        self.remote_address = remote_address
        super().__init__(
            f"Remote addess {remote_address} is wrong. Use hex values between '0x96d96db64b24' and '0x136db2c96592b'."
        )
