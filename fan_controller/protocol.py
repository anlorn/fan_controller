from enum import Enum


COMMANDS = {
    'PAIR': '0x9659',
    'FAN_HIGH': '0x92DB',
    'FAN_MEDIUM': '0xB2DB',
    'FAN_LOW': '0x96DB',
    'FAN_OFF': '0xB6CB',
    'LIGHT_TOGGLE': '0x92CB',
}


ENDING = '0b001011001'


PULSE_LENGTH = 200  # us
PAUSE_BETWEEN_REPEATS = 24000  # us
REPEAT_TIMES = 10
