import logging
from time import time, sleep
from RPi import GPIO

from fan_controller import protocol, config, helpers, server

logger = logging.getLogger(__name__)


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
