import logging
from time import time, sleep
from RPi import GPIO

from fan_controller import protocol, config, helpers

# switching to debug will break protocol, because printing will increase pulse length
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_command(source: str, command: str):
    """
    Send a specific command to fan
    source - ID of source remote HEX
    command - command itself HEX
    """
    logger.info("Going to send command %s from source %s", source, command)
    binary_command = helpers.hex2bin(source) + helpers.hex2bin(command) + protocol.ENDING[2:]
    transmit(binary_command)
    sleep(helpers.us2s(protocol.PAUSE_BETWEEN_REPEATS * 50))


def transmit(code: str):
    logging.info("Will send '%s'", code)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.GPIO_TX, GPIO.OUT)
    for _ in range(protocol.REPEAT_TIMES):
        logger.debug("Repeat %d", protocol.REPEAT_TIMES)
        for symbol in code:
            logger.debug("Going to transmit %s", symbol)
            if symbol == '1':
                logger.debug("GPIO %d set to high", config.GPIO_TX)
                GPIO.output(config.GPIO_TX, GPIO.HIGH)
            elif symbol == '0':
                logger.debug("GPIO %d set to low", config.GPIO_TX)
                GPIO.output(config.GPIO_TX, GPIO.LOW)
            else:
                raise ValueError(f"Wrong symbol {symbol} in a binary code")
            logger.debug("Will sleep %d µs", protocol.PAUSE_BETWEEN_REPEATS)
            _sleep(protocol.PULSE_LENGTH)
        GPIO.output(config.GPIO_TX, GPIO.LOW)
        _sleep(protocol.PAUSE_BETWEEN_REPEATS)


def _sleep(sleep_period: int):
    current_time = time()
    sleep_till = current_time + (sleep_period * (10 ** -6))
    logger.debug("Current time %f, sleep till %s", current_time, sleep_till)
    tick = helpers.us2s(protocol.PULSE_LENGTH) / 100
    while time() <= sleep_till:
        sleep(tick)


def main():
    send_command("0x96d96db64b24", protocol.LIGHT_TOGGLE)
    # send_command("0xb6db2c96592c", protocol.LIGHT_TOGGLE)


if __name__ == '__main__':
    main()
