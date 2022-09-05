import logging
from time import sleep

from fan_controller import protocol, helpers, transmitter, config

logger = logging.getLogger(__name__)


def send_command(remote_name: str, command_name: str):
    """
    Send a specific command to fan
    source - ID of source remote HEX
    command - command itself HEX
    """
    source = config.get_remote_address(remote_name)
    command = protocol.COMMANDS[command_name.upper()]
    logger.info("Going to send command %s from source %s", source, command)
    binary_command = helpers.hex2bin(source) + helpers.hex2bin(command) + protocol.ENDING[2:]
    transmitter.transmit(binary_command)
    sleep(helpers.us2s(protocol.PAUSE_BETWEEN_REPEATS * 50))


def add_remote(remote_name: str, remote_address: str):
    config.add_remote(remote_name, remote_address)


def del_remote(remote_name: str):
    config.del_remote(remote_name)
