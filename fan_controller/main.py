import logging
from time import time, sleep
from RPi import GPIO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

gpio_tx = 25

pulse_length = 200 # µs
pause_between_repeats = 24000 # µs
repeat_times = 10

code = '1001011011011001011011011011011001001011001001001001001011001011001011001'


def transmit(code: str, pulse_length: int, gpio_tx: int):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_tx, GPIO.OUT)
    for i in range(repeat_times):
        logger.debug("Repeat %d", repeat_times)
        for symbol in code:
            logger.debug("Going to transmit %s", symbol)
            if symbol == '1':
                logger.debug("GPIO %d set to high", gpio_tx)
                GPIO.output(gpio_tx, GPIO.HIGH)
            elif symbol == '0':
                logger.debug("GPIO %d set to low", gpio_tx)
                GPIO.output(gpio_tx, GPIO.LOW)
            else:
                raise ValueError(f"Wrong symbol {symbol} in a binary code")
            logger.debug("Will sleep %d µs", pulse_length)
            _sleep(pulse_length)
        GPIO.output(gpio_tx, GPIO.LOW)
        _sleep(pause_between_repeats)


def _sleep(sleep_period: int):
    current_time = time()
    sleep_till = current_time + (sleep_period * (10 ** -6))
    logger.debug("Current time %f, sleep till %s", current_time, sleep_till)
    tick = 4.9999999999999996e-05
    while time() <= sleep_till:
        sleep(tick)


def main():
    transmit(code, pulse_length, gpio_tx)


if __name__ == '__main__':
    main()
