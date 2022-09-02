# fan_controller
Python prototype to control ceiling fan ( H52-5B ) through 315Mhz transmitter

Recorded from remote with FCC ID: A25-TX005R

# Tranmission parameters

* Modulation: ASK
* Pulse Width: 450ms
* Coding: NRZ
* Zeros and ones have equal pulse width. GPIO set to high for 405ms means 1, while GPIO set to low for 450 ms means 0.

# Protocol

Every messages remotes sends 5 times, with pause between message 850us. 

Every message has remote ID + command + ending:
* Remote ID is unique 6 bytes identifier every remote has. Fan learn this identifier during pairing session. 
* Command is an actual command for the fan. See table below
* Ending is 9 bits `0b001011001`. They are always the same in every message.

## Commands

|  Action |  Code  |
| ------------ | ------------ |
| Pair remote | 0x9659 |
|  High Speed |  0x92db |
|   Medium speed | 0xb2db |
| Low Speed | 0x96db |
| Turn off fan | 0xb6cb |
| Toggle light on/off | 0x92cb |

## Remote ID
Can be any value between `0x96db2c96592d` and `0x136db2c96592b`, including these values. Maybe range even bigger, but I don't want to spend time finding precise ranges. I can confirm that `0xFFFFFFFFFFFF` doesn't work as well as `0xb6db2c96592c`.

## Example
 Let's assume you have fan you paired earlier with remote ID `0x96d97db34b24`. Then to send a command to toggle light you send `0x96d97db34b24` + `0x92cb` + `0b001011001`. Which in binary format will be `0b1001011011011001011111011011001101001011001001001001001011001011001011001`


# RUN
`poetry run main`
